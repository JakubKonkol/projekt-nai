from flask import Blueprint, jsonify

summarize_blueprint = Blueprint('summarize', __name__, url_prefix='/api')


@summarize_blueprint.route('/summarize', methods=['GET'])
def summarize():
    response_data = {"result": "this is a test"}
    return jsonify(response_data)
