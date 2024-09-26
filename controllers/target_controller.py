from flask import Flask, Blueprint, jsonify, request

from model import Target
from service.target_service import convert_to_json, delete_target, update_target, create_target

from service.target_service import get_target_by_id, get_all_targets



app = Flask(__name__)

target_blue_print =Blueprint('targets', __name__)


@target_blue_print.route('/<int:t_id>', methods=['GET'])
def get_target_by_id_route(t_id: int):
    return (get_target_by_id(t_id)
    .map(convert_to_json)
    .map(lambda t: (jsonify(t), 200))
    .value_or((jsonify({}), 404)))


@target_blue_print.route('/', methods=['GET'])
def get_all_targets_route():
        return (get_all_targets()
                .map(lambda targets: [convert_to_json(target) for target in targets])
                .map(lambda t: (jsonify(t), 200))
                .value_or((jsonify({}), 404)))


@target_blue_print.route('/<int:t_id>', methods=['DELETE'])
def delete_target_route(t_id: int):
    result = delete_target(t_id)
    return jsonify(result), 200

@target_blue_print.route('/<int:t_id>', methods=['PUT'])
def update_target_route(t_id: int):
    target_json = request.json
    target = Target(target_id= target_json.get("target_id"), target_industry=target_json.get("target_industry"),
                    city_id=target_json.get("city_id"), target_type_id=target_json.get("target_type_id"),
                    target_priority=target_json.get("target_priority") )
    result = update_target(t_id, target)
    return jsonify(result), 200


@target_blue_print.route('/', methods=['POST'])
def create_target_route():
    target_json = request.json
    target = Target(target_id=target_json.get("target_id"), target_industry=target_json.get("target_industry"),
                    city_id=target_json.get("city_id"), target_type_id=target_json.get("target_type_id"),
                    target_priority=target_json.get("target_priority"))
    result = create_target(target)
    return jsonify(result), 200
