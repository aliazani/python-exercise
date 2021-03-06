from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, INTEGER
from sqlalchemy.orm import sessionmaker, aliased
from sqlalchemy import and_, or_

db_conn = 'sqlite:///F:\\People.db'
engine = create_engine(db_conn, echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'People'
    idi = Column(INTEGER, primary_key=True)
    name = Column(String)
    last_name = Column(String)
    password = Column(String)

    def __init__(self, name, last_name, password):
        self.name = name
        self.last_name = last_name
        self.password = password

    def __repr__(self):
        return f"<User('{self.name}', '{self.last_name}', '{self.password}')>"

# CRUD : Create
# Base.metadata.create_all(engine)
# add_user = User("ali", "azn", "sdasdnac")
# print(add_user.idi)
# print(add_user.name)
# session.add(add_user)
# session.commit()
# ---> create multi user:
# session.add_all([
#     User("ali", "rezai", "pass"),
#     User("ahmad", "ahmdi", "pass2")K
# ])
# session.commit()
# my_user = session.query(User).filter_by(name="ahmad").first()
# print(my_user)
# my_user.password = "pass2 new"
# print(my_user)

# print(session.new)
# CRUD : Read
# my_user = session.query(User).filter_by(name="ali").first()
# print(my_user)
# print(my_user.name)
# print(my_user.password)
# all_users = session.query(User).all()
# for user in all_users:
#     print(user.name)
# state session
# transient
# pending
# persistent
# detach


# rollback

# fake_user = User("fake", "invalid", "12345")
# session.add(fake_user)
# print(fake_user in session)
# session.rollback()
# print(fake_user in session)

# query
# for instance in session.query(User).order_by(User.idi):
#     print(instance)

# for name, full_name in session.query(User.name, User.last_name):
#     print(name, full_name)

# for row in session.query(User.name.label('Name')).all():
#     print(row.Name)

# alias
# user_alias = aliased(User, name="user_alias")
# for row in session.query(user_alias, user_alias.name).all():
#     print(row.user_alias)

# order
# for row in session.query(User).order_by(User.idi)[1:3]:
#     print(row)

# filter
# for n in session.query(User.name).filter_by(name="ahmad").first():
#     print(n)

# for n in session.query(User.name).filter_by(name="ahmad").all():
#     print(n)

# for n in session.query(User).filter(User.last_name == 'azn'):
#     print(n)

# and
# for n in session.query(User).filter(User.name == 'ali').filter(User.last_name == 'azn'):
#     print(n)
#
# for n in session.query(User).filter(User.last_name !='azn'):
#     print(n)

# for i in session.query(User).filter(User.password.like('%pass%')):
#     print(i)

# for n in session.query(User).filter(User.name.in_(['ali', 'majid'])):
#     print(n)

# for n in session.query(User).filter(~User.name.in_(['ali', 'majid'])):
#     print(n)

# for n in session.query(User).filter(User.last_name == None):
#     print(n)
#
# for n in session.query(User).filter(User.last_name != None):
#     print(n)

# for n in session.query(User).filter(and_(User.last_name != None, User.password == 'pass')):
#     print(n)
#
# for n in session.query(User).filter(or_(User.last_name != None, User.password == 'pass')):
#     print(n)

# another kind of query
# # from_statement
# for user in session.query(User).from_statement(r"SELECT * From People Where name=:name").params(name='ahmad').all():
#     print(user)
#

