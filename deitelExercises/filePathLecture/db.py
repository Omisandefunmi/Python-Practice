import sqlite3

with sqlite3.connect(":memory:") as connection:
    cursor = connection.cursor()

cursor.execute("CREATE TABLE User (name TEXT, age INT)")