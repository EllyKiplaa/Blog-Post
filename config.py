import os

class Config:

    
    # MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = '707569981'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elly:Access2020@localhost/YuBlog'


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}