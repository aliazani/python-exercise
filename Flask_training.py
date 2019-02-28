from flask import Flask

app = Flask(__name__)


@app.route('/')
def welcome():
    return 'Welcome'


@app.route('/ali')
def name():
    return 'your name is ali'


if __name__ == '__main__':
    app.run()
