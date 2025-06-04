"""

"""

import enum
from typing import TYPE_CHECKING
from sqlalchemy import String, Integer, DateTime, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.utils.database.base import Base

if TYPE_CHECKING:
    from .acc_model import Acc

class ClientStatus(enum.Enum):
    Online: str = "online"
    Offline: str = "offline"

class Client(Base):
    __tablename__ = "client"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, comment="")
    name: Mapped[str] =  mapped_column(String(64), nullable=False, comment="")
    status: Mapped[str] = mapped_column(SqlEnum(ClientStatus, name="status"), nullable=False, default=ClientStatus.Offline, comment="")
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, comment="")
    update_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, comment="")

    accounts: Mapped[list["Acc"]] = relationship("Acc", back_populates="client", cascade="all, delete-orphan")
