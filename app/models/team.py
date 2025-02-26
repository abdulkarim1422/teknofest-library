from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class Team(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default=uuid.uuid4, primary_key=True)
    name: str
    created_at: datetime = Field(default=datetime.utcnow)
    updated_at: datetime = Field(default=datetime.utcnow)
    deleted_at: Optional[datetime] = None
    description: str
    stage: str # University, High School, Middle School, etc.
    member_count: int
    members: list[uuid.UUID]
    leader: uuid.UUID
    competition_id: uuid.UUID
    years: list[int]
    status: str
    rank: int
    relation: str # central, related, friend, none