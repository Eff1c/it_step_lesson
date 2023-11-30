from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from config import Config
from models import Base


db = SQLAlchemy(model_class=Base)

ma = Marshmallow()


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    ma.init_app(app)

    from blueprints import main_blueprint
    app.register_blueprint(main_blueprint)

    return app
