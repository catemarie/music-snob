import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO events (title, content) VALUES (?, ?)",
            ('First Event', 'Content for the first event')
            )

cur.execute("INSERT INTO events (title, content) VALUES (?, ?)",
            ('Second Event', 'Content for the second event')
            )

connection.commit()
connection.close()