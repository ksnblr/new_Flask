from flask import flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<H1> Hello Puppies </H1>'

if __name__ == '__main__':
    app.run()
