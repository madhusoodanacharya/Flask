from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'h23432vv434b5465cxvmzhgfsdg674354385'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app
