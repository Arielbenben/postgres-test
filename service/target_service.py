from sqlalchemy import inspect
import repository.target_repository as t
from model import Target
from typing import Dict

from repository.target_repository import get_all_target_db, find_target_by_id_db, update_target_db, create_target_db, \
    delete_target_db


def get_all_targets():
    return get_all_target_db()

def get_target_by_id(t_id: int):
    return find_target_by_id_db(t_id)

def create_target(target: Target):
    return create_target_db(target)

def update_target(t_id: int, target: Target):
    return update_target_db(t_id, target)

def delete_target(t_id: int):
    return delete_target_db(t_id)

def convert_to_json(target: Target) -> Dict[str, str]:
    return {c.key: getattr(target, c.key) for c in inspect(target).mapper.column_attrs}
