# 📝 Todo In-Memory CLI Application (Phase I)

## 📌 Overview
This project is a **Python-based command-line Todo application** developed for **Hackathon Phase I** using a **spec-driven, agentic development approach**.

The application allows users to manage todo tasks **entirely in memory**, focusing on clean architecture, modular design, and reproducible development practices.

---

## 🎯 Objective
To build a working console application that demonstrates:

- Adding tasks with title and description
- Viewing all tasks with status indicators
- Updating task details
- Deleting tasks by ID
- Marking tasks as completed and incomplete
- Clean project structure
- Spec-driven development workflow (no vibe coding)

---

## ⚙️ Technology Stack
- **Python**: 3.13+
- **UV**: Python package & environment manager
- **Spec-Kit Plus**: Specification-driven development
- **pytest**: Unit testing
- **ruff**: Linting & formatting
- **CLI (Command Line Interface)**

---

## 🧠 Development Approach
This project strictly follows the **Agentic Dev Stack workflow**:

1. Constitution creation
2. Formal specifications
3. Task breakdown
4. AI-assisted implementation
5. Review & validation

All logic was implemented using structured prompts and reusable intelligence — **no ad-hoc or vibe coding**.

---

## 📂 Project Structure

Todo-Phase1/
│
├── .gemini/ # Gemini CLI metadata
├── .pytest_cache/
├── .specify/ # Spec-Kit Plus internal data
├── history/ # Specification history
├── specs/ # Formal specifications
│
├── src/
│ ├── init.py
│ ├── main.py # CLI entry point
│ ├── models.py # Task & status models
│ └── services.py # Business logic layer
│
├── tests/
│ └── unit/
│ └── test_services.py # Unit tests
│
├── .gitignore
├── GEMINI.md
├── pyproject.toml
├── ruff.toml
└── README.md


## ✅ Features Implemented

### Core Features
- ➕ Add a task (title + optional description)
- 📋 View all tasks with status indicators
- ✏️ Update task title and description
- 🗑️ Delete a task by ID
- ✅ Mark task as **Completed**
- 🔁 Mark task as **Incomplete**

### Task Status
- `PENDING`
- `COMPLETED`


## 🖥️ Sample CLI Menu

--- Todo CLI ---

Add Task

View All Tasks

Mark Task as Completed

Update Task

Delete Task

Mark Task as Incomplete

Exit


## ▶️ How to Run the Application

### 1️⃣ Install dependencies
```bash
pip install -e .
UV is supported and can be used as the package manager if preferred.

2️⃣ Run the CLI
bash
Copy code
python -m src.main
🧪 Running Unit Tests
bash
Copy code
pytest
📌 Notes
All tasks are stored in memory (no database).

Restarting the application resets all tasks.

Designed for clarity, extensibility, and hackathon evaluation.

Project structure and workflow are reusable for future hackathons.

🏁 Project Status
✅ Phase I – Completed

All required features for Phase I have been successfully implemented and demonstrated through a working console application.
