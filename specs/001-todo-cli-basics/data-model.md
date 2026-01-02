# Data Model: Todo CLI Application

This document defines the data structures used in the application.

## 1. Task Entity

This is the central entity in the application.

- **Description**: Represents a single todo item.
- **Storage**: Held in an in-memory dictionary in the `services` layer, where the key is the `task_id`.

### Attributes

| Attribute     | Type         | Description                                        | Constraints / Validation Rules       |
|---------------|--------------|----------------------------------------------------|--------------------------------------|
| `task_id`     | `int`        | A unique identifier for the task.                  | Required, auto-incrementing, unique. |
| `title`       | `str`        | The main description of the task.                  | Required, non-empty string.          |
| `description` | `str`        | Optional additional details about the task.        | Optional, can be an empty string.    |
| `status`      | `TaskStatus` (Enum) | The current state of the task.                   | Must be one of the enum values.      |

### 2. TaskStatus Enum

A simple enumeration to represent the state of a task.

| Value       | Description                         |
|-------------|-------------------------------------|
| `PENDING`   | The initial state of a newly created task. |
| `COMPLETED` | The state of a task that has been finished. |

### Example Representation (Python)

```python
from dataclasses import dataclass
from enum import Enum, auto

class TaskStatus(Enum):
    PENDING = auto()
    COMPLETED = auto()

@dataclass
class Task:
    task_id: int
    title: str
    description: str
    status: TaskStatus = TaskStatus.PENDING
```

### State Transitions

A task can only move from `PENDING` to `COMPLETED`.

1.  **Creation**: A new `Task` is always created with the `PENDING` status.
2.  **Completion**: A user can trigger an action that changes the status from `PENDING` to `COMPLETED`.
3.  No other transitions are permitted (e.g., from `COMPLETED` back to `PENDING`).
