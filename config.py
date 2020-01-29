import os
basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS  = False
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MAIL_SERVER = 'stmp.gmail.com'  # os.environ.get('MAIL_SERVER')
    MAIL_PORT = 587  # int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = 1  # os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = 'r4subscribe@gmail.com'  # os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = 'eMR5MRtHtsv65Tx'  # os.environ.get('MAIL_PASSWORD')
    ADMINS = ['rkisyula12@gmail.com']
    LANGUAGES = ['en', 'es', 'sw']
    MS_TRANSLATOR_KEY = '3fc118366ce54022a18dfc6886f9c1bc'  # os.environ.get('MS_TRANSLATOR_KEY')
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    POSTS_PER_PAGE = 10
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
