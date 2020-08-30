import os
class Config:
    '''
    General configuration settings
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SECRET_KEY="testkeyindevconfig"
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://elly:Access2020@localhost/YuBlog"

class ProdConfig(Config):
    '''
    Production Configurations
    '''
    SECRET_KEY="testkeyindevconfig"
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://elly:Access2020@localhost/YuBlog"

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