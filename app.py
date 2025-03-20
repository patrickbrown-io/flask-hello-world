# Patrick Brown
# 3/20/25
# pabr5825 || patrickbrown-io


# An index to practice deploying 
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World from Patrick Brown in 3308'
