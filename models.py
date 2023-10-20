from pydantic import BaseModel
from enum import Enum
from uuid import UUID, uuid4
from typing import Optional, List


class Location(BaseModel):
    city: str
    state: Optional[str] = None
    country: str = "us"


