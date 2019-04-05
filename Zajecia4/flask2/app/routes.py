from app import app
from flask import render_template
from app.plot_maker import do_the_plot

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

@app.route('/secret_plot')
def secret_plot():
    dest = '/static/images/fig.png'
    do_the_plot(dest)
    return render_template('plots.html', plot = dest)

#  Jak kogoś ciekawi jak to jest robione http://jinja.pocoo.org/