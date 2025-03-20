# Patrick Brown
# 3/20/25
# pabr5825 || patrickbrown-io


# An index to practice deploying 
from flask import Flask
import psycopg2
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World from Patrick Brown in 3308'
@app.route('/db_test')
def testing():
    # Db connection
    conn = psycopg2.connect("postgresql://lab_ten_user:l9Gk7iZ41U78nL2cJtteABJpHhBJrZfw@dpg-cve3e1l2ng1s73ccuqh0-a/lab_ten")
    # Cursor
    cur = conn.cursor()
    # Create our table
    cur.execute('''
    CREATE TABLE IF NOT EXISTS Basketball(
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
''')
    # Commit
    conn.commit()

    conn.close() # end with this to close connection
    return 'Basketball table created!'
