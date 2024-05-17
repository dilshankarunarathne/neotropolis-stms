from dao.payment_dao import PaymentDAO
from models.payment_model import Payment
from services.database_service import dao

payment_dao = PaymentDAO(dao)


def add_payment(payment: Payment):
    payment_dao.save_payment(payment)


def remove_payment(p_id: int):
    return payment_dao.remove_payment(p_id)


def get_payment_history(dtp_token: str):
    return payment_dao.get_payment_history(dtp_token)
