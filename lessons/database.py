import sqlite3



def create_tables(con):
    con.execute('''CREATE TABLE IF NOT EXISTS todos(
    name TEXT,
    description TEXT,
    status TEXT
    )''')

if __name__ == '__main__':
    con = sqlite3.connect('lessons/database.db')
    create_tables(con)