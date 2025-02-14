from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class Competition(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow)
    updated_at: datetime = Field(default=datetime.utcnow)
    deleted_at: Optional[datetime] = None
    number: int
    tr_name: str
    en_name: str
    ar_name: str
    tr_description: str
    en_description: str
    ar_description: str
    years: list[int]
    min_member: int
    max_member: int
