import os
from .containers import Container

from flask import Flask
from flask_cors import CORS

import locale
locale.setlocale(locale.LC_ALL, 'de_DE.utf8')
def decimalpoint(value):
    """Applies thousands separator to integer."""
    return '{:n}'.format(int(value))


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        CACHE_TYPE='SimpleCache',  # Flask-Caching related configs
        CACHE_DEFAULT_TIMEOUT= 300, # Flask-Caching related configs
        DATABASE=os.path.join(app.instance_path, 'kickbasepyserver.sqlite'),
    )

    app.jinja_env.filters['decimalpoint'] = decimalpoint

    # create Dependency Injection Container
    container = Container()
    app.container = container

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # register with database
    from . import db
    db.init_app(app)

    # register blueprint auth
    from .user import auth
    app.register_blueprint(auth.bp)

    # register blueprint league
    from .league import league
    app.register_blueprint(league.bp)

     # register blueprint league
    from .gift import gift
    app.register_blueprint(gift.bp)

     # CORS
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    return app

   