from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, INTEGER
from sqlalchemy.orm import sessionmaker

db_conn = 'sqlite:///F:\\rez.db'
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
# add_user = User("ali", "azani", "Aliazani1378")
# print(add_user.idi)
# print(add_user.name)
# session.add(add_user)
# session.commit()
# CRUD : Read
my_user = session.query(User).filter_by(name="ali").first()
print(my_user)
