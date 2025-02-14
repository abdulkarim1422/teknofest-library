from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class Resource(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow)
    updated_at: datetime = Field(default=datetime.utcnow)
    deleted_at: Optional[datetime] = None
    competition_id: uuid.UUID # The competition that the resource is related to
    team_id: uuid.UUID # The team that created the resource
    resource_type: str # GitHub, Youtube, Google Drive, etc.
    resource_url: str
    description: str
    year: int # The year that the resource is created
    comments: list[uuid.UUID]