from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from models.location import Location
from services.location_service import add_location, get_location

router = APIRouter(
    prefix="/api/location",
    tags=["location"],
    responses={404: {"description": "The requested uri was not found"}},
)


@router.post("/add_location")
async def add_location_route(
        dtp_token: str = Form(...),
        latitude: float = Form(...),
        longitude: float = Form(...),
        token: str = Depends(oauth2_scheme)
):
    """
    The endpoint for adding a new location

    Returns:
        (Location) The location that was added

    Raises:
        HTTPException: if the user is not authorized

    :param token:
    :param dtp_token:
    :param latitude:
    :param longitude:

    """
    if await get_current_user(token) is None:
        raise credentials_exception

    location = Location(
        dtp_token=dtp_token,
        latitude=latitude,
        longitude=longitude
    )

    add_location(location)

    return {"location": location}
