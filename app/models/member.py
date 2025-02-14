from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class Member(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow)
    updated_at: datetime = Field(default=datetime.utcnow)
    deleted_at: Optional[datetime] = None
    ar_name: str
    en_name: str
    membership_number: str
    email: str
    phone: str
    university: str
    major: str
    year: int
    sex: str
    birthdate: datetime
    country: str
    city: str
    district: str
    team_ids: list[uuid.UUID]
    status: str
    is_advisor: bool
    is_leader: bool
    skills: list[str]
    rating: int
    comments: list[uuid.UUID]