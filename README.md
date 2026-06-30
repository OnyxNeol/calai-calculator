# CalAI Calculator OS CLI

> Modular CRUDC archive calculator with AI core — runs anywhere Python runs.

## Install

```bash
pip install calai-calculator
```

## Usage

```bash
# Interactive REPL
calai

# One-shot
calai add 5 3
calai mul 6 7
calai div 10 0

# Smartwatch / minimal mode
calai --watch

# Version
calai --version
```

## Commands

| Command | Example | Description |
|---------|---------|-------------|
| `add X Y` | `add 5 3` | Add → auto-saved to V |
| `sub X Y` | `sub 10 4` | Subtract |
| `mul X Y` | `mul 6 7` | Multiply |
| `div X Y` | `div 20 4` | Integer divide |
| `v SLOT VAL` | `v 1 42` | Save to V archive |
| `vf SLOT EXPR` | `vf A "add(3,4)"` | Save formula to VF |
| `strv SLOT VAL` | `strv A1 99` | Save stream to STRV |
| `vp SLOT` | `vp B1` | Save process marker |
| `vc SLOT` | `vc C1` | Save CalAI chat |
| `call CalAI ...` | `call CalAI what is 2+2` | Query CalAI |
| `read V 1` | `read VF A` | Read from archive |
| `del V 1` | `del VP B1` | Delete from archive |
| `list` | | Show all archives |

## Archives

| Archive | Slots | Purpose |
|---------|-------|---------|
| V | 30 | Auto-saved numeric results |
| VF | 26 | Named formulas (A–Z) |
| STRV | 30 | Data streams |
| VP | 30 | Process markers |
| VC | 30 | CalAI chat histories |

## Smartwatch Mode

Compact output designed for tiny screens (e.g. WearOS, Tizen):

```bash
calai --watch
```

## Author

Onyxl

## License
MIT
