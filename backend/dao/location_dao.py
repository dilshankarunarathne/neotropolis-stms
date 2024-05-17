from dao.database_connection import DatabaseConnection
from models.location import Location


class LocationDAO:
    def __init__(self, database_connection: DatabaseConnection):
        self.db_connection = database_connection

    def save_location(self, location: Location):
        cnx = self.db_connection.get_connection()
        cursor = cnx.cursor()
        add_location = ("INSERT INTO locations "
                        "(dtp_token, latitude, longitude, timestamp) "
                        "VALUES (%s, %s, %s, CURRENT_TIMESTAMP)")
        data_location = (location.dtp_token, location.latitude, location.longitude)
        cursor.execute(add_location, data_location)
        cnx.commit()
        cursor.close()

    def get_location(self, dtp_token: str) -> Location:
        cnx = self.db_connection.get_connection()
        cursor = cnx.cursor()
        query = "SELECT * FROM locations WHERE dtp_token = %s ORDER BY timestamp DESC LIMIT 1"
        values = (dtp_token,)
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()
        if result is None:
            return None
        return Location(id=result[0], dtp_token=result[1], latitude=result[2], longitude=result[3], timestamp=result[4])
