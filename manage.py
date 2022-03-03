from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.models import db
from app import app

# import models
from app.models.user import User


# register app and db with migration class
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
