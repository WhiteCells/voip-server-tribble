"""

"""

from pydantic import BaseModel
from datetime import datetime


class NotifyVo(BaseModel):
    clientId: str


class HeartbeatVo(BaseModel):
    timestamp: datetime

