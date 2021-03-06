#!/usr/bin/env python
# coding=utf-8

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'akd3091ajds4vlr3nddj90312edad'
    
    
    @staticmethod
    def init_app():
        pass

class DevelopmentConfig(BaseConfig):
    DEBUG = True

    MONGODB_SETTINGS = {
        'db': 'xiudb',
        'host': '172.30.180.73:27017',
        'username': 'xiu',
        'password': 'xiu'
    }


config = {
    'dev': DevelopmentConfig,
}
