"""

"""

import enum
from typing import TYPE_CHECKING
from sqlalchemy import String, Integer, DateTime, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship
from datetime import datetime
from app.utils.database.base import Base

if TYPE_CHECKING:
    from .client_model import Client

class AccStatus(enum.Enum):
    Online: str = "online"
    Offline: str = "offline"

class Acc(Base):
    __tablename__ = "acc"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, comment="")
    name: Mapped[str] =  mapped_column(String(64), nullable=False, comment="")
    pwd: Mapped[str] = mapped_column(String(64), nullable=False, comment="")
    host: Mapped[str] = mapped_column(String(64), nullable=False, comment="")
    status: Mapped[str] = mapped_column(SqlEnum(AccStatus, name="status"), nullable=False, default=AccStatus.Offline, comment="")
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, comment="")
    update_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, comment="")

    client_id: Mapped[int] = mapped_column(ForeignKey("client.id", ondelete="CASCADE"), nullable=False)
    client: Mapped["Client"] = relationship("Client", back_populates="accounts")
