from fastapi import Depends
from sqlalchemy import update
from sqlalchemy.ext.asyncio import AsyncSession

from database.db_helper import db_helper
from database.models import Bet
from schemas.bet_status import BetStatus
from schemas.event import EventUpdate
from schemas.event_status import EventStatus


class EventDAL:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def update_event(
            self,
            event_id: str,
            event_update: EventUpdate,
    ) -> None:
        await self._session.execute(
            update(Bet)
            .values(**{
                Bet.status.name: (
                    BetStatus.WIN
                    if event_update.status == EventStatus.WIN
                    else EventStatus.LOSE
                )
            })
            .where(
                Bet.event_id == event_id,
            )
        )
        await self._session.commit()


def event_dal_depends(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> EventDAL:
    return EventDAL(session)
