import pathlib
import sys

import pytest

from main import app

sys.path.append(str(pathlib.Path(__file__).parent))
from .client import TestClient


@pytest.fixture(scope='function')
async def client():
    async with TestClient(app=app, base_url="http://test", timeout=300) as ac:
        yield ac



