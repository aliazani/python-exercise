from sqlalchemy import create_engine

db_conn = 'sqlite:///F:\\dvdrental\\dvdrental\\toc.dat'
engine = create_engine(db_conn, echo=True)
engine.execute('select 1').scalar()
