"""

"""

from pydantic import BaseModel
from datetime import datetime


class NotifyDto(BaseModel):
    threadNum: int


class HeartbeatDto(BaseModel):
    threadNum: int

