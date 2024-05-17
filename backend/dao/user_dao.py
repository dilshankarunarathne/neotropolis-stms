from datetime import datetime

import mysql.connector

from dao.database_connection import DatabaseConnection
from models.user_model import User, UserInDB


class UserDAO:
    def __init__(self, database_connection: DatabaseConnection):
        self.db_connection = database_connection

    def create_user(self, user: User):
        cnx = self.db_connection.get_connection()
        cursor = cnx.cursor()
        add_user = ("INSERT INTO users "
                    "(id, username, email, is_admin, hashed_password, mobile, "
                    "first_name	, last_name, dtp_token) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)")
        data_user = (user.id, user.username, user.email, user.is_admin, user.hashed_password,
                     user.mobile, user.first_name, user.last_name, user.dtp_token)
        cursor.execute(add_user, data_user)
        cnx.commit()
        cursor.close()

    def get_user_by_username(self, username: str) -> UserInDB | None:
        cnx = self.db_connection.get_connection()
        cursor = cnx.cursor()
        query = ("SELECT * "
                 "FROM users "
                 "WHERE username = %s")
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        cursor.close()
        if row is None:
            return None
        return UserInDB(**dict(
            zip(['id', 'username', 'email', 'is_admin', 'hashed_password', 'mobile', 'fist_name', 'last_name',
                 'dtp_token'], row)))

    def get_last_user_id(self) -> int:
        cnx = self.db_connection.get_connection()
        cursor = cnx.cursor()
        query = "SELECT MAX(id) FROM users"
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        if row is None:
            return 0
        return row[0]

    def blacklist_token(self, token: str):
        """
        Add a token to the blacklist table with the current timestamp
        """
        try:
            cnx = self.db_connection.get_connection()
            cursor = cnx.cursor()
            query = "INSERT INTO blacklist (token, blacklisted_on) VALUES (%s, %s)"
            timestamp = datetime.now()
            values = (token, timestamp)
            cursor.execute(query, values)
            cnx.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print(err)

    def is_token_blacklisted(self, token: str) -> bool:
        """
        Check if a token exists in the blacklist table
        """
        try:
            cnx = self.db_connection.get_connection()
            cursor = cnx.cursor()
            query = "SELECT COUNT(*) FROM blacklist WHERE token = %s"
            values = (token,)
            cursor.execute(query, values)
            result = cursor.fetchone()[0]
            cursor.close()
            return result > 0
        except mysql.connector.Error as err:
            print(err)
            return False
