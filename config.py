import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '630dd5c25ceeb8031c1391420e1387bf'