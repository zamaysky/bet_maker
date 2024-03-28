import pathlib
import sys

import pytest
from httpx import ASGITransport

from main import app

sys.path.append(str(pathlib.Path(__file__).parent))
from .client import Client


@pytest.fixture
async def client():
    async with Client(
            transport=ASGITransport(app),
            base_url="http://test",
            timeout=300,
    ) as ac:
        yield ac
