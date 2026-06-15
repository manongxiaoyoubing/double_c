import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'mysql+pymysql://root:123456@localhost:3306/double_carbon')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # DeepSeek API 配置
    API_TYPE = os.getenv('API_TYPE', 'deepseek')
    API_KEY = os.getenv('API_KEY', '')
    API_URL = os.getenv('API_URL', 'https://api.deepseek.com/v1')
    MODEL_NAME = os.getenv('MODEL_NAME', 'deepseek-chat')

    # RAG 配置
    RAG_CHUNK_SIZE = int(os.getenv('RAG_CHUNK_SIZE', 500))
    RAG_CHUNK_OVERLAP = int(os.getenv('RAG_CHUNK_OVERLAP', 50))
    FAISS_INDEX_PATH = os.getenv('FAISS_INDEX_PATH', 'data/faiss_index')
