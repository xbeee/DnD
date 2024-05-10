from instance.models import *
from core import *

# автаризация
@api.route('/login', methods=['POST'])
def Login():
    name = request.form.get('name')
    user = User.query.filter_by(name=name).first()
    if user is None:
        return redirect('/')

    if(user.role == 'GM'):
        return render_template('gamemaster.html')
    heroes = []
    if(user.role == 'User'):
        # если игрок
        query = Heroes.query.filter_by(user=name).all()
        for hero in query:
            heroes.append({
                'name': hero.name,
                'klas': hero.klas,
                'race': hero.rase,
                'lvl': hero.lvl,
            })
        return render_template('heroes.html', heroes=heroes)

# выход из акаунта
@api.route('/logout/<name>')
def Logout(name):
    # отключил игрока от лобби
    user = User.query.filter_by(name=name).first()
    user.status = False
    db.session.commit()
    # уведомление мастеру
    send('disconnect', {
        'msg': 'disconnect',
        'user': name
    })
    return redirect('/')