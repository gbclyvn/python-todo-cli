# Simple Python To-Do CLI 🚀

A lightweight, minimal Command Line Interface (CLI) To-Do List application built with **Python** and **Google Fire**. This application saves your tasks locally to a plain text file (`todo.txt`), meaning your entries are preserved even after you close your terminal.

This project was built from scratch to practice functional Python programming without complex classes or boilerplates.

---

## ✨ Features

- **Add Tasks**: Instantly append new items to your local file.
- **View List**: Read all active items printed sequentially.
- **Remove Items**: Safely search for and erase a specific task by text.
- **Persistent Storage**: Data is automatically saved locally in `todo.txt`.

---

## 🛠️ Prerequisites

Make sure you have Python installed and the Google Fire library added to your environment:

```bash
# Install Google Fire if you haven't already
pip install fire
```

---

## 🚀 How To Use

Navigate to your project directory in the terminal and execute the following commands:

### 1. Add a new task
```bash
python simple_todo.py add "Buy milk"
python simple_todo.py add "Study Python loops"
```

### 2. View your current list
```bash
python simple_todo.py list
```

### 3. Remove a completed task
```bash
python simple_todo.py remove "Buy milk"
```

---

## 📂 File Structure

```text
├── simple_todo.py    # Main application logic
├── todo.txt          # Automatically generated text file holding your data
└── README.md         # Documentation
```

---

## 🌱 Learning Milestones

This project was built to master the fundamentals of:
1. **File Handling**: Opening, writing (`a` mode), reading (`r`), and overwriting (`w`) text files in Python.
2. **CLI Automation**: Using Google Fire to instantly turn standard functions into callable terminal commands.
3. **Array Manipulation**: Modifying raw string data inside dynamic Python lists.
