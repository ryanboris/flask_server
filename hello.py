from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/users')
def users():
    if request.method == 'POST':
        return request.form['username']
