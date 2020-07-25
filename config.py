import os
class Config:
    '''
    General configuration settings
    '''
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'

class ProdConfig(Config):
    '''
    Production Configurations
    '''
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI= os.environ.get('DATABASE_URL')

class DevConfig(Config):
    '''
    Development Configurations
    '''
    SECRET_KEY="testkeyindevconfig"
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://elly:Access2020@localhost/YuBlog"
    DEBUG = True

class TestConfig(Config):
    SECRET_KEY="testkeyintestconfig"
    SQLALCHEMY_DATABASE_URI="postgresql+psycopg2://elly:Access2020@localhost/YuBlog_test"

configurations = {
    "production":ProdConfig,
    "development":DevConfig,
    "testing":TestConfig
}