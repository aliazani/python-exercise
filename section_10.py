from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route('/login/<name>/<int:rep>')
def login(name, rep):
    return render_template('login.html', name=name, path="https://www.google.com", rep=rep)


@app.route('/table/<int:m>/<int:n>')
def table_show(m, n):
    return render_template('table.html', m=m, n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)


# link to connect http://127.0.0.1:8080/login/ali/3
