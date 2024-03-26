from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(AsyncAttrs, DeclarativeBase):
    pass


class B(Base):
    __tablename__ = "my_table"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str]


base = Base()