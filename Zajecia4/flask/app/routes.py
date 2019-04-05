from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pasza'}
    zajecia = [
        {
            'temat': 'Przypomnienie Pythona',
            'tresc': 'Na pierwszych zajęciach poznawaliśmy zaawansowane sztuczki w pythonie.'
        },
        {
            'temat': 'Numpy',
            'tresc': 'Na drugich zajęciach były liczone numeryczne całki'
        }
    ]
    return render_template('index.html', title='Zajęcia Inceptio', user=user, zajecia=zajecia)

#  Jak kogoś ciekawi jak to jest robione http://jinja.pocoo.org/