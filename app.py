from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hey There!"


@app.route('/<name>')
def name(name):
    return "Hallo {}".format(name)


if __name__ == '__main__':
    app.run()
