from flask import Flask

def create_app():
    app = Flask(__name__g)
    app.config.from_pyfile('settings.py')
    return app


