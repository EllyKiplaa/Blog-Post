from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Article,Comment,Quotes



# Creating app instance
app = create_app('production')
from app.models import User

manager = Manager(app)


manager.add_command('server',Server)

@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover("tests")
    unittest.TextTestRunner(verbosity=5).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Article = Article, Comment = Comment, Quotes = Quotes )
if __name__ == '__main__':
    manager.run()