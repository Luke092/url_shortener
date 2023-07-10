from flask import Flask
from flask_cors import CORS

from route.url import UrlRouter


def main():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(UrlRouter, url_prefix='/api/url')
    app.run()


if __name__ == "__main__":
    main()
