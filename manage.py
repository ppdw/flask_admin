from flask_script import Manager

from config.config import create_app

app = create_app()
app.config['DEBUG'] = True
manage = Manager(app=app)

if __name__ == '__main__':
    manage.run()