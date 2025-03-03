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
    stage: Optional[str]: None # University, High School, Middle School, etc.
    institution_name: Optional[str] = None
    member_count: Optional[int] = None
    tap_members: Optional[list[uuid.UUID]] = None
    members_list: Optional[list[str]] = None
    leader: Optional[uuid.UUID] = None
    competition_id: uuid.UUID
    years: list[int]
    status: Optional[str] = None # "finalist", "derece", "etc"
    rank: Optional[int] = None
    relation: Optional[str] = None # central, related, friend, None
    intro_file_path: Optional[str] = None
    team_link: Optional[str] = None