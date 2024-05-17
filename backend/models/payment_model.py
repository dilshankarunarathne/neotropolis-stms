from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Payment(BaseModel):
    id: Optional[int] = None
    amount: float
    description: str
    timestamp: Optional[datetime] = None
    dtp_token: str
    u_id: int
