"""

"""

import enum
import uuid
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

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), comment="id")
    name: Mapped[str] =  mapped_column(String(64), nullable=False, comment="名称")
    thread_num: Mapped[int] = mapped_column(Integer, nullable=False, comment="线程数")
    status: Mapped[str] = mapped_column(SqlEnum(ClientStatus, name="status"), nullable=False, default=ClientStatus.Offline, comment="状态")
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, comment="创建时间")
    update_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, comment="更新时间")
    online_at: Mapped[datetime] = mapped_column(DateTime, nullable=True, comment="上线时间")
    last_online_at: Mapped[datetime] = mapped_column(DateTime, nullable=True, comment="上次上线时间")

    accounts: Mapped[list["Acc"]] = relationship("Acc", back_populates="client", cascade="all, delete-orphan")
