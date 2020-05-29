My Personal Portfolio-Website
    This project is part of my foundation project. I have used Flask and SQLAlchemy for it. The database is only for my personal login and it's purpose is to edit projects and skills directly inside the website without changing the code. I am currently hosting it via GCP on www.richard-kruemmel.de

How to set up this programm

    Prerequisite: Python3

    pip3 install -r requirements.txt

    Create config.py 

        import os
        basedir = os.path.abspath(os.path.dirname(__file__))


        class Config(object):
        SECRET_KEY = os.environ.get('SECRET_KEY') or ‘>insert secure hash<‘
        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'sqlite:///' + os.path.join(basedir, 'app.db')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        MAIL_SERVER = os.environ.get('MAIL_SERVER')
        MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
        MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
        MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
        MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
        ADMINS = [‘>insert your email adress<]


    Create DB

        pip install flask-migrate

        flask db init

        flask db migrate -m “databasetable”

        flask db upgrade

        Run python3

            >>>from app import db
            >>> from app.models import User
            >>> u = User(username=“admin”, email=“admin@example.com”)
            >>>u.set_password('mypassword')
            >>> db.session.add(u)
            >>> db.session.commit()

    Execute python portfolio.py

    Got to http://127.0.0.1:5000/login
        Enter your username and password and login
    Go to http://127.0.0.1:5000/about
        Add skill name and level (e.g. 70%) to your portfolio
