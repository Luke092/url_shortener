from flask import Flask

from route.url import UrlRouter


def main():
    app = Flask(__name__)
    app.register_blueprint(UrlRouter, url_prefix='/api/url')
    app.run()


if __name__ == "__main__":
    main()
