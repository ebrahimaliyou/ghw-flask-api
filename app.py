import json
from flask import Flask, request
from api.routes.routes import routes



def create_app():
    app = Flask(__name__)
    app.register_blueprint(routes, url_prefix="/api")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
