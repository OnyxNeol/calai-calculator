# CalAI Calculator OS CLI
# Author: Selvam + Copilot
# Modular CRUDC system with archives: V, VF, STRV, VP, VC
# Includes CLI loop for interactive commands

import sys

class ArchiveSystem:
    def __init__(self, max_slots, prefix):
        self.max_slots = max_slots
        self.prefix = prefix
        self.slots = {}

    def create(self, slot, content):
        if len(self.slots) >= self.max_slots:
            return f"{self.prefix} archive full!"
        self.slots[slot] = content
        return f"{self.prefix}{slot} saved."

    def read(self, slot):
        return self.slots.get(slot, f"{self.prefix}{slot} empty.")

    def update(self, slot, content):
        if slot in self.slots:
            self.slots[slot] = content
            return f"{self.prefix}{slot} updated."
        return f"{self.prefix}{slot} not found."

    def delete(self, slot):
        if slot in self.slots:
            del self.slots[slot]
            return f"{self.prefix}{slot} deleted."
        return f"{self.prefix}{slot} not found."

    def check(self, slot):
        return f"{self.prefix}{slot}: {self.slots.get(slot, 'empty')}"

    def list_all(self):
        return {slot: content for slot, content in self.slots.items()}


# Initialize archives
V = ArchiveSystem(30, "V")       # Results 1–30
VF = ArchiveSystem(26, "VF")     # Formulas A–Z
STRV = ArchiveSystem(30, "STRV") # Streams A1–A30
VP = ArchiveSystem(30, "VP")     # Processes B1–B30
VC = ArchiveSystem(30, "VC")     # Chats C1–C30

# CalAI core (compressed Gemma-4 simulation)
class CalAI:
    def __init__(self):
        self.history = []

    def call(self, query):
        response = f"CalAI response to: {query}"
        self.history.append(response)
        return response

    def save_chat(self, slot):
        if len(VC.slots) >= VC.max_slots:
            return "VC archive full!"
        VC.create(slot, self.history.copy())
        return f"VC{slot} saved."

    def list_chats(self):
        return VC.list_all()


calai = CalAI()

# Arithmetic functions
def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x // y if y != 0 else "Error: divide by zero"

# CLI loop
def main():
    print("=== CalAI Calculator OS CLI ===")
    print("Type commands (add, sub, mul, div, vp, vc, call CalAI, exit)")
    while True:
        cmd = input(">> ").strip()
        if cmd == "exit":
            print("Goodbye!")
            sys.exit(0)

        parts = cmd.split()
        if not parts:
            continue

        if parts[0] == "add":
            result = add(int(parts[1]), int(parts[2]))
            print("Result:", result)
        elif parts[0] == "sub":
            result = sub(int(parts[1]), int(parts[2]))
            print("Result:", result)
        elif parts[0] == "mul":
            result = mul(int(parts[1]), int(parts[2]))
            print("Result:", result)
        elif parts[0] == "div":
            result = div(int(parts[1]), int(parts[2]))
            print("Result:", result)
        elif parts[0] == "vp":
            slot = parts[1] if len(parts) > 1 else "B1"
            print(VP.create(slot, "Process saved"))
        elif parts[0] == "vc":
            slot = parts[1] if len(parts) > 1 else "C1"
            print(calai.save_chat(slot))
        elif parts[0] == "call" and len(parts) > 1 and parts[1] == "CalAI":
            query = " ".join(parts[2:]) if len(parts) > 2 else "No query"
            print(calai.call(query))
        elif parts[0] == "list":
            print("V:", V.list_all())
            print("VF:", VF.list_all())
            print("STRV:", STRV.list_all())
            print("VP:", VP.list_all())
            print("VC:", VC.list_all())
        else:
            print("Unknown command.")

if __name__ == "__main__":
    main()
