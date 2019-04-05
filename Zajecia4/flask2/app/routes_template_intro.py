from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Piotrek'}
    return '''
<html>
    <head>
        <title>Strona główna | zajęcia Incpetio</title>
    </head>
    <body>
        <h1>Cześć, ''' + user['username'] + '''!</h1>
    </body>
</html>'''