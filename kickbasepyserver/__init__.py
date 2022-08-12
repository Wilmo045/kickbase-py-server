import os
from .containers import Container

from flask import Flask



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'kickbasepyserver.sqlite'),
    )

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
    from . import auth
    app.register_blueprint(auth.bp)

    # register blueprint blog
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    # register blueprint kickbase
    from . import kickbase
    app.register_blueprint(kickbase.bp)


    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    return app