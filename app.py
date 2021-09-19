import sqlite3
from flask import Flask

app = Flask(__name__)

@app.route('/')
def init():
    return "html 100"