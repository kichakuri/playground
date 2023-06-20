import sqlite3

conn = sqlite3.connect('Test_DB.db')

cursor=conn.cursor()

try:
    cursor.execute('CREATE TABLE test (name STRING, gender STRING, yob INTEGER')
except Exception as e
    pass

