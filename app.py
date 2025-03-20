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

# Table init route
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

# Table seed route
@app.route('/db_insert')
def inserting():
    # Db connection
    conn = psycopg2.connect("postgresql://lab_ten_user:l9Gk7iZ41U78nL2cJtteABJpHhBJrZfw@dpg-cve3e1l2ng1s73ccuqh0-a/lab_ten")
    # Cursor
    cur = conn.cursor()
    # Create our table
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        '''
    )
    # Commit
    conn.commit()

    conn.close() # end with this to close connection
    return 'Basketball table successfully seeded!'

# Table seed route
@app.route('/db_select')
def selecting():
    # Db connection
    conn = psycopg2.connect("postgresql://lab_ten_user:l9Gk7iZ41U78nL2cJtteABJpHhBJrZfw@dpg-cve3e1l2ng1s73ccuqh0-a/lab_ten")
    # Cursor
    cur = conn.cursor()
    # Create our table
    cur.execute('''
        SELECT * From Basketball
        '''
    )
    records = cur.fetchall()
    conn.close() # end with this to close connection

    response_string = ""
    response_string += "<table>"
    for player in records:
        response_string+="<tr>"
        for info in player:
            response_string+="<td>{}</td".format(info)
        response_string+="</tr>"
    response_string+="</table>"
    return response_string


@app.route('/db_drop')
def dropping():
    # Db connection
    conn = psycopg2.connect("postgresql://lab_ten_user:l9Gk7iZ41U78nL2cJtteABJpHhBJrZfw@dpg-cve3e1l2ng1s73ccuqh0-a/lab_ten")
    # Cursor
    cur = conn.cursor()
    # Drop table
    cur.execute('''
        DROP TABLE Basketball;
        '''
    )
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"