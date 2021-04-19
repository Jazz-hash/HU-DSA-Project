# ? imports ( Flask, Selectorlib)
from flask import Flask, render_template, request

# ? Creating app with Flask
app = Flask(__name__)

@app.route('/')
def index():
    # ? rendering htm file.
    return render_template('index.htm')