import sqlite3

con = sqlite3.connect('mod3_pract/testdb_sqlite3.db')

cursor = con.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS  personal_date(
               name TEXT NOT NULL, 
               login TEXT NOT NULL,
               password TEXT NOT NULL)
               ''')

date = [
    ('gmail', 'sergey', 123123),
    ('wow',250525, 813857)
]
cursor.executemany("INSERT INTO personal_date(name, login, password) VALUES(?,?,?)", date)

con.commit()

data = cursor.execute('SELECT * FROM personal_date')
print(data.fetchall())
