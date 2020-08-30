import os
class Config:
    '''
    General configuration settings
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY="testkeyindevconfig"
    SQLALCHEMY_DATABASE_URI="postgres://zdunvuehmeybxn:b9ed27414bc6ff6716a15b97e1c7b53d990b0c2ffc6b37e50eee8fe92dd52fe1@ec2-54-86-57-171.compute-1.amazonaws.com:5432/dba2q06slbp382"

class ProdConfig(Config):
    '''
    Production Configurations
    '''
    SECRET_KEY="testkeyindevconfig"
    SQLALCHEMY_DATABASE_URI=""

class DevConfig(Config):
    '''
    Development Configurations
    '''
    SECRET_KEY="testkeyindevconfig"
    SQLALCHEMY_DATABASE_URI=""
    DEBUG = True

class TestConfig(Config):
    SECRET_KEY="testkeyintestconfig"
    SQLALCHEMY_DATABASE_URI=""

configurations = {
    "production":ProdConfig,
    "development":DevConfig,
    "testing":TestConfig
}