import os
from pypdf import PdfReader
from docx import Document

class DocumentProcessor:
    def read_file(self, file_path):
        """读取文件内容"""
        ext = os.path.splitext(file_path)[1].lower()
        
        if ext == '.pdf':
            return self._read_pdf(file_path)
        elif ext in ['.docx', '.doc']:
            return self._read_docx(file_path)
        elif ext == '.txt':
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        else:
            raise ValueError(f'不支持的文件类型: {ext}')
    
    def _read_pdf(self, file_path):
        """读取PDF文件"""
        text = ""
        reader = PdfReader(file_path)
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text
    
    def _read_docx(self, file_path):
        """读取Word文件"""
        doc = Document(file_path)
        text = ""
        for para in doc.paragraphs:
            text += para.text + "\n"
        return text
    
    def extract_clauses(self, text):
        """从文本中提取条款（简单按段落分割）"""
        paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
        return paragraphs
