from langchain.documents import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from config import Config
import os

class RAGEngine:
    def __init__(self):
        self.embedings = HuggingFaceEmbeddings(model_name="paraphrase-multilingual-MiniLM-L12-v2")
        self.faiss_path = Config.FAISS_INDEX_PATH
        self.text_splitter = CharacterTextSplitter(
            chunk_size=Config.RAG_CHUNK_SIZE,
            chunk_overlap=Config.RAG_CHUNK_OVERLAP
        )
    
    def process_document(self, file_path, policy_id):
        """处理文档并创建向量索引"""
        # 读取文档内容
        from utils.document_processor import DocumentProcessor
        processor = DocumentProcessor()
        text = processor.read_file(file_path)
        
        # 分块
        chunks = self.text_splitter.split_text(text)
        
        # 创建向量索引
        if os.path.exists(self.faiss_path):
            vectorstore = FAISS.load_local(self.faiss_path, self.embedings)
            vectorstore.add_texts(chunks, metadatas=[{"policy_id": policy_id, "chunk_index": i} for i in range(len(chunks))])
        else:
            vectorstore = FAISS.from_texts(chunks, self.embedings, metadatas=[{"policy_id": policy_id, "chunk_index": i} for i in range(len(chunks))])
        
        vectorstore.save_local(self.faiss_path)
        return len(chunks)
    
    def ask(self, question, policy_id=None):
        """回答问题"""
        if not os.path.exists(self.faiss_path):
            return {"answer": "暂无政策数据，请先上传政策文件", "sources": []}
        
        # 加载向量索引
        vectorstore = FAISS.load_local(self.faiss_path, self.embedings)
        
        # 相似度搜索
        if policy_id:
            docs = vectorstore.similarity_search(question, k=3, filter={"policy_id": policy_id})
        else:
            docs = vectorstore.similarity_search(question, k=3)
        
        # 构建上下文
        context = "\n\n".join([doc.page_content for doc in docs])
        
        # 调用LLM生成回答
        from langchain.chat_models import ChatOpenAI
        llm = ChatOpenAI(
            model=Config.MODEL_NAME,
            openai_api_key=Config.API_KEY,
            openai_api_base=Config.API_URL
        )
        
        prompt = f"""基于以下政策内容回答问题：
        
政策内容：
{context}

问题：{question}

请基于政策内容准确回答，不要编造信息。"""
        
        response = llm.predict(prompt)
        
        return {
            "answer": response,
            "sources": [doc.page_content[:200] for doc in docs]
        }
