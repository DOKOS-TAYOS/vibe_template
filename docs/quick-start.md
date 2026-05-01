# Quick Start

## 1. Create the Environment

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e .[dev]
```

Linux or macOS:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e .[dev]
```

## 2. Bootstrap the Template

```bash
python -m project_name.cli bootstrap
```

The bootstrap step asks for:

- project title
- distribution name
- package name
- author name
- initial version
- project scope
- license choice

## 3. Verify the Base

```bash
python -m project_name.cli quality
```

## 4. Start Building

- keep the public API minimal
- add tests before behavior changes
- update `CHANGELOG.md`
- update `docs/docs_for_ai/status.md`
