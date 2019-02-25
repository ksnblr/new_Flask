from flask import Flask
app = Flask(__name__)


@app.route('/') # Fill this in!
def index():
    return "<H1><B> Welcome to my Generic Page</B></H1>"

@app.route('/puppy/<name>') # Fill this in!
def puppylatin(name):
    return "<H1><B> Welcome to my Generic Page {} </B></H1>".format(name)

if __name__ == '__main__':
    app.run()
