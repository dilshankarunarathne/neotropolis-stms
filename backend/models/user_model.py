from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str | None = None
    email: str | None = None
    is_admin: bool | None = None
    mobile: str | None = None
    first_name: str | None = None
    last_name: str | None = None
    dtp_token: str | None = None


class UserInDB(User):
    hashed_password: str
