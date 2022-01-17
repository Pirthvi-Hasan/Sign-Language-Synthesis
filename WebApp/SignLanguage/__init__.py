from flask import Flask
from flask.helpers import url_for

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'thisisasecret'

    from .views import views
    from .detect import detect
    app.register_blueprint(views,url_prefix="/")
    app.register_blueprint(detect,url_prefix='/')

    return app

