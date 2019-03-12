from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from config.config import create_app
from model.test import db

app = create_app()
migrate = Migrate(app, db)
app.config['DEBUG'] = True
manage = Manager(app=app)

# migrate
# db init        ->      初始化数据库
# db migrate     ->      创建迁移历史
# db upgrade     ->      更新数据库
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
