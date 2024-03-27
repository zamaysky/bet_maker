from asyncio import current_task

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import (
    AsyncSession,
    create_async_engine,
    async_sessionmaker,
    async_scoped_session,
)

from config import settings


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self._session_factory = async_sessionmaker(
            bind=create_async_engine(
                url=url,
                echo=echo,
                poolclass=NullPool,
            ),
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self._session_factory,
            scopefunc=current_task,
        )
        return session

    async def session_dependency(self) -> AsyncSession:
        async with self._session_factory() as session:
            yield session
            await session.close()

    async def scoped_session_dependency(self) -> AsyncSession:
        session = self.get_scoped_session()
        yield session
        await session.close()


db_helper = DatabaseHelper(
    url=settings.db_url_asyncpg,
    echo=False,
)
