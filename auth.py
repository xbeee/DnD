from instance.models import *
from core import *

# автаризация
@api.route('/login', methods=['POST'])
def Login():
    # беру имя из формы
    try:
        name = request.form.get('name')
    except:
        resp = {
            "errCode": 1,
            "errString": "нехватает данных"
        }
        return resp, 401

    # если не нашёл такого игрока
    user = User.query.filter_by(name=name).first()
    if user is None:
        resp = {
            "errCode": 2,
            "errString": "неверный логин"
        }
        return resp, 401

    # меняю статус
    user.status = True
    db.session.commit()

    token = create_access_token(identity=name)
    heroes = []
    if(user.role == 'user'):
        # если игрок
        query = Heroes.query.filter_by(user=name).all()
        for hero in query:
            heroes.append({
                'name': hero.name,
                'klas': hero.klas,
                'race': hero.rase,
                'lvl': hero.lvl,
            })
    return {
        'access_token':token,
        'role': user.role,
        'heroes': heroes
    }

# выход из акаунта
@api.route('/logout')
@jwt_required()
def Logout():
    # отключил игрока от лобби
    name = get_jwt()["sub"]
    user = User.query.filter_by(name=name).first()
    user.status = False
    db.session.commit()
    # убрал JWT
    resp = jsonify({"msg":"logout successful"})
    unset_jwt_cookies(resp)
    # уведомление мастеру
    send('disconnect', {
        'msg': 'disconnect',
        'user': name
    })
    return resp