import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

# imported so we have access to app and db in this script
from app import app, db
# export APP_SETTINGS="config.DevelopmentConfig"

app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

# In order to run migrations from the command line
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()