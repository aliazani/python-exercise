import sqlite3


def add_user(conn, username, age):
    # username = "ali', 21); DELETE FROM company ; INSERT INTO Person (name, age) VALUES ('Ali"
    # "INSERT INTO Person (name, age) VALUES ('ali', 21); " \
    # "DELETE FROM company ; " \
    # "INSERT INTO Person (name, age) VALUES ('Ali', {age})"
    query = f"INSERT INTO Person (name, age) VALUES ('{username}', {age})"
    conn.execute(query)
    conn.commit()


conn = sqlite3.connect("new_table.sqlite")

conn.execute('''
 CREATE TABLE IF NOT EXISTS Person
     (ID INTEGER PRIMARY KEY  AUTOINCREMENT,
     NAME           TEXT    NOT NULL,
     AGE            INT     NOT NULL);''')

add_user(conn, "Jack", 21)
add_user(conn, "John", 41)
add_user(conn, "Emma", 29)
add_user(conn, "Jacob", 43)
