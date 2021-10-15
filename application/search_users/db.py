from psycopg2 import Error
from sqlalchemy import func
from sqlalchemy import orm, create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from application.bot_message.get_token import get_token
from application.search_users.r_json import get_maxID_from_json

def get_engine():
    v = get_token()
    DSN = v[2]
    engine = create_engine(DSN)
    return engine

Base = declarative_base()

class Usersdb(Base):
    __tablename__ = 'accept_users'
    id = Column(Integer(), primary_key=True)
    usersid = Column(Integer(), nullable=False)
    username = Column(String(30), nullable=False)

def new_data(list_of_candidate):
    try:
        engine = get_engine()
        Session = orm.sessionmaker(bind=engine)
        Base.metadata.create_all(engine)
        with Session() as session:
            session.query(Usersdb).delete()
            session.commit()

        for user in list_of_candidate:
            a_user = Usersdb(usersid = user['id'],username = user['first_name'])

            with Session() as session:
                session.add(a_user)
                session.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

def get_last_userid():
    try:
        engine = get_engine()
        Session = orm.sessionmaker(bind=engine)
        with Session() as session:
            maxuserID = session.query(func.max(Usersdb.usersid)).scalar()

    except (Exception, Error) as error:
        maxuserID = get_maxID_from_json()


    return maxuserID

def delete_data():
    try:
        engine = get_engine()
        Session = orm.sessionmaker(bind=engine)
        with Session() as session:
            session.query(Usersdb).delete()
            session.commit()
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)













