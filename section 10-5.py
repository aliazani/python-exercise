import sqlite3

conn = sqlite3.connect("database.sqlite")

conn.execute('''CREATE TABLE IF NOT EXISTS COMPANY
         (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL,
         ADDRESS        CHAR(50),
         SALARY         REAL);''')

conn.execute(
    """INSERT INTO COMPANY (NAME,AGE,ADDRESS,SALARY) 
    VALUES ('{}', {}, '{}', 20000.00 )""")

conn.commit()
