from flask import Blueprint, request, jsonify, make_response

from controller.url import UrlController

UrlRouter = Blueprint('url_controller', __name__)


@UrlRouter.route('/<url>')
def get(url):
    res = UrlController().get_by_code(url)
    if res["status"] > 300:
        return make_response("", res["status"])

    return jsonify(res["body"])


@UrlRouter.route('/', methods=['POST'])
def addUrl():
    body = request.get_json()
    res = UrlController().add(body['url'])
    if res["status"] > 300:
        return make_response("", res["status"])

    return jsonify(res["body"])
