from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from flask_marshmallow import Marshmallow
from flask_cors import CORS


app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)
migrate = Migrate(app, db)

ma = Marshmallow(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('runserver',Server(host="0.0.0.0",port=5000,use_debugger=None))

cors = CORS(app, resource={r"/*":{"origins":"*"}})


from controllers.views import *


if __name__ == "__main__":
    app.run()