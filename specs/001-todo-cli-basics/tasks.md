# Tasks: In-memory Todo CLI Application

**Input**: Design documents from `/specs/001-todo-cli-basics/`
**Prerequisites**: `plan.md`, `spec.md`, `data-model.md`

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure.

- [x] T001 Create the directory structure: `src/` and `tests/unit/`.
- [x] T002 Create a `pyproject.toml` file to define project metadata and dependencies.
- [x] T003 Add `pytest` as a development dependency in `pyproject.toml`.
- [x] T004 [P] Create a `.gitignore` file with standard Python ignores.
- [x] T005 [P] Create a basic `ruff.toml` or `.flake8` configuration file for linting.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core data models and services that must be complete before any user story can be implemented.

- [x] T006 Implement the `TaskStatus` enum and the `Task` data class in `src/models.py` as defined in `data-model.md`.
- [x] T007 Create the `TaskService` class in `src/services.py`. It should initialize an in-memory dictionary to store tasks and a counter for task IDs.
- [x] T008 [P] Implement the basic application loop in `src/main.py` which will display a menu and prompt for user input.

---

## Phase 3: User Story 1 - Add and View Tasks (Priority: P1) 🎯 MVP

**Goal**: Allow users to add new tasks and see a list of all their tasks.
**Independent Test**: User can start the app, add a task, and see it displayed in the task list.

### Implementation for User Story 1

- [x] T009 [US1] Implement the `add_task(title: str, description: str)` method in the `TaskService` (`src/services.py`). It should create a new `Task` object, assign it a new ID, and store it in the dictionary.
- [x] T010 [US1] Implement the `get_all_tasks()` method in the `TaskService` (`src/services.py`) that returns a list of all current tasks.
- [x] T011 [US1] In `src/main.py`, create a function to handle adding a task. This function should prompt the user for a title and optional description, then call the `add_task` service method.
- [x] T012 [US1] In `src/main.py`, create a function to handle viewing all tasks. This function should call `get_all_tasks` and print the formatted list to the console, showing ID, title, description, and status.

---

## Phase 4: User Story 2 - Mark Task as Completed (Priority: P2)

**Goal**: Allow users to mark a task as completed.
**Independent Test**: User can list tasks, select one by its ID, and mark it as complete. The updated status is visible in the task list.

### Implementation for User Story 2

- [x] T013 [US2] Implement the `complete_task(task_id: int)` method in the `TaskService` (`src/services.py`). It should find the task by its ID and update its status to `COMPLETED`.
- [x] T014 [US2] In `src/main.py`, add a menu option and a handler function to prompt the user for a task ID and call the `complete_task` service method.

---

## Phase 5: User Story 3 - Update a Task (Priority: P3)

**Goal**: Allow users to edit the title or description of a task.
**Independent Test**: User can list tasks, select one, and edit its title/description. The changes are visible in the task list.

### Implementation for User Story 3

- [x] T015 [US3] Implement the `update_task(task_id: int, new_title: str, new_description: str)` method in the `TaskService` (`src/services.py`).
- [x] T016 [US3] In `src/main.py`, add a menu option and handler to let the user choose a task to update and provide the new text.

---

## Phase 6: User Story 4 - Delete a Task (Priority: P4)

**Goal**: Allow users to remove a task from their list.
**Independent Test**: User can add a task and then successfully delete it, confirming it no longer appears in the list.

### Implementation for User Story 4

- [x] T017 [US4] Implement the `delete_task(task_id: int)` method in the `TaskService` (`src/services.py`).
- [x] T018 [US4] In `src/main.py`, add a menu option and handler to prompt for a task ID and call the `delete_task` service method.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final improvements for usability and robustness.

- [x] T019 Implement validation and error handling in `src/main.py` for all user inputs. This includes handling non-existent task IDs and invalid menu choices, showing friendly error messages.
- [x] T020 Add a main menu option in `src/main.py` to exit the application cleanly.
- [x] T021 [P] Write unit tests for the `TaskService` methods (`add`, `get`, `update`, `delete`, `complete`) in `tests/unit/test_services.py`.
- [ ] T022 Create a `README.md` file in the project root with a description and clear instructions on how to run the app and its tests, based on `quickstart.md`.

---

## Dependencies & Execution Order

- **Setup (Phase 1)** must be completed first.
- **Foundational (Phase 2)** depends on Phase 1. It blocks all user story implementation.
- **User Stories (Phase 3-6)** can be implemented in any order after Phase 2 is complete, but following the priority (P1 -> P4) is recommended for iterative delivery.
- **Polish (Phase 7)** can be worked on after the user stories are complete. Unit tests (T021) can be developed in parallel with their corresponding service methods.
