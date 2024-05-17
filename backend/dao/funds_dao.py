from dao.database_connection import DatabaseConnection


class FundsDAO:
    def __init__(self, database_connection: DatabaseConnection):
        self.db_connection = database_connection

    def insert_funds(self, amount: float, dtp_token: str) -> float:
        cnx = self.db_connection.get_connection()
        cursor = cnx.cursor()
        add_funds = ("INSERT INTO funds "
                     "(amount, dtp_token, timestamp) "
                     "VALUES (%s, %s, CURRENT_TIMESTAMP)")
        data_funds = (amount, dtp_token)
        cursor.execute(add_funds, data_funds)
        cnx.commit()
        cursor.close()
        return amount
