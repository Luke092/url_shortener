from flask import Blueprint, request, jsonify

from controller.url import UrlController

UrlRouter = Blueprint('url_controller', __name__)


@UrlRouter.route('/<url>')
def get(url):
    res = UrlController().get_by_code(url)
    return jsonify(res)


@UrlRouter.route('/', methods=['POST'])
def addUrl():
    body = request.get_json()
    res = UrlController().add(body['url'])
    return jsonify(res)
