from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Location(BaseModel):
    id: Optional[int] = None
    dtp_token: str
    latitude: float
    longitude: float
    timestamp: Optional[datetime] = None
