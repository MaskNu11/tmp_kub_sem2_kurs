import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
import logging
import asyncio
from sqlalchemy import select
from db.models import Base, User
from db.orm_quary import orm_add_user, urm_quared_get_user_all
import json


logging.basicConfig(
    level=logging.INFO,
)

engine = create_async_engine(f"postgresql+asyncpg://{'postgres'}:{'2486'}@{'localhost'}:{'5432'}/{'postgres'}", echo=True)


SESSION_MAKER = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)



# async def drop_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.drop_all)
async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    # async with session_maker() as session:
    #     data['session'] = session




# async with session_maker() as session:
# 	query = select(Category)
# 	result = await session.execute(query)
# 	for i in result:
# 		print(i.id)
#theatre