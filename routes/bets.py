from typing import Annotated

from fastapi import APIRouter, Body, Depends
from starlette import status

from crud.bet_dal import BetDAL, bet_dal_depends
from schemas.bet import BetItem, BetCreation
from schemas.bet_status import BetStatus
from schemas.pagination import Pagination

router = APIRouter(
    prefix=r'/bets',
    tags=['bets']
)


@router.post(
    r'/',
    response_model=BetItem,
    status_code=status.HTTP_201_CREATED,
)
async def create_bet(
        bet_creation: BetCreation = Body(),
        bet_dal: BetDAL = Depends(bet_dal_depends),
):
    return await bet_dal.create_bet(bet_creation)


@router.get(
    r'/',
    response_model=list[BetItem]
)
async def get_bets(
        bet_dal: Annotated[BetDAL, Depends(bet_dal_depends)],
        pagination: Annotated[Pagination, Depends()],
        bet_status: BetStatus = None,
        event_id: str | None = None,
):
    return await bet_dal.get_bets(
        bet_status=bet_status,
        pagination=pagination,
        event_id=event_id,
    )
