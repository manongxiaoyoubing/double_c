from db import db
from models import PolicyClause, Policy, ReviewDetail
from datetime import datetime

class ComplianceEngine:
    def check_compliance(self, review_id):
        """检查项目合规性"""
        from models import ReviewRecord
        record = ReviewRecord.query.get(review_id)
        if not record:
            return {"overall_result": "error", "score": 0}
        
        # 获取相关政策条款
        clauses = PolicyClause.query.join(Policy).filter(
            Policy.industry == record.industry
        ).all()
        
        results = []
        compliant_count = 0
        
        for clause in clauses:
            # 检查每一项
            detail = ReviewDetail(
                review_id=review_id,
                policy_id=clause.policy_id,
                clause_id=clause.id,
                check_item=clause.clause_type,
                requirement=clause.clause_text[:200] if clause.clause_text else '',
                is_compliant=None,
                conclusion=''
            )
            
            # 简单判断（实际项目需要更复杂的逻辑）
            if clause.energy_type and record.energy_consumption:
                # 检查能耗
                detail.actual_value = str(record.energy_consumption)
                detail.is_compliant = True  # 简化处理
                detail.conclusion = '符合'
                compliant_count += 1
            
            db.session.add(detail)
            results.append(detail)
        
        db.session.commit()
        
        # 计算得分
        total = len(clauses) if clauses else 1
        score = (compliant_count / total) * 100 if total > 0 else 0
        
        return {
            "overall_result": "compliant" if score >= 60 else "non-compliant",
            "score": round(score, 2),
            "conclusion": f"共检查{total}项，符合{compliant_count}项，得分{score}分"
        }
    
    def generate_report(self, review_id):
        """生成审查报告"""
        from models import ReviewRecord, ReviewDetail
        record = ReviewRecord.query.get(review_id)
        details = ReviewDetail.query.filter_by(review_id=review_id).all()
        
        report = {
            "project_name": record.project_name,
            "industry": record.industry,
            "review_result": record.review_result,
            "compliance_score": record.compliance_score,
            "details": [d.to_dict() for d in details],
            "generated_at": datetime.now().isoformat()
        }
        
        return report
