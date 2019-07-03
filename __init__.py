from routes.home import home
from flask_wtf.csrf import CSRFProtect
from flask_mongoengine import MongoEngine
from models.user import User
from flask_login import LoginManager
from flask_toastr import Toastr

from routes.auth import auth
from routes.admin.admin import admin
from routes.admin.post import admin_post
from routes.admin.catalog import admin_catalog
from routes.admin.product import admin_product
# insert_route


from logging.handlers import RotatingFileHandler
import logging
import os




def register_auth(app):
    login_manager = LoginManager(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.objects(id=user_id).first()


def register_feature(app):
    CSRFProtect(app)
    MongoEngine(app)
    toastr = Toastr(app)


def register_blueprints(app):
    app.register_blueprint(home)
    app.register_blueprint(auth)
    app.register_blueprint(admin)
    app.register_blueprint(admin_post)
    app.register_blueprint(admin_catalog)
    app.register_blueprint(admin_product)
#     insert_blueprint


def register_logging(app):
    path = app.config['LOGGING_PATH']
    os.makedirs(path, exist_ok=True)

    info_fh = RotatingFileHandler(os.path.join(path, 'info.log'), maxBytes=10000000, backupCount=3)
    info_fh.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))
    info_fh.setLevel(logging.INFO)
    app.logger.addHandler(info_fh)

    warning_fh = RotatingFileHandler(os.path.join(path, 'errors.log'), maxBytes=10000000, backupCount=3)
    warning_fh.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s '
        '[in %(pathname)s:%(lineno)d]'
    ))

    warning_fh.setLevel(logging.ERROR)
    app.logger.addHandler(warning_fh)


def create_dummy_data():
    from dump.dummy import dump_post
    dump_post()

def create_app(app):
    app.config.from_object('config.BaseConfig')
    register_blueprints(app)
    register_feature(app)
    register_auth(app)
    register_logging(app)
    #create_dummy_data()
    return app
