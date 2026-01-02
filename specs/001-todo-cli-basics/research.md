# Research: In-memory Todo CLI Application

**Purpose**: To document the technology and design decisions made for the Todo CLI application.

## 1. Programming Language

- **Decision**: Python 3.13+
- **Rationale**: This was mandated by the project constitution. Python's simplicity and extensive standard library make it ideal for a beginner-friendly CLI application without requiring external dependencies.
- **Alternatives Considered**: None, as this was a primary constraint.

## 2. Data Storage

- **Decision**: In-memory Python dictionary.
- **Rationale**: The constitution requires ephemeral, in-memory storage only. A Python dictionary provides an efficient and simple way to store and access tasks using a unique ID as the key. For instance: `tasks = {1: Task(...), 2: Task(...)}`.
- **Alternatives Considered**:
  - **List of objects**: A simple list `[Task(), Task()]` would work, but managing unique IDs and lookups would be less efficient (O(n) search) compared to a dictionary's O(1) key lookup.

## 3. Testing Framework

- **Decision**: `pytest`.
- **Rationale**: While `unittest` is built-in, `pytest` has become the de-facto standard in the Python community. It offers a simpler, less boilerplate-heavy syntax for writing tests, better fixture management, and powerful plugins. This aligns with the "Clean Code" principle.
- **Alternatives Considered**:
  - **`unittest`**: The built-in library is a viable option but is more verbose than `pytest`.

## 4. Code Structure

- **Decision**: A modular structure within the `src/` directory.
  - `src/models.py`: To define the `Task` data class.
  - `src/services.py`: For the core business logic (adding, updating, deleting tasks from the in-memory store).
  - `src/main.py`: The main application loop and user-facing CLI presentation logic.
- **Rationale**: This separation of concerns aligns with the "Clean Code" principle. It decouples the data representation (`models`), the core logic (`services`), and the user interface (`main`), making the code easier to understand, test, and maintain.
- **Alternatives Considered**:
  - **Single-file script**: This would be simpler for a tiny script but would violate the separation of concerns for an application with multiple distinct functions, making it harder to scale or maintain.
