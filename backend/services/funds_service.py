from dao.funds_dao import FundsDAO
from services.database_service import dao

funds_dao = FundsDAO(dao)


def add_funds(amount: float, dtp_token):
    """
    The endpoint for adding funds to the account

    Returns:
        (float) The amount of funds that were added

    Raises:
        HTTPException: if the user is not authorized

    :param dtp_token:
    :param amount:

    """
    funds_dao.insert_funds(amount, dtp_token)

    return {"avail amount": amount}
