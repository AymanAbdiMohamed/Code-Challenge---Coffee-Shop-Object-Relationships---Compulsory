# Coffee Shop Domain Model

## Overview
This Python project models a Coffee Shop domain using object-oriented programming principles. The application defines three main entities: `Customer`, `Coffee`, and `Order`, and establishes relationships between them to simulate real-world interactions in a coffee shop.

The project demonstrates class design, method implementation, data validation, and object relationships in Python.

---

## Features
- **Customer**
  - Has a name (1-15 characters)
  - Can place multiple orders
  - Can list all coffees ordered
  - Can determine the most devoted customer for a coffee (`most_aficionado`)

# Coffee Shop Domain Model

Overview
--------
This small Python project implements a domain model for a coffee shop using three main classes: `Customer`, `Coffee`, and `Order`. It demonstrates class relationships, simple validation, and aggregate methods (for example: average order price, most-aficionado customer for a coffee).

Quick Features
--------------
- `Customer`: name validation (1–15 chars), places orders, lists coffees ordered, `most_aficionado` aggregation
- `Coffee`: name validation (>=3 chars), lists orders and unique customers, `num_orders` and `average_price`
- `Order`: links `Customer` + `Coffee` with a `price` (1.0–10.0) and keeps a global list of orders

Requirements
------------
- Python 3.8+ (3.10/3.11/3.13 tested)
- `pipenv` is supported via the included `Pipfile`, or you can use a plain `venv`.

Quickstart (recommended: Pipenv)
--------------------------------
1. Clone the repository and enter it:

```bash
git clone https://github.com/AymanAbdiMohamed/Code-Challenge---Coffee-Shop-Object-Relationships---Compulsory.git
cd Code-Challenge---Coffee-Shop-Object-Relationships---Compulsory
```

2a. Using `pipenv` (uses `Pipfile`):

```bash
pipenv install --dev
pipenv shell
```

2b. Or using a standard `venv` (portable):

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt || pip install black flake8 pytest
```

Running tests
-------------
Run the test suite with `pytest`:

```bash
pytest -q
```

Linting & Formatting
--------------------
- Format code with `black`:

```bash
black . --exclude ".venv"
```

- Lint with `flake8` (example flags used in this repo):

```bash
flake8 . --exclude .venv --max-line-length=88
```

Usage / Debug CLI
-----------------
There is a small interactive script `debug.py` that can be used to create customers/coffees and place orders from the terminal:

```bash
python debug.py
```

Project layout
--------------
- `coffee.py` — `Coffee` class and related helpers
- `customer.py` — `Customer` class and helpers
- `order.py` — `Order` class and data validation
- `debug.py` — lightweight interactive CLI for manual testing
- `tests/` — pytest tests (run with `pytest`)
- `Pipfile` — optional pipenv dependencies

Notes
-----
- The code uses in-memory lists (class attributes) to track all instances for simplicity; this is intentional for the exercise.
- If you want, I can add a `pyproject.toml` or `setup.cfg` to centralize `black`/`flake8` configuration and add a GitHub Actions workflow to run tests and linters.

Contact / Next steps
--------------------
Tell me if you want me to:

- Add CI (GitHub Actions) to run tests and linters automatically
- Add a `requirements.txt` or `pyproject.toml`
- Tighten typing with `mypy`

Enjoy — and let me know what you'd like next.
