from dao.token_dao import TokenDAO
from services.database_service import dao

token_dao = TokenDAO(dao)


def add_token_to_blacklist(token: str):
    token_dao.blacklist_token(token)


def check_if_token_is_blacklisted(token: str) -> bool:
    return token_dao.is_token_blacklisted(token)
