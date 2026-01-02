from typing import Dict, List
from src.models import Task, TaskStatus


class TaskService:
    """Service for managing tasks."""

    def __init__(self):
        self._tasks: Dict[int, Task] = {}
        self._next_id: int = 1

    def add_task(self, title: str, description: str) -> Task:
        """Adds a new task."""
        task = Task(
            task_id=self._next_id,
            title=title,
            description=description,
        )
        self._tasks[self._next_id] = task
        self._next_id += 1
        return task

    def get_all_tasks(self) -> List[Task]:
        """Returns all tasks."""
        return list(self._tasks.values())

    def complete_task(self, task_id: int) -> Task | None:
        """Marks a task as completed."""
        task = self._tasks.get(task_id)
        if task:
            task.status = TaskStatus.COMPLETED
        return task

    # ✅ NEW METHOD (INCOMPLETE)
    def mark_incomplete(self, task_id: int) -> Task | None:
        """Marks a task as incomplete (pending)."""
        task = self._tasks.get(task_id)
        if task:
            task.status = TaskStatus.PENDING
        return task

    def update_task(self, task_id: int, new_title: str, new_description: str) -> Task | None:
        """Updates a task's title and description."""
        task = self._tasks.get(task_id)
        if task:
            task.title = new_title
            task.description = new_description
        return task

    def delete_task(self, task_id: int) -> Task | None:
        """Deletes a task."""
        if task_id in self._tasks:
            return self._tasks.pop(task_id)
        return None
