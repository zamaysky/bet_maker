from pydantic import BaseModel

from schemas.event_status import EventStatus


class EventUpdate(BaseModel):
    status: EventStatus
