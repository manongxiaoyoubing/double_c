from flask import Flask, request, jsonify
from flask_cors import CORS
from config import Config
from db import db
from models import User, Policy, PolicyClause, ReviewRecord, ReviewDetail, QALog, SystemConfig, OperationLog, PolicyIndustry, PolicyRegion

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 初始化扩展
    db.init_app(app)

    # 配置CORS（允许前端 localhost:5173 携带 cookie）
    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173", "supports_credentials": True}})

    # 全局错误处理器
    @app.errorhandler(Exception)
    def handle_exception(e):
        response = jsonify({
            'code': 500,
            'message': f'服务器错误: {str(e)}'
        })
        response.status_code = 500
        return response

    @app.errorhandler(404)
    def handle_404(e):
        return jsonify({'code': 404, 'message': '接口不存在'}), 404

    # 注册蓝图
    from api.auth import auth_bp
    from api.qa import qa_bp
    from api.policy import policy_bp
    from api.review import review_bp

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(qa_bp, url_prefix='/api/qa')
    app.register_blueprint(policy_bp, url_prefix='/api/policy')
    app.register_blueprint(review_bp, url_prefix='/api/review')

    # 健康检查接口
    @app.route('/api/health')
    def health_check():
        return jsonify({'status': 'ok'}), 200

    # 创建数据库表
    with app.app_context():
        db.create_all()
        if not User.query.filter_by(username='admin').first():
            admin_user = User(
                username='admin',
                password='admin123',
                role='admin',
                real_name='管理员'
            )
            db.session.add(admin_user)
            db.session.commit()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
