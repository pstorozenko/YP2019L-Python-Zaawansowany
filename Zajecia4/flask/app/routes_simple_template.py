from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pasza'}
    return render_template('index.html', title='Zajęcia Inceptio', user=user)

#  Jak kogoś ciekawi jak to jest robione http://jinja.pocoo.org/