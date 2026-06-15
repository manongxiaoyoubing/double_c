from flask import Blueprint, request, jsonify, session

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'code': 400, 'message': '请求体不能为空'}), 400
        
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        
        if not username or not password:
            return jsonify({'code': 400, 'message': '用户名和密码不能为空'}), 400
        
        from models import User
        user = User.query.filter_by(username=username).first()
        
        if user and user.password == password:
            session['user_id'] = user.id
            session['username'] = user.username
            session['role'] = user.role
            return jsonify({
                'code': 200,
                'message': '登录成功',
                'data': {
                    'username': user.username,
                    'role': user.role,
                    'real_name': user.real_name
                }
            })
        
        return jsonify({'code': 401, 'message': '用户名或密码错误'}), 401
    except Exception as e:
        return jsonify({'code': 500, 'message': f'登录失败: {str(e)}'}), 500

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({'code': 200, 'message': '已退出登录'})

@auth_bp.route('/me', methods=['GET'])
def get_current_user():
    if 'user_id' not in session:
        return jsonify({'code': 401, 'message': '未登录'}), 401
    return jsonify({
        'code': 200,
        'data': {
            'username': session.get('username'),
            'role': session.get('role')
        }
    })
