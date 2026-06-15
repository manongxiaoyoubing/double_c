from datetime import datetime
from db import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default='user')
    real_name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    last_login_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    is_active = db.Column(db.Boolean, default=True)
    deleted_at = db.Column(db.DateTime)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'role': self.role,
            'real_name': self.real_name,
            'email': self.email,
            'phone': self.phone,
            'last_login_at': self.last_login_at.isoformat() if self.last_login_at else None,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'is_active': self.is_active
        }

class Policy(db.Model):
    __tablename__ = 'policies'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    file_name = db.Column(db.String(200))
    file_path = db.Column(db.String(500))
    file_type = db.Column(db.String(20))
    file_size = db.Column(db.Integer)
    industry = db.Column(db.String(100))
    region = db.Column(db.String(100))
    policy_level = db.Column(db.String(20))
    effective_date = db.Column(db.Date)
    expiry_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='active')
    uploaded_by = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    chunk_count = db.Column(db.Integer, default=0)
    indexed = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'file_name': self.file_name,
            'file_type': self.file_type,
            'industry': self.industry,
            'region': self.region,
            'policy_level': self.policy_level,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'chunk_count': self.chunk_count,
            'indexed': self.indexed
        }

class PolicyClause(db.Model):
    __tablename__ = 'policy_clauses'
    id = db.Column(db.Integer, primary_key=True)
    policy_id = db.Column(db.Integer, db.ForeignKey('policies.id'), nullable=False)
    clause_index = db.Column(db.Integer)
    clause_text = db.Column(db.Text, nullable=False)
    clause_type = db.Column(db.String(50))
    energy_type = db.Column(db.String(50))
    threshold_value = db.Column(db.Float)
    threshold_unit = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'policy_id': self.policy_id,
            'clause_index': self.clause_index,
            'clause_text': self.clause_text,
            'clause_type': self.clause_type,
            'energy_type': self.energy_type,
            'threshold_value': self.threshold_value,
            'threshold_unit': self.threshold_unit
        }

class ReviewRecord(db.Model):
    __tablename__ = 'review_records'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    project_name = db.Column(db.String(200), nullable=False)
    project_type = db.Column(db.String(50))
    industry = db.Column(db.String(100))
    region = db.Column(db.String(100))
    project_scale = db.Column(db.Float())
    energy_consumption = db.Column(db.Float())
    carbon_emission = db.Column(db.Float())
    production_capacity = db.Column(db.Float())
    review_result = db.Column(db.String(20))
    compliance_score = db.Column(db.Float())
    overall_conclusion = db.Column(db.Text)
    detail_result = db.Column(db.Text)
    report_path = db.Column(db.String(500))
    report_format = db.Column(db.String(10), default='pdf')
    status = db.Column(db.String(20), default='pending')
    submitted_at = db.Column(db.DateTime, default=datetime.now)
    reviewed_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'project_name': self.project_name,
            'project_type': self.project_type,
            'industry': self.industry,
            'region': self.region,
            'review_result': self.review_result,
            'compliance_score': self.compliance_score,
            'status': self.status,
            'submitted_at': self.submitted_at.isoformat() if self.submitted_at else None
        }

class ReviewDetail(db.Model):
    __tablename__ = 'review_details'
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column(db.Integer, db.ForeignKey('review_records.id'), nullable=False)
    policy_id = db.Column(db.Integer, db.ForeignKey('policies.id'))
    clause_id = db.Column(db.Integer, db.ForeignKey('policy_clauses.id'))
    check_item = db.Column(db.String(200))
    requirement = db.Column(db.Text)
    actual_value = db.Column(db.String(200))
    threshold_value = db.Column(db.String(200))
    is_compliant = db.Column(db.Boolean())
    conclusion = db.Column(db.Text)
    suggestion = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'review_id': self.review_id,
            'check_item': self.check_item,
            'is_compliant': self.is_compliant,
            'conclusion': self.conclusion
        }

class QALog(db.Model):
    __tablename__ = 'qa_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    policy_id = db.Column(db.Integer, db.ForeignKey('policies.id'))
    question = db.Column(db.Text, nullable=False)
    answer = db.Column(db.Text)
    source_clauses = db.Column(db.Text)
    tokens_used = db.Column(db.Integer)
    processing_time = db.Column(db.Float())
    created_at = db.Column(db.DateTime, default=datetime.now)
    error_message = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'question': self.question,
            'answer': self.answer,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class SystemConfig(db.Model):
    __tablename__ = 'system_configs'
    id = db.Column(db.Integer, primary_key=True)
    config_key = db.Column(db.String(100), unique=True, nullable=False)
    config_value = db.Column(db.Text)
    config_type = db.Column(db.String(20), default='string')
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'config_key': self.config_key,
            'config_value': self.config_value,
            'config_type': self.config_type,
            'description': self.description
        }

class OperationLog(db.Model):
    __tablename__ = 'operation_logs'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    operation_type = db.Column(db.String(50), nullable=False)
    target_type = db.Column(db.String(50))
    target_id = db.Column(db.Integer)
    operation_desc = db.Column(db.Text)
    ip_address = db.Column(db.String(50))
    user_agent = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'operation_type': self.operation_type,
            'operation_desc': self.operation_desc,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class PolicyIndustry(db.Model):
    __tablename__ = 'policy_industries'
    id = db.Column(db.Integer, primary_key=True)
    policy_id = db.Column(db.Integer, db.ForeignKey('policies.id'), nullable=False)
    industry_name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'policy_id': self.policy_id,
            'industry_name': self.industry_name
        }

class PolicyRegion(db.Model):
    __tablename__ = 'policy_regions'
    id = db.Column(db.Integer, primary_key=True)
    policy_id = db.Column(db.Integer, db.ForeignKey('policies.id'), nullable=False)
    region_name = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'policy_id': self.policy_id,
            'region_name': self.region_name
        }
