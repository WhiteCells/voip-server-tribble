"""

"""

from app.utils.database.base import Base
from app.utils.database.session import engine


async def init_models():
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.create_all)
    pass


async def startups():
    await init_models()