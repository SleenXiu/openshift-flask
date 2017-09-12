
from flask import render_template, request, redirect, url_for, jsonify
from ..models import User
from . import main

@main.route('/xiu')
def xiu():
    u = User.objects(username='xiu').first()
    if u: 
        return redirect(url_for('main.index'))
    u = User(username='xiu', password='xiu')
    u.save()
    return "create xiu!-- kown nothing"

@main.route('/')
def index():
    s = User.objects().order_by('-id')
    return render_template('index.html', users=s)

