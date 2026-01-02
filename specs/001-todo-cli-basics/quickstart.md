# Quickstart: In-memory Todo CLI Application

This guide provides instructions on how to set up and run the Todo CLI application.

## Prerequisites

- Python 3.13 or higher.
- `git` for cloning the repository.

## Setup

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create a virtual environment** (recommended):
    ```bash
    python -m venv .venv
    ```

3.  **Activate the virtual environment**:
    -   **Windows**:
        ```powershell
        .venv\Scripts\Activate.ps1
        ```
    -   **macOS/Linux**:
        ```bash
        source .venv/bin/activate
        ```

4.  **Install dependencies**:
    This project uses `pytest` for testing.
    ```bash
    pip install pytest
    ```

## Running the Application

To start the application, run the main script from the root of the project directory:

```bash
python src/main.py
```

The application will launch and display a menu of available commands.

## Running Tests

To ensure the application is working correctly, you can run the test suite:

```bash
pytest
```

This command will discover and run all tests located in the `tests/` directory.
