from datetime import datetime

from dao.database_connection import DatabaseConnection


class TokenDAO:
    def __init__(self, database_connection: DatabaseConnection):
        self.db_connection = database_connection

    def blacklist_token(self, token: str):
        cnx = self.db_connection.get_connection()
        cursor = cnx.cursor()
        query = "INSERT INTO blacklist (token, blacklisted_on) VALUES (%s, %s)"
        timestamp = datetime.now()
        values = (token, timestamp)
        cursor.execute(query, values)
        cnx.commit()
        cursor.close()

    def is_token_blacklisted(self, token: str) -> bool:
        cnx = self.db_connection.get_connection()
        cursor = cnx.cursor()
        query = "SELECT COUNT(*) FROM blacklist WHERE token = %s"
        values = (token,)
        cursor.execute(query, values)
        result = cursor.fetchone()[0]
        cursor.close()
        return result > 0
