import os

class Config(object):
    UPLOAD_FOLDER = 'static/images'

    RECAPTCHA_PUBLIC_KEY = '6LeckacdAAAAAHSQu1A2h2ZXnXSrcoAFwIOvyi3d'
    RECAPTCHA_PRIVATE_KEY = '6LeckacdAAAAADOPi7qaBle16terydNyysELh9E1'
    
    SQLALCHEMY_DATABASE_URI = 'mysql://root:Nghiaoi123@localhost/qlloteria'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = 'SECRET_KEY'