from flask import Flask
from flask.ext.moment import Moment


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('envvar.py')


# Extension initialization
moment = Moment(app)


# Import views at the end
from app import views
















