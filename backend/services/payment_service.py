from dao.payment_dao import PaymentDAO
from models.payment_model import Payment
from services.database_service import dao

# Create a PaymentDAO instance
payment_dao = PaymentDAO(dao)


def add_payment(payment: Payment):
    payment_dao.save_payment(payment)


def remove_payment(id: int):
    payment_dao.remove_payment(id)
