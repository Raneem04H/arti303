# Lab 3 — Environments, Project Structure & Reliable Code

ARTI 303 — Programming for AI

This lab covers virtual environments, dependencies, Python modules,
file handling, error handling, logging, PEP 8, and automated tests.

## Files

- `lab03 (1).ipynb`: completed notebook with outputs.
- `src/`: grade and name-cleaning utilities.
- `tests/`: automated tests for the utilities.
- `data/`: sample student CSV files.
- `requirements.txt`: pinned dependencies.
- `.gitignore`: excludes environments, caches, logs, and credentials.

## Setup and Running

Use Python 3.12. From the repository's main folder, run:

```powershell
cd lab03
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest tests/ -v
```

To run the notebook, open it in VS Code, select the `.venv` kernel,
and choose Run All.

## Test Results

All notebook self-checks passed, and all five automated tests passed.
