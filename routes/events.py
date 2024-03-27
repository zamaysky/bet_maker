from fastapi import APIRouter, Depends
from starlette import status

from crud.event_dal import EventDAL, event_dal_depends
from schemas.event import EventUpdate

router = APIRouter(
    prefix=r'/events',
    tags=['bets']
)


@router.put(
    r'/{event_id}',
    status_code=status.HTTP_204_NO_CONTENT
)
async def update_event(
        event_update: EventUpdate,
        event_id: str,
        event_dal: EventDAL = Depends(event_dal_depends)
):
    await event_dal.update_event(
        event_id=event_id,
        event_update=event_update,
    )
