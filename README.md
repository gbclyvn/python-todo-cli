# Local Task Management CLI

A minimalist, functional command-line interface (CLI) application designed for local task tracking. This utility abstracts terminal argument parsing using Google Fire and leverages synchronous file input/output operations to persist data locally in a plain text format.

The primary architectural goal of this codebase is to demonstrate functional programming practices, state persistence via file handling, and efficient collection management without relying on object-oriented structures or verbose boilerplate code.

---

## Features

- **Add Tasks**: Instantly append new items to your local file.
- **View List**: Read all active items printed sequentially.
- **Remove Items**: Safely search for and erase a specific task by text.
- **Persistent Storage**: Data is automatically saved locally in `todo.txt`.


---

## Prerequisites

The application requires Python 3.x and the Google Fire library. Ensure dependencies are satisfied within your active virtual environment prior to execution:

```bash
pip install fire
```

---

## API Usage and Deployment

Execute the application script directly from your terminal by targeting the desired operational commands. 

*Note: Replace `main.py` with the exact filename of your Python source code.*

### 1. Append a New Task
Appends a string argument to the end of the data file ledger.
```bash
python main.py add "Deploy database migrations"
python main.py add "Review open pull requests"
```

### 2. Retrieve All Active Tasks
Reads and displays the current unparsed data array directly from the storage stream.
```bash
python main.py list
```

### 3. Remove a Target Task
Locates, matches, and purges the specified string from the text record before saving the updated file state.
```bash
python main.py remove "Deploy database migrations"
```

---

## Project Structure

```text
├── main.py        # Core application logic and execution commands
├── todo.txt       # Automatically generated text ledger for persistent storage
└── README.md      # Technical documentation and deployment guide
```

---

## Core Competencies Demonstrated

1. **Stream Execution and File Operations**: Implementing file modification modes including append (`a`), read (`r`), and write (`w`) to manipulate local project ledgers safely.
2. **Dynamic Argument Mapping**: Streamlining developer environments by translating low-level script functions directly into clean, standardized executable workflows.
3. **Data Integrity Management**: Managing raw list objects to evaluate and alter application datasets securely.
