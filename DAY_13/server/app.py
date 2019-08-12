import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_bootstrap import Bootstrap

main_directory = os.path.abspath(os.path.dirname(__file__))

app_connexion = connexion.App(__name__, specification_dir=main_directory)

app = app_connexion.app
Bootstrap(app)

# database path
sqlite_path = "sqlite:///" + os.path.join(main_directory, "music_store.db")

# Configure the SqlAlchemy part of the app instance
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = sqlite_path
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# sql alchemy orm to communicate with sqlite db
db = SQLAlchemy(app)

# marshmallow init
ma = Marshmallow(app)
