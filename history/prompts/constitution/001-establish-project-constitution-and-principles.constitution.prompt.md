---
id: 001
title: Establish Project Constitution and Principles
stage: constitution
date: 2026-01-01
surface: "agent"
model: "gemini"
feature: "none"
branch: "main"
user: "user"
command: "/sp.constitution"
labels: [constitution, setup, principles]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
  - .specify/templates/plan-template.md
  - .specify/templates/spec-template.md
  - .specify/templates/tasks-template.md
tests:
  - "none"
---

## Prompt

/sp.constitution Project: Hackathon 2 – Phase I
Todo In-Memory Python Console Application

Purpose:
Build a clean, beginner-friendly, in-memory Todo CLI application using spec-driven development.
The project must demonstrate proper Agentic Dev Stack workflow using Spec-Kit Plus.

Core Principles:
- Spec-driven development only (no vibe coding)
- No manual coding by the human
- All code generated via LLM instructions
- Simple, readable, and maintainable Python
- Beginner-friendly console interaction
- In-memory storage only (no database, no files)

Functional Requirements:
- Add a todo task (title + optional description)
- View all tasks with status (Pending / Completed)
- Update task title or description
- Delete a task
- Mark a task as completed

Technical Standards:
- Python version: 3.13+
- Console-based application
- Use functions and clear separation of concerns
- Follow clean code principles
- Use meaningful variable and function names
- No external frameworks

Project Constraints:
- No persistent storage (memory only)
- No GUI
- No web framework
- No unnecessary complexity

Deliverables:
- /src folder with Python source code
- README.md with usage instructions
- specs/history folder containing all specs
- Working console app demonstrating all features

Evaluation Criteria:
- Correct use of Spec-Kit Plus workflow
- Quality of specifications
- Clear planning and task breakdown
- Clean, correct, and runnable code

## Response snapshot

I have successfully established the project constitution and aligned the specification, planning, and task templates with its principles.

- **`.specify/memory/constitution.md`**: Created version 1.0.0 based on the provided principles and requirements.
- **`.specify/templates/*.md`**: Updated the plan, spec, and task templates to reflect the new constitutional mandates, ensuring future work aligns with the project's standards for simplicity, structure, and workflow.

A Prompt History Record (PHR) has been created to document this setup process.

## Outcome

- ✅ Impact: High. Established the foundational rules for the project.
- 🧪 Tests: N/A. No tests were run.
- 📁 Files: 4 files updated.
- 🔁 Next prompts: /sp.specify to start defining a feature.
- 🧠 Reflection: The process of creating the constitution and then immediately propagating the changes to the project templates is a good way to ensure consistency from the start.

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): none
- Prompt variant (if applicable): none
- Next experiment (smallest change to try): none
