"""

"""

import uuid
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from app.utils.database.base import Base

class TaskModel(Base):
    __tablename__ = "task"

    id: Mapped[str] = mapped_column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()), comment="id")
