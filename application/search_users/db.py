from sqlalchemy import func
from sqlalchemy import orm, create_engine, MetaData, Table, Integer, String, Column, DateTime, Numeric
from sqlalchemy.ext.declarative import declarative_base
from application.get_token import get_token

v = get_token()
DSN = v[2]

engine = create_engine(DSN)
Session = orm.sessionmaker(bind=engine)

Base = declarative_base()

class Usersdb(Base):
    __tablename__ = 'accept_users'
    id = Column(Integer(), primary_key=True)
    usersid = Column(Integer(), nullable=False)
    username = Column(String(30), nullable=False)
    userphotolink = Column(String(300))
    userphotoid = Column(Numeric)

def new_data(list_of_candidate):
    Base.metadata.create_all(engine)
    with Session() as session:
        session.query(Usersdb).delete()
        session.commit()

    for user in list_of_candidate:

        a_user = Usersdb(usersid = user['id'],username = user['first_name'])
        with Session() as session:
            session.add(a_user)
            session.commit()

def add_data(users_id, photolink):

    with Session() as session:
        session.query(Usersdb).filter(Usersdb.usersid == users_id).update({"userphotolink": photolink})
        session.commit()


def get_last_userid():
    with Session() as session:
        maxuserID = session.query(func.max(Usersdb.usersid)).scalar()

    return maxuserID

def delete_data():
    with Session() as session:
        session.query(Usersdb).delete()
        session.commit()












