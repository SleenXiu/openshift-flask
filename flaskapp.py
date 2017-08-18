# coding=utf-8

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'hello openshift'

@app.route('/test')
def test():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080')
