# CalAI Calculator OS — Core Engine
# Author: Selvam + Copilot

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
        return dict(self.slots)


V    = ArchiveSystem(30, "V")
VF   = ArchiveSystem(26, "VF")
STRV = ArchiveSystem(30, "STRV")
VP   = ArchiveSystem(30, "VP")
VC   = ArchiveSystem(30, "VC")


class CalAI:
    def __init__(self):
        self.history = []

    def call(self, query):
        response = f"CalAI › {query}"
        self.history.append(response)
        return response

    def save_chat(self, slot):
        if len(VC.slots) >= VC.max_slots:
            return "VC archive full!"
        VC.create(slot, self.history.copy())
        return f"VC{slot} saved."

    def list_chats(self):
        return VC.list_all()


def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x // y if y != 0 else "Error: divide by zero"
