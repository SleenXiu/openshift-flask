#!/usr/bin/env python
# coding=utf-8

from flaskapp import app as application

if __name__ == '__main__':
    application.run(host='0.0.0.0', port='8080')
