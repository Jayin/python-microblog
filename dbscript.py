#encoding:utf-8

from app import db, models


def init_db():
    db.drop_all()
    db.create_all()

    u = models.User(nickname='john', email='john@email.com', role=models.ROLE_USER)
    db.session.add(u)

    u = models.User(nickname='jack', email='jack@email.com', role=models.ROLE_USER)
    db.session.add(u)


    u = models.User(nickname='mars', email='mars@email.com', role=models.ROLE_USER)
    db.session.add(u)

    u = models.User(nickname='Peter', email='Peter@email.com', role=models.ROLE_USER)
    db.session.add(u)
    db.session.u

    db.session.commit()

def query():
    res = models.User.query.filter().offset(1).limit(2).all()
    print res

def update():
    res  = models.User.query.filter_by(nickname='john').first()
    res.nickname = 'John'
    db.session.add(res)
    db.session.commit()
    print res

# query()
update()