from sqlalchemy.exc import SQLAlchemyError
from returns.maybe import Maybe
from config.base import session_factory
from model import Target
from returns.result import Success, Failure
from typing import List


def create_target_db(target: Target):
    try:
        with session_factory() as session:
            session.add(target)
            session.commit()
    except SQLAlchemyError as e:
        print("create_target failed", str(e))


def update_target_db(t_id: int, new_target: Target):
    try:
        with session_factory() as session:
            target =  find_target_by_id_db(t_id).map(session.merge).value_or(0)
            if target:
                target.target_priority = new_target.target_priority
                target.target_type_id = new_target.target_type_id
                target.city_id = new_target.city_id
                target.target_industry = new_target.target_industry
                target.target_id = new_target.target_id
            session.commit()
    except SQLAlchemyError as e:
        print("update_target failed", str(e))


def delete_target_db(t_id: int):
    try:
        with session_factory() as session:
            target = session.get(Target, t_id)
            if target:
                session.delete(target)
                session.commit()
                return Success(target)
            else:
                Failure(target)
    except SQLAlchemyError as e:
        print("delete_target failed", str(e))


def get_all_target_db() -> Maybe[List[Target]]:
    try:
        with session_factory() as session:
            return Maybe.from_optional(session.query(Target).all())
    except SQLAlchemyError as e:
        print("get_all_target failed", str(e))


def find_target_by_id_db(t_id: int) -> Maybe[Target]:
    with session_factory() as session:
        return Maybe.from_optional(session.get(Target, t_id))

# print(get_all_target())
# create_target(Target(target_id=1000000000, target_industry="dfds", city_id=4146, target_type_id=2936, target_priority=4))
# delete_target(3881)
# update_target(1000000000, Target(target_id=100000, target_industry="industry11", city_id=4146, target_type_id=2936, target_priority=4))
# print(find_target_by_id(100000))