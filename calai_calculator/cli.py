#!/usr/bin/env python3
"""CalAI Calculator OS — CLI entry point."""
import sys
import argparse
from .core import CalAI, V, VF, STRV, VP, VC, add, sub, mul, div

BANNER = r"""
  ____      _    _    ___ 
 / ___|__ _| |  / \  |_ _|
| |   / _` | | / _ \  | | 
| |__| (_| | |/ ___ \ | | 
 \____\__,_|_/_/   \_\___|
 Calculator OS CLI  v1.1.0
"""

HELP = """
Commands:
  add  X Y        Add two numbers
  sub  X Y        Subtract
  mul  X Y        Multiply
  div  X Y        Integer divide
  v    SLOT VAL   Save result to V archive  (e.g. v 1 42)
  vf   SLOT EXPR  Save formula to VF        (e.g. vf A "add(3,4)")
  strv SLOT VAL   Save stream to STRV       (e.g. strv A1 99)
  vp   SLOT       Save process marker to VP (e.g. vp B1)
  vc   SLOT       Save CalAI chat to VC     (e.g. vc C1)
  call CalAI ...  Query CalAI engine
  read V SLOT     Read from any archive     (e.g. read V 1)
  del  V SLOT     Delete from archive
  list            Show all archive contents
  help            Show this message
  exit / quit     Exit
"""

calai = CalAI()
ARCHIVES = {"V": V, "VF": VF, "STRV": STRV, "VP": VP, "VC": VC}
result_counter = [1]

def auto_v(result):
    """Auto-save numeric results to next V slot."""
    slot = str(result_counter[0])
    if result_counter[0] <= 30:
        V.create(slot, result)
        result_counter[0] += 1
    return slot

def run():
    parser = argparse.ArgumentParser(description="CalAI Calculator OS CLI", add_help=False)
    parser.add_argument("--watch", action="store_true", help="Minimal smartwatch mode")
    parser.add_argument("--version", action="store_true")
    parser.add_argument("cmd", nargs="*")
    args = parser.parse_args()

    if args.version:
        print("calai-calculator 1.1.0")
        return

    watch_mode = args.watch

    # One-shot mode: calai add 3 4
    if args.cmd:
        _exec(" ".join(args.cmd), watch_mode)
        return

    # Interactive REPL
    if not watch_mode:
        print(BANNER)
    else:
        print("CalAI v1.1 [watch]")

    prompt = "> " if watch_mode else "calai >> "
    while True:
        try:
            cmd = input(prompt).strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break
        if not cmd:
            continue
        if cmd in ("exit", "quit"):
            print("Bye!")
            break
        if cmd == "help":
            print(HELP if not watch_mode else _watch_help())
            continue
        _exec(cmd, watch_mode)


def _watch_help():
    return "a b  + - * /  v#  list  call  exit"


def _exec(cmd, watch=False):
    parts = cmd.split()
    if not parts:
        return

    def out(msg):
        print(msg)

    op = parts[0].lower()

    try:
        if op == "add":
            r = add(float(parts[1]), float(parts[2]))
            slot = auto_v(r)
            out(f"{r}  →V{slot}" if not watch else str(r))
        elif op == "sub":
            r = sub(float(parts[1]), float(parts[2]))
            slot = auto_v(r)
            out(f"{r}  →V{slot}" if not watch else str(r))
        elif op == "mul":
            r = mul(float(parts[1]), float(parts[2]))
            slot = auto_v(r)
            out(f"{r}  →V{slot}" if not watch else str(r))
        elif op == "div":
            r = div(float(parts[1]), float(parts[2]))
            if isinstance(r, str):
                out(r)
            else:
                slot = auto_v(r)
                out(f"{r}  →V{slot}" if not watch else str(r))
        elif op == "v":
            out(V.create(parts[1], parts[2]) if len(parts) > 2 else V.read(parts[1]))
        elif op == "vf":
            out(VF.create(parts[1], " ".join(parts[2:])) if len(parts) > 2 else VF.read(parts[1]))
        elif op == "strv":
            out(STRV.create(parts[1], parts[2]) if len(parts) > 2 else STRV.read(parts[1]))
        elif op == "vp":
            slot = parts[1] if len(parts) > 1 else "B1"
            out(VP.create(slot, "process"))
        elif op == "vc":
            slot = parts[1] if len(parts) > 1 else "C1"
            out(calai.save_chat(slot))
        elif op == "call" and len(parts) > 1 and parts[1].lower() == "calai":
            query = " ".join(parts[2:]) or "?"
            out(calai.call(query))
        elif op == "read" and len(parts) >= 3:
            arch = ARCHIVES.get(parts[1].upper())
            out(arch.read(parts[2]) if arch else "Unknown archive.")
        elif op == "del" and len(parts) >= 3:
            arch = ARCHIVES.get(parts[1].upper())
            out(arch.delete(parts[2]) if arch else "Unknown archive.")
        elif op == "list":
            if watch:
                out(f"V:{len(V.slots)} VF:{len(VF.slots)} VP:{len(VP.slots)} VC:{len(VC.slots)}")
            else:
                for name, arch in ARCHIVES.items():
                    out(f"  {name}: {arch.list_all() or 'empty'}")
        else:
            out("?" if watch else f"Unknown: '{op}'. Type 'help'.")
    except (IndexError, ValueError) as e:
        out(f"Err: {e}" if watch else f"Error: {e}  — check arguments.")


if __name__ == "__main__":
    run()
