from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/login/<name>/<int:rep>')
def login(name, rep):
    return render_template('login.html', name=name, path="https://www.google.com", rep=rep)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080,)
