import sqlite3

conn = sqlite3.connect('mod3_pract/sqlite3/my.test.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS my(
               id INTEGER PRIMERY KEY,
               name TEXT,
               phone TEXT,
               age INEGER)
''')

# user_date = [(1,'Sergey', '0730798909', 31), 
#              (2,'Sofia', '07398909', 22)]
# cursor.executemany("INSERT INTO my (id,name,phone,age) VALUES(?,?,?,?)", user_date)
# conn.commit()

connect_db = cursor.execute("SELECT * FROM my")
cursor.execute("DELETE FROM my WHERE age < 30")
conn.commit()
for ind, data in enumerate(cursor.execute("SELECT * FROM my")):
    print(f'{ind}: {data}')


