from dao.user_dao import UserDAO
from models.user_model import User
from services import database_service

user_dao = UserDAO(database_service.dao)


def add_new_user(user: User):
    user_dao.create_user(user)


def user_exists(username: str) -> bool:
    if get_user(username) is None:
        return False
    return True


def get_next_avail_id() -> int:
    last_id = user_dao.get_last_user_id()
    if last_id is None:
        return 1
    return last_id + 1


def get_user(username: str):
    return user_dao.get_user_by_username(username)
