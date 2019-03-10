from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, INTEGER

db_conn = 'sqlite:///F:\\rez.db'
engine = create_engine(db_conn, echo=True)
Base = declarative_base()


class User(Base):
    __tablename__ = 'some'
    idi = Column(INTEGER, primary_key=True)
    name = Column(String)
    f_name = Column(String)
    password = Column(String)

    def __init__(self, name, f_name, password):
        self.name = name
        self.f_name = f_name
        self.password = password

    def __repr__(self):
        return f"<User('{self.name}', '{self.f_name}', '{self.password}')>"


Base.metadata.create_all(engine)