# Hands-On: Code Formatting and Linting in Python

These exercises will help you learn to automatically format Python code using tools like `black`, and identify problems using linters like `flake8` or `pylint`.

---

## Hands-On #1

### Exercise 0:

1. Clone the following repository:  https://github.com/shafe123/AI2C-python-formatting.git

1. Open the new repository as a folder in VS Code.

1. Install prerequisites via the terminal. (Optional, setup a virtual environment beforehand)
```bash
pip install black flake8 pylint pre-commit
```

### Exercise 1: Format Code with `black`

**Goal**: Use `black` to autoformat an unformatted Python script.

1. Install black by running the following command.

2. Look at the file called `messy.py`, it should resemble the following:

```python
def greet(name): print("Hello,"+name)
greet("world")
```

2. Run `black`:

```bash
black messy.py
```

✅ *Check*: The file should now be properly formatted with consistent indentation and spacing.

🎯 *Extra*:  config VS Code to use black as its autoformatter on python files.

---

### Exercise 2: Format an Entire Directory

**Goal**: Use `black` to format all `.py` files in a project.

1. Inspect the remaining files and observe how they change after running black.

```bash
black .
```

✅ *Check*: All Python files in the current directory and subdirectories are formatted.

---

### Exercise 3: Install and Run `flake8`

**Goal**: Use `flake8` to identify potential issues in a Python file.

1. Check the contents of `bad_style.py` before running the tool.

1. Run `flake8`:

```bash
flake8 bad_style.py
```

✅ *Check*: Output should list issues such as unused imports, extra spaces, and unused functions.

🎯 *Extra*:  Run flake8 on the whole directory.

---

### Exercise 4: Configure `flake8` with a Config File

**Goal**: Customize `flake8` using a configuration file.

1. Create a `.flake8` file in the repository's root directory, this particular config makes it compatible with black:

```
[flake8]
max-line-length = 88
extend-ignore = E203, W503
```

2. Re-run:

```bash
flake8 bad_style.py
```

For more details read https://black.readthedocs.io/en/stable/guides/using_black_with_other_tools.html

✅ *Check*: You should not see the line-length warning anymore.

---

### Exercise 5: Lint with `pylint`

**Goal**: Use `pylint` to get more detailed feedback.

1. Run it on `bad_style.py`:

```bash
pylint bad_style.py
```

✅ *Check*: You'll receive a score and detailed output for code quality, style, and possible bugs.

🎯 *Extra*:  Run pylint on the whole directory

---

### Exercise 6: Format and Lint as a Pre-Commit Hook

**Goal**: Set up autoformatting and linting with `pre-commit` hooks.

1. Create a `.pre-commit-config.yaml`:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 25.1.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 6.1.0
    hooks:
      - id: flake8
```

2. Install and run hooks, note the output of the command:

```bash
pre-commit install
pre-commit run --all-files
```

3. Run the hooks again, did the output change?

```bash
pre-commit run --all-files
```

✅ *Check*: Try committing and ensure that the files are formatted and checked before committing.

🤚 *Hint*: You can use `git restore *` to change all the files back to the original version that you pulled.

🎯 *Extra*:  Fix the errors and try committing again.

---

### Exercise 7: Add More Tools to Pre-Commit

**Goal**: Enhance your pre-commit workflow by adding additional code quality tools.

1. Update your `.pre-commit-config.yaml` to include more hooks, such as `isort` (for import sorting), `docformatter` (for docstring formatting), and other useful tools:

```yaml
repos:
  - repo: https://github.com/psf/black
    rev: 25.1.0
    hooks:
      - id: black
  - repo: https://github.com/pycqa/flake8
    rev: 7.3.0
    hooks:
      - id: flake8
  - repo: https://github.com/PyCQA/isort
    rev: 6.0.1
    hooks:
      - id: isort
  - repo: https://github.com/PyCQA/docformatter
    rev: v1.7.6
    hooks:
      - id: docformatter
        args: ["--black", "--in-place", "--recursive", "."]
  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: v1.17.0
    hooks:
      - id: mypy
  - repo: https://github.com/PyCQA/bandit
    rev: 1.8.6
    hooks:
      - id: bandit
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-json
      - id: check-added-large-files
  - repo: https://github.com/codespell-project/codespell
    rev: v2.4.1
    hooks:
      - id: codespell
```

2. Reinstall the hooks to update them:

```bash
pre-commit install
pre-commit run --all-files
```

✅ *Check*: Try committing again. Now, in addition to formatting and linting, your code will be checked for types, security issues, spelling, trailing whitespace, and more.