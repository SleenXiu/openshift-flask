# coding=utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello openshift'

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/xiu')
def xiu():
    return "hello xiu"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
