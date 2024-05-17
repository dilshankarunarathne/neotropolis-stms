from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class Fund(BaseModel):
    id: Optional[int] = None
    dtp_token: str
    amount: float
    timestamp: Optional[datetime] = None
