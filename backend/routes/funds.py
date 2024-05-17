from fastapi import APIRouter, Form, Depends

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from services.funds_service import add_funds

router = APIRouter(
    prefix="/api/funds",
    tags=["funds"],
    responses={404: {"description": "The requested uri was not found"}},
)


@router.post("/add_funds")
async def add_funds_route(
        amount: float = Form(...),
        dtp_token: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    """
    The endpoint for adding funds to the account

    Returns:
        (float) The amount of funds that were added

    Raises:
        HTTPException: if the user is not authorized

    :param dtp_token:
    :param token:
    :param amount:

    """
    if await get_current_user(token) is None:
        raise credentials_exception

    add_funds(amount, dtp_token)

    return {"amount": amount}
