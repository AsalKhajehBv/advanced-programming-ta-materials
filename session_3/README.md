# Session 3: Library

- A library is a collection of code (functions, classes, modules) that can be reused in multiple projects.

- Hosting it on GitHub allows others to see, download, and contribute to it.

## Tools You Need

- Python installed

- Git installed

- A GitHub account

- A code editor

## Plan Your Library

```arduino
math_tools_project/
│
├── math_tools/
│   ├── __init__.py
│   ├── operations.py
│
├── tests/
│   └── test_operations.py
│
├── README.md
├── setup.py
└── .gitignore
```

### What is a README file?

A `README.md` file is a documentation file that appears on the front page of a GitHub repository.
It tells anyone who visits what the project is, how to use it, how to install it, and sometimes, how to contribute. The `.md` extension stands for Markdown, a lightweight text formatting language.

With Markdown, you can add:

Bold text → **bold**

Italic text → *italic*

Code blocks → `code`

Headings →
## Heading

Lists →
- item 1
- item 2

Links → [title](url)

Code blocks →
```python
print("Hello!")
```

### What `.gitignore` Does

`.gitignore` is a special file used by Git to tell it which files or folders to ignore — meaning they won’t be tracked, committed, or uploaded to GitHub.

This keeps your repository clean and free of unnecessary or private files (like temporary data, caches, system files, or passwords).

#### Why You Need It

When you write and run Python code, your system automatically generates some extra files — for example:

`__pycache__/` — stores compiled bytecode (`.pyc` files). Not needed in version control.

`.vscode/` — local VS Code configuration; only useful on your machine.

`.env` — often stores private variables (like tokens or passwords).

`.ipynb_checkpoints/` — Jupyter auto-saves, not relevant to the main code.

If you don’t ignore them, they’ll show up in your Git commits and clutter your GitHub repo.

#### Here’s the added .gitignore file:

```bash
__pycache__/
*.pyc
.env
.envrc
.vscode/
.ipynb_checkpoints
```

|Line |	Meaning|
|-----|---------------|
|__pycache__/ |	Ignore all __pycache__ folders created by Python when running code.|
|*.pyc |	Ignore all compiled Python files (they end with .pyc).|
|.env |	Ignore the .env file, which might store private environment variables (e.g., GitHub tokens).|
|.envrc |	Similar to .env, often used for environment setup; ignore for privacy.|
|.vscode/ |	Ignore your VS Code settings (workspace preferences, extensions, etc.).|
|.ipynb_checkpoints |	Ignore temporary Jupyter Notebook checkpoint files.|

Once you create a .gitignore file and commit it, Git automatically checks it before adding files.

### What is setup.py?

`setup.py` is a Python script used by setuptools (a Python packaging tool) to tell Python and pip how to install your library.

It contains metadata about the package (like name, version, author) and instructions on which files to include.

Once it’s set up, students can run:

```bash
pip install -e .
```

to install the library.

#### Basic Structure

A minimal setup.py looks like this:

```python
from setuptools import setup, find_packages

setup(
    name="math_tools",          # Name of the package
    version="0.0.1",            # Version number
    description="Small math helpers",  # Short description
    packages=find_packages(),    # Automatically finds all packages in folder and returns a list of their names to include when installing your library
    python_requires=">=3.8",     # Python version requirement
)
```

### What is `__init__.py`?

`__init__.py` is a special Python file that tells Python that a directory is a package.

Without it, Python would treat that folder as just a normal directory — not something it can import from.

You can use `__all__` to define what’s available when users import everything.

```python
from math_tools import *
```