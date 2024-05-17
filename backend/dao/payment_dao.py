from dao.database_connection import DatabaseConnection


class PaymentDAO:
    def __init__(self, database_connection: DatabaseConnection):
        self.db_connection = database_connection

    def save_payment(self, payment):
        cnx = self.db_connection.get_connection()
        cursor = cnx.cursor()
        add_payment = ("INSERT INTO payments "
                       "(amount, description, timestamp, dtp_token, u_id) "
                       "VALUES (%s, %s, CURRENT_TIMESTAMP, %s, %s)")
        data_payment = (payment.amount, payment.description, payment.dtp_token, payment.u_id)
        cursor.execute(add_payment, data_payment)
        cnx.commit()
        cursor.close()

    def remove_payment(self, id: int):
        cnx = self.db_connection.get_connection()
        cursor = cnx.cursor()
        delete_payment = ("DELETE FROM payments WHERE id = %s")
        cursor.execute(delete_payment, (id,))
        cnx.commit()
        cursor.close()
