from dao.location_dao import LocationDAO
from dao.database_connection import DatabaseConnection
from config import config
from models.location import Location

database_connection = DatabaseConnection(
    host=config.get("database", "database.host"),
    user=config.get("database", "database.user"),
    password=config.get("database", "database.password"),
    database=config.get("database", "database.dbname")
)

location_dao = LocationDAO(database_connection)


def add_location(location: Location):
    location_dao.save_location(location)


def get_location(dtp_token: str) -> Location:
    return location_dao.get_location(dtp_token)
