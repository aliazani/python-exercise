import sqlite3


def get_info(name, family_name, age, sex):
    query = conn.execute(
        f''''INSERT INTO people(Name, Family_name, Age, Sex) VALUES('{name}', '{family_name}', {age}, '{sex}')
    
               ''')

    conn.execute(query)


conn = sqlite3.connect('exercise.db')
conn.execute('''CREATE TABLE people(
        ID PRIMARY KEY INTEGER AUTOINCREMENT,
        Name    VARCHAR(45), 
        Family_name   VARCHAR(45),
        Age     INT,
        Sex     VARCHAR(1)) ''')
