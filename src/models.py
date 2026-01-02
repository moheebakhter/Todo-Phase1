from dataclasses import dataclass
from enum import Enum, auto


class TaskStatus(Enum):
    """Enum for task status."""
    PENDING = auto()
    COMPLETED = auto()


@dataclass
class Task:
    """Dataclass for a single task."""
    task_id: int
    title: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
