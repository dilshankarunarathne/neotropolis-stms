from dao.location_dao import LocationDAO
from models.location import Location
from services.database_service import dao

location_dao = LocationDAO(dao)


def add_location(location: Location):
    location_dao.save_location(location)


def get_location(dtp_token: str) -> Location:
    return location_dao.get_location(dtp_token)
