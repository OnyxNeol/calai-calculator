# CalAI Calculator OS CLI

A modular, CRUDC-based calculator system with intelligent archive management.

## Author
Selvam + Copilot

## Features
- Arithmetic: add, sub, mul, div (with zero-division guard)
- **V Archive** — Store up to 30 results
- **VF Archive** — Store up to 26 named formulas (A–Z)
- **STRV Archive** — 30 data streams (A1–A30)
- **VP Archive** — 30 process slots (B1–B30)
- **VC Archive** — 30 CalAI chat histories (C1–C30)
- **CalAI core** — Gemma-4 simulation engine

## Run
```bash
python3 calai_calculator.py
```

## Commands
| Command | Description |
|---------|-------------|
| `add X Y` | Add two numbers |
| `sub X Y` | Subtract |
| `mul X Y` | Multiply |
| `div X Y` | Integer divide |
| `vp SLOT` | Save process to VP archive |
| `vc SLOT` | Save CalAI chat to VC archive |
| `call CalAI QUERY` | Query the CalAI engine |
| `list` | Show all archive contents |
| `exit` | Quit |

## License
MIT
