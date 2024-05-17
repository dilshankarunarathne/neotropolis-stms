from pydantic import BaseModel


class Location(BaseModel):
    id: int
    dtp_token: str
    latitude: float
    longitude: float
    timestamp: str
