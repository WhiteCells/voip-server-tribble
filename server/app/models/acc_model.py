"""

"""

import enum
import uuid
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

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), comment="id")
    name: Mapped[str] =  mapped_column(String(64), nullable=False, comment="sip name")
    pwd: Mapped[str] = mapped_column(String(64), nullable=False, comment="sip pwd")
    host: Mapped[str] = mapped_column(String(64), nullable=False, comment="sip host")
    status: Mapped[str] = mapped_column(SqlEnum(AccStatus, name="status"), nullable=False, default=AccStatus.Offline, comment="状态")
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, comment="创建时间")
    update_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, comment="更新时间")
    register_at: Mapped[datetime] = mapped_column(DateTime, nullable=True, comment="注册时间")
    last_register_at: Mapped[datetime] = mapped_column(DateTime, nullable=True, comment="上次注册时间")

    client_id: Mapped[str] = mapped_column(ForeignKey("client.id", ondelete="CASCADE"), nullable=True)
    client: Mapped["Client"] = relationship("Client", back_populates="accounts")
