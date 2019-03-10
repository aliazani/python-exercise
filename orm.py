from sqlalchemy import create_engine

db_conn = 'sqlite:///F:\\rez.db'
engine = create_engine(db_conn, echo=True)
engine.execute("select 1").scalar()

