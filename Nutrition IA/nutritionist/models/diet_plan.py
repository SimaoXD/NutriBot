from pydantic import BaseModel
from datetime import datetime, timezone
from typing import Optional


class DietPlan(BaseModel):
    user_id: int
    details: int
    created_at: datetime = datetime.now(timezone.utc)