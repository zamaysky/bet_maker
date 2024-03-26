from typing import Annotated

from fastapi import APIRouter, Body, Depends


router = APIRouter(
    prefix=r'/v1/bets',
    tags=['bets']
)





