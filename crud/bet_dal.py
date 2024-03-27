from fastapi import Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database.db_helper import db_helper
from database.models import Bet
from schemas.bet import BetCreation
from schemas.bet_status import BetStatus
from schemas.pagination import Pagination


class BetDAL:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def create_bet(self, bet_creation: BetCreation) -> Bet:
        bet = Bet(**bet_creation.model_dump())
        self._session.add(bet)
        await self._session.commit()
        return bet

    async def get_bets(
            self,
            bet_status: BetStatus | None = None,
            pagination: Pagination | None = None,
            event_id: str | None = None,
    ) -> list[Bet]:
        query = select(Bet).order_by(Bet.id)
        if event_id:
            query = query.where(Bet.event_id == event_id)
        if bet_status:
            query = query.where(Bet.status == bet_status)
        if pagination:
            query = query.limit(pagination.limit).offset(pagination.offset)
        return [*(await self._session.execute(query)).scalars().all()]


def bet_dal_depends(
        session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> BetDAL:
    return BetDAL(session)
