from httpx import AsyncClient
from pydantic import TypeAdapter
from starlette import status

from schemas.bet import BetItem, BetCreation
from schemas.event import EventUpdate


class TestClient(AsyncClient):
    async def get_bets(self, params: dict | None = None) -> list[BetItem]:
        params = params or {}
        response = await self.get(
            r'bets/',
            params=params
        )
        assert response.status_code == status.HTTP_200_OK
        return TypeAdapter(list[BetItem]).validate_json(response.text)

    async def create_bet(self, bet_creation: BetCreation) -> BetItem:
        response = await self.post(
            r'bets/',
            json=bet_creation.model_dump()
        )
        assert response.status_code == status.HTTP_201_CREATED
        return BetItem.model_validate_json(response.text)

    async def update_event(self, event_id: str, event_update: EventUpdate) -> None:
        response = await self.put(
            rf'events/{event_id}',
            json=event_update.model_dump(),
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT
