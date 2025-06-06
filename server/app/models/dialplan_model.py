"""

"""

import enum
import uuid
from sqlalchemy import String, Integer, DateTime, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime
from app.utils.database.base import Base


class DialplanStatus(enum.Enum):
    Free = "free"
    During = "during"
    Finish = "finish"


class Dialplan(Base):
    __tablename__ = "dialplan"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), comment="id")
    phone: Mapped[str] = mapped_column(String(64), nullable=False, comment="手机号")
    status: Mapped[str] = mapped_column(SqlEnum(DialplanStatus, name="status"), nullable=False, default=DialplanStatus.Free, comment="状态")
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, comment="创建时间")
    update_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, comment="更新时间")