from flask import Blueprint, request, jsonify, current_app
from db import db
from models import QALog, Policy
from utils.rag_engine import RAGEngine
from datetime import datetime

qa_bp = Blueprint('qa', __name__)

@qa_bp.route('/ask', methods=['POST'])
def ask_question():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'code': 400, 'message': '请求体不能为空'}), 400
        
        question = data.get('question', '').strip()
        policy_id = data.get('policy_id')
        
        if not question:
            return jsonify({'code': 400, 'message': '问题不能为空'}), 400
        
        # 调用RAG引擎
        rag = RAGEngine()
        result = rag.ask(question, policy_id)
        
        # 记录日志
        qa_log = QALog(
            user_id=request.environ.get('user_id', 0),
            policy_id=policy_id,
            question=question,
            answer=result.get('answer', ''),
            source_clauses=result.get('sources', '')
        )
        db.session.add(qa_log)
        db.session.commit()
        
        return jsonify({
            'code': 200,
            'data': result
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': str(e)}), 500

@qa_bp.route('/history', methods=['GET'])
def get_qa_history():
    try:
        logs = QALog.query.order_by(QALog.created_at.desc()).limit(50).all()
        return jsonify({
            'code': 200,
            'data': [log.to_dict() for log in logs]
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': str(e)}), 500
