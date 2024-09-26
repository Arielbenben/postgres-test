from sqlalchemy import inspect
import repository.target_repository as t
from model import Target
from typing import Dict


def get_all_targets():
    return t.get_all_target_db()

def get_target_by_id(t_id: int):
    return t.find_target_by_id_db(t_id)

def create_target(target: Target):
    return t.create_target_db(target)

def update_target(t_id: int, target: Target):
    return t.update_target_db(t_id, target)

def delete_target(t_id: int):
    return t.delete_target_db(t_id)

def convert_to_json(target: Target) -> Dict[str, str]:
    return {c.key: getattr(target, c.key) for c in inspect(target).mapper.column_attrs}
