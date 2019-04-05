from app import app
from flask import Flask
from flask import json

from app.my_api_tools import make_summary, LastVisit

lv = LastVisit()

@app.route('/')
def index():
    return "Hello world"        

@app.route('/visit')
def visit():
    return "Last visit: " + str(lv())

@app.route('/summary')
def summary():
    data = make_summary()
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )
    return response


