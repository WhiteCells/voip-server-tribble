"""

"""

import enum
from sqlalchemy import String, Integer, DateTime, Enum as SqlEnum
from sqlalchemy.orm import Mapped,  mapped_column
from datetime import datetime
from app.utils.database.base import Base


class DialplanStatus(enum.Enum):
    Free = "free"
    During = "during"
    Finish = "finish"


class Dialplan(Base):
    __tablename__ = "dialplan"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    phone: Mapped[str] = mapped_column(String(64), nullable=False, comment="")
    status: Mapped[str] = mapped_column(SqlEnum(DialplanStatus, name="status"), nullable=False, default=DialplanStatus.Free, comment="")
    create_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.now, comment="")
