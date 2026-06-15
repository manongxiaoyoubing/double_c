from flask import Blueprint, request, jsonify, current_app
from db import db
from models import Policy, PolicyClause, PolicyIndustry, PolicyRegion
import os
from datetime import datetime

policy_bp = Blueprint('policy', __name__)

@policy_bp.route('/list', methods=['GET'])
def list_policies():
    try:
        policies = Policy.query.filter_by(status='active').all()
        return jsonify({
            'code': 200,
            'data': [p.to_dict() for p in policies]
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': str(e)}), 500

@policy_bp.route('/upload', methods=['POST'])
def upload_policy():
    try:
        if 'file' not in request.files:
            return jsonify({'code': 400, 'message': '请选择文件'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'code': 400, 'message': '请选择文件'}), 400
        
        # 保存文件
        filename = file.filename
        file_path = os.path.join(current_app.root_path, '..', 'data', 'uploads', filename)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        file.save(file_path)
        
        # 创建政策记录
        policy = Policy(
            title=request.form.get('title', filename),
            file_name=filename,
            file_path=file_path,
            file_type=filename.split('.')[-1].lower(),
            industry=request.form.get('industry', ''),
            region=request.form.get('region', '')
        )
        db.session.add(policy)
        db.session.commit()
        
        return jsonify({
            'code': 200,
            'message': '上传成功',
            'data': policy.to_dict()
        })
    except Exception as e:
        return jsonify({'code': 500, 'message': str(e)}), 500

@policy_bp.route('/<int:policy_id>', methods=['DELETE'])
def delete_policy(policy_id):
    try:
        policy = Policy.query.get(policy_id)
        if not policy:
            return jsonify({'code': 404, 'message': '政策不存在'}), 404
        
        policy.status = 'deleted'
        policy.deleted_at = datetime.now()
        db.session.commit()
        
        return jsonify({'code': 200, 'message': '删除成功'})
    except Exception as e:
        return jsonify({'code': 500, 'message': str(e)}), 500
