import asyncio
import uuid

import pytest

from client import TestClient
from schemas.bet import BetCreation, BetItem
from schemas.bet_status import BetStatus
from schemas.event import EventUpdate
from schemas.event_status import EventStatus


@pytest.mark.parametrize(
    'bet_creation',
    [
        BetCreation(
            event_id='sdfaads',
            summa=1344,
        )
    ]
)
async def test_bet_creation(client: TestClient, bet_creation: BetCreation):
    bet: BetItem = await client.create_bet(
        bet_creation=bet_creation
    )
    assert bet.status == BetStatus.NOT_PLAYED
    assert all(
        getattr(bet, field) == getattr(bet_creation, field)
        for field in ('summa', 'event_id')
    )


@pytest.mark.parametrize(
    ('event_id', 'expected_count'),
    [
        (uuid.uuid4().hex, 14),
        (uuid.uuid4().hex, 25),
    ]
)
async def test_get_bets(client: TestClient, event_id: str, expected_count: int) -> None:
    for _ in range(expected_count):
        await client.create_bet(
            bet_creation=BetCreation(
                event_id=event_id,
                summa=134,
            )
        )
    bets: list[BetItem] = await client.get_bets(
        params={
            'event_id': event_id,
            'limit': expected_count,
            'status': BetStatus.NOT_PLAYED.value,
        }
    )
    assert len(bets) == expected_count


@pytest.mark.parametrize(
    ('event_id', 'expected_count'),
    [
        (uuid.uuid4().hex, 3),
        (uuid.uuid4().hex, 5),
    ]
)
async def test_update_event(
        client: TestClient,
        event_id: str,
        expected_count: int,
) -> None:
    for _ in range(expected_count):
        await client.create_bet(
            bet_creation=BetCreation(
                event_id=event_id,
                summa=134,
            )
        )
    await client.update_event(
        event_id=event_id,
        event_update=EventUpdate(status=EventStatus.WIN)
    )
    bets: list[BetItem] = await client.get_bets(
        params={
            'event_id': event_id,
            'status': BetStatus.WIN.value,
        }
    )
    assert len(bets) == expected_count
    await client.update_event(
        event_id=event_id,
        event_update=EventUpdate(status=EventStatus.LOSE)
    )
    bets: list[BetItem] = await client.get_bets(
        params={
            'event_id': event_id,
            'status': BetStatus.LOSE.value,
        }
    )
    assert len(bets) == expected_count
