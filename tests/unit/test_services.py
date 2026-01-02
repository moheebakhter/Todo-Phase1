import pytest
from src.services import TaskService
from src.models import TaskStatus


@pytest.fixture
def task_service():
    """Fixture to create a TaskService instance for each test."""
    return TaskService()


def test_add_task(task_service):
    """Test adding a task."""
    task = task_service.add_task("Test Title", "Test Description")
    assert task.task_id == 1
    assert task.title == "Test Title"
    assert task.description == "Test Description"
    assert task.status == TaskStatus.PENDING
    assert len(task_service.get_all_tasks()) == 1


def test_get_all_tasks(task_service):
    """Test getting all tasks."""
    task_service.add_task("Task 1", "Desc 1")
    task_service.add_task("Task 2", "Desc 2")
    tasks = task_service.get_all_tasks()
    assert len(tasks) == 2
    assert tasks[0].title == "Task 1"
    assert tasks[1].title == "Task 2"


def test_complete_task(task_service):
    """Test completing a task."""
    task = task_service.add_task("Test Task", "")
    assert task.status == TaskStatus.PENDING
    
    updated_task = task_service.complete_task(task.task_id)
    assert updated_task is not None
    assert updated_task.status == TaskStatus.COMPLETED
    
    # Test completing a non-existent task
    assert task_service.complete_task(999) is None


def test_update_task(task_service):
    """Test updating a task."""
    task = task_service.add_task("Original Title", "Original Desc")
    
    updated_task = task_service.update_task(
        task_id=task.task_id,
        new_title="New Title",
        new_description="New Desc"
    )
    assert updated_task is not None
    assert updated_task.title == "New Title"
    assert updated_task.description == "New Desc"
    
    # Test updating a non-existent task
    assert task_service.update_task(999, "T", "D") is None


def test_delete_task(task_service):
    """Test deleting a task."""
    task1 = task_service.add_task("Task 1", "")
    task_service.add_task("Task 2", "")
    
    assert len(task_service.get_all_tasks()) == 2
    
    deleted_task = task_service.delete_task(task1.task_id)
    assert deleted_task is not None
    assert deleted_task.task_id == task1.task_id
    assert len(task_service.get_all_tasks()) == 1
    assert task_service.get_all_tasks()[0].title == "Task 2"
    
    # Test deleting a non-existent task
    assert task_service.delete_task(999) is None
    assert len(task_service.get_all_tasks()) == 1
