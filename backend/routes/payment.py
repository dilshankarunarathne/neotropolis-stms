from fastapi import APIRouter, Depends, Form

from auth.authorize import oauth2_scheme, get_current_user, credentials_exception
from models.payment_model import Payment
from services.payment_service import add_payment, remove_payment

router = APIRouter(
    prefix="/api/payment",
    tags=["payment"],
    responses={404: {"description": "The requested uri was not found"}},
)


@router.post("/add_payment")
async def add_payment_route(
        amount: float = Form(...),
        description: str = Form(...),
        dtp_token: str = Form(...),
        token: str = Depends(oauth2_scheme)
):
    user = await get_current_user(token)
    if user is None:
        raise credentials_exception

    payment = Payment(
        amount=amount,
        description=description,
        dtp_token=dtp_token,
        u_id=user.id)

    add_payment(payment)

    return {"payment successful": amount, "description": description}


@router.delete("/remove_payment")
async def remove_payment_route(
        p_id: int = Form(...),
        token: str = Depends(oauth2_scheme)
):
    if await get_current_user(token) is None:
        raise credentials_exception

    # TODO: check if the user is an admin

    remove_payment(p_id)

    return {"deleted payment": id}
