from datetime import datetime

from pydantic import BaseModel, Field, ConfigDict

from schemas.bet_status import BetStatus


class BetBase(BaseModel):
    event_id: str
    summa: float = Field(..., gt=0)


class BetCreation(BetBase):
    pass


class BetItem(BetBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    status: BetStatus
    created_at: datetime
    updated_at: datetime
