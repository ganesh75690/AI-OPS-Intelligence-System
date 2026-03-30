from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    id: int
    description: str
    priority: str

class Action(BaseModel):
    task_id: int
    action_type: str  # assign / escalate / ignore

class Observation(BaseModel):
    tasks: List[Task]
    message: str
