import sys
sys.path.append('../')

from core import *
from instance.models import *

@api.route('/start/<hero>', methods=['GET'])
@jwt_required()
def Start(hero):
    if Heroes.query.filter_by(name=hero).first() is None:
        resp = {
            "errCode": 3,
            "errString": "нет такого героя"
        }
        return resp, 404
    
    # основная инфа
    hero = Heroes.query.filter_by(name=hero).first()
    klas = KlassData.query.filter((KlassData.klas==hero.klas)&(KlassData.lvl==hero.lvl)).first()
    race = RaceData.query.filter_by(race=hero.race).first()
    variant = VariantData.query.filter_by(variant=hero.variant).first()
    resp = {
        'can_spell': hero.can_spell, # 0 - не может, 1 - может все, 2 - может не все
        'name': hero.name,
        'klas': hero.klas,
        'race': hero.rase,
        'variant': hero.variant, 
        'lvl': hero.lvl,
        'exp': hero.exp,
        'count_mana': hero.count_mana.split(','),
        'max_spell': klas.max_spell,
        'max_mana': klas.max_mana.split(','),
        'name_mana': klas.name_mana,
        'klass_disc': klas.disc,
        'klas_skill': klas.skill,
        'race_disc': race.disc,
        'race_skill': race.skill,
        'variant_disc': variant.disc,
        'variant_skill': variant.skill,
        'spell': [],
    }
    # заполняем спелы
    query = HeroesSpell.query.filter_by(hero=hero.id).all()
    for el in query:
        spell = Spell.query.filter_by(id=el.spell).first()
        resp['spell'].append({
            'title': spell.title,
            'short_disc': spell.short_disc,
            'disc': spell.disc,
            'cost': spell.cost,
            'lvl_mana': spell.lvl_mana,
        })
    send('connect', {
        'msg': 'connect',
        'user': get_jwt()["sub"],
        'hero': resp
    })
    return resp, 200

@api.route('/newHero', methods=['POST'])
@jwt_required()
def NewHero():
    try:
        name = request.form['name']
        klas = request.form['klas']
        race = request.form['race']
        variant = request.form['variant']
        lvl = request.form['lvl']
    except:
        resp = {
            "errCode": 1,
            "errString": "нехватает данных"
        }
        return resp, 401
    
    spell = Spell.query.filter((Spell.klas==klas)&(Spell.variant==variant)).all()
    # выкидываем лохов
    if spell is None:
        hero = Heroes(user=get_jwt()["sub"], name=name, klas=klas, race=race, variant=variant, lvl=lvl)
        db.session.add(hero)
        db.session.commit()
        return redirect(f'/start/{name}') # хз работает ли
    
    queryKlas = KlassData.query.filter((KlassData.klas==klas)&(KlassData.lvl==lvl)).first()
    # выкидываем индивидуальных
    if queryKlas.max_spell >= spell.count():
        hero = Heroes(user=get_jwt()["sub"], name=name, klas=klas, race=race, variant=variant, lvl=lvl, can_spell=1)
        db.session.add(hero)
        for el in spell:
            s = HeroesSpell(hero=name, spell=el.id)
            db.session.add(hero)
        db.session.commit()
        return redirect(f'/start/{name}') # хз работает ли

    # заклинатели
    resp = []
    for el in spell:
        resp.append({
            'title': el.title,
            'short_disc': el.short_disc,
            'disc': el.disc,
            'cost': el.cost,
            'lvl_mana': el.lvl_mana,
        })
    return {
        'msg': 'надо выбрать заклинания',
        'spell': resp
    }, 200