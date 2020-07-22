from . import db
from flask_sqlalchemy import SQLAlchemy

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    article = db.relationship('Article',backref='user',lazy = 'dynamic')
    comments = db.relationship('Comment',backref='user',lazy='dynamic')


class Article(db.Model):
    '''
    This class will contain the database schema for articles table
    '''
    __tablename__ = 'articles'

    id = db.Column(db.Integer,primary_key = True)
    article = db.Column(db.String)
    category = db.Column(db.String)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))

class Comment(db.Model):
    '''
    This class will contain the schema for comments
    '''
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    article_id = db.Column(db.Integer,db.ForeignKey('articles.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))


class Quotes:
    def __init__(self,author,quote):
        '''
        Method to instanciate the quotes class
        '''
        self.author = author
        self.quote = quote

    