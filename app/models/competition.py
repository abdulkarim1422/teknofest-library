from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
import uuid

class Competition(SQLModel, table=True):
    id: Optional[uuid.UUID] = Field(default=uuid.uuid4, primary_key=True)
    created_at: datetime = Field(default=datetime.utcnow)
    updated_at: datetime = Field(default=datetime.utcnow)
    deleted_at: Optional[datetime] = None
    number: int # used in the URL Query
    tr_name: str
    tr_description: str
    tr_link: str
    en_name: str
    en_description: str
    en_link: str
    ar_name: str
    ar_description: str
    ar_link: str
    years: list[int] # The years that the competition is held
    min_member: int # Minimum number of members in a team
    max_member: int # Maximum number of members in a team
    comments: list[uuid.UUID]
    reports_files: dict[int, str] # Links or File paths to the previous years' reports of the competition and the year that the reports belong to
    results_files: dict[int, str] # Links or File paths to the previous years' results of the competition and the year that the results belong to
    