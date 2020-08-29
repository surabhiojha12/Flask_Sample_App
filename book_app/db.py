import sqlite3

conn = sqlite3.connect('books.sqlite')

cursor = conn.cursor()

sql_query = """ CREATE TABLE book(
             id integer NOT NULL PRIMARY KEY AUTOINCREMENT,
             name text NOT NULL,
             price float NOT NULL
            )"""

cursor.execute(sql_query)