import asyncio
from contextlib import asynccontextmanager

from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from config import settings


engine = create_async_engine(
    url=settings.db_url_asyncpg,
    echo=False,
)
session_factory = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


@asynccontextmanager
async def get_session() -> AsyncSession:
    session = session_factory()
    yield session
    if session is not None:
        await session.close()


async def main():
    async with get_session() as session:
        res = await session.execute(
            text('create table my table (id INTEGER PRIMARY KEY')
        )
        print(res.scalars().all())


if __name__ == '__main__':
    asyncio.run(main())
