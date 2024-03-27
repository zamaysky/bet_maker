import datetime

from sqlalchemy import Enum, DateTime, func
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.dialects import postgresql

from .base import Base
from schemas.bet_status import BetStatus


class Bet(Base):
    event_id: Mapped[str] = mapped_column(
        postgresql.VARCHAR(64),
        nullable=False
    )
    summa: Mapped[float] = mapped_column(
        postgresql.NUMERIC(10, 2),
        nullable=False,
    )
    status: Mapped[BetStatus] = mapped_column(
        Enum(BetStatus),
        nullable=False,
        default=BetStatus.NOT_PLAYED,
    )
    created_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(), nullable=False
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
        default=datetime.datetime.now(datetime.timezone.utc),
        server_default=func.now(),
        onupdate=datetime.datetime.now(datetime.timezone.utc),
        nullable=False
    )

