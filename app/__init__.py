from flask import Flask, jsonify
from .routes import bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(bp)

    return app