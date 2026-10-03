# Snake Eyes

A command-line dice game. Bet points on a roll of two dice — roll snake eyes (two 1s) and win 35x your bet; roll anything else and lose it.

## Setup

### 1. Create a virtual environment

From the `snakeEyes` folder (one time only):

**macOS / Linux:**

```bash
python3 -m venv .venv
```

**Windows:**

```powershell
py -m venv .venv
```

### 2. Activate it

Each time you open a new terminal:

**macOS / Linux:**

```bash
source .venv/bin/activate
```

**Windows (PowerShell):**

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell says running scripts is disabled, run this once, then try again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

**Windows (Command Prompt):**

```cmd
.venv\Scripts\activate.bat
```

Your prompt will show `(.venv)` when it's active. Run `deactivate` to turn it off.

### 3. Install pytest

With the virtual environment active:

```bash
python -m pip install pytest
```

## Running the tests

```bash
python -m pytest -v
```

## Playing the game

```bash
python main.py
```
