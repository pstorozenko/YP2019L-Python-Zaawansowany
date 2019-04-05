from app import app
from flask import render_template
from flask import Flask, redirect, url_for, request

from app.plot_maker import do_the_plot, check_fun

@app.route('/', methods = ['POST', 'GET'])
@app.route('/index', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':

        x0 = request.form['x0']
        xk = request.form['xk']
        fun_name = request.form['fun']
        
        fun = check_fun(fun_name)
        
        if fun is None:
            msg = "Nie ma takiej funkcji"
            return render_template('index.html', message = msg )
        else:
            dest = '/static/images/'
            url = do_the_plot(dest, x0, xk, fun)
            return render_template('index.html', url=url )
    else:
        return render_template('index.html')
        
    


#  Jak kogoś ciekawi jak to jest robione http://jinja.pocoo.org/
