from instance.models import *
from core import *

# автаризация
@api.route('/login', methods=['POST'])
def Login():
    try:
        name = request.form.get('name')
    except:
        resp = {
            "errCode": 1,
            "errString": "нехватает данных"
        }
        return resp, 401

    user = User.query.filter_by(name=name).first()
    if user is None:
        resp = {
            "errCode": 2,
            "errString": "неверный логин"
        }
        return resp, 401

    token = create_access_token(identity=name)
    return {'access_token':token}

# выход из акаунта
@api.route('/logout', methods=["POST"])
def Logout():
    resp = jsonify({"msg":"logout successful"})
    unset_jwt_cookies(resp)
    return resp