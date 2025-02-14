from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class Member(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow)
    updated_at: datetime = Field(default=datetime.utcnow)
    deleted_at: Optional[datetime] = None
    name: str
    membership_number: str
    email: str
    phone: str
    university: str
    major: str
    year: int
    team_ids: list[uuid.UUID]
    status: str
    is_advisor: bool
    skills: list[str]
    rating: int
    comments: list[uuid.UUID]