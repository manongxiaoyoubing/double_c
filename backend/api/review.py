from flask import Blueprint, request, jsonify
from db import db
from models import ReviewRecord, ReviewDetail
from utils.compliance_engine import ComplianceEngine
from datetime import datetime

review_bp = Blueprint('review', __name__)

@review_bp.route('/submit', methods=['POST'])
def submit_review():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'code': 400, 'message': '请求体不能为空'}), 400
        
        # 创建审查记录
        record = ReviewRecord(
            user_id=request.environ.get('user_id', 0),
            project_name=data.get('project_name', ''),
            project_type=data.get('project_type', ''),
            industry=data.get('industry', ''),
            region=data.get('region', ''),
            energy_consumption=data.get('energy_consumption'),
            carbon_emission=data.get('carbon_emission')
        )
        db.session.add(record)
        db.session.commit()
        
        # 调用合规引擎
        engine = ComplianceEngine()
        result = engine.check_compliance(record.id)
        
        # 更新审查结果
        record.review_result = result.get('overall_result', 'unknown')
        record.compliance_score = result.get('score', 0)
        record.overall_conclusion = result.get('conclusion', '')
        record.status = 'completed'
        record.reviewed_at = datetime.now()
        db.session.commit()
        
        return jsonify({
            'code': 200,
            'message': '审查完成',
            'data': record.to_dict()
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': str(e)}), 500

@review_bp.route('/<int:review_id>', methods=['GET'])
def get_review_result(review_id):
    try:
        record = ReviewRecord.query.get(review_id)
        if not record:
            return jsonify({'code': 404, 'message': '审查记录不存在'}), 404
        
        details = ReviewDetail.query.filter_by(review_id=review_id).all()
        
        return jsonify({
            'code': 200,
            'data': {
                'record': record.to_dict(),
                'details': [d.to_dict() for d in details]
            }
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': str(e)}), 500

@review_bp.route('/history', methods=['GET'])
def get_review_history():
    try:
        records = ReviewRecord.query.order_by(ReviewRecord.created_at.desc()).limit(50).all()
        return jsonify({
            'code': 200,
            'data': [r.to_dict() for r in records]
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': str(e)}), 500
