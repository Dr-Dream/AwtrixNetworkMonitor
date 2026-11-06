"""Exercise the handoff methods from the Berry source using a small syntax adapter.

This checks event ordering without compiling Berry or simulating device timing.
Only the simple statements in these methods are translated; API calls are mocks.
"""
from pathlib import Path
import re
from types import SimpleNamespace
import unittest

SOURCE = Path(__file__).resolve().parents[1] / "NetworkMonitor.ax"


def load_methods():
    source = SOURCE.read_text()
    methods = {}
    for name in ("finish_turn", "next_page", "on_hide"):
        match = re.search(r"^  def " + name + r"\(\)\n(.*?)^  end$", source, re.M | re.S)
        if match is None:
            raise AssertionError(f"Missing method: {name}")
        lines = [f"def {name}(self):"]
        for line in match[1].splitlines():
            if line.strip() == "end":
                continue
            line = line[2:]
            line = re.sub(r"\btrue\b", "True", line)
            line = re.sub(r"\bfalse\b", "False", line)
            line = re.sub(r"\bnil\b", "None", line)
            line = re.sub(r"!(?!=)", "not ", line).replace("&&", "and").replace("||", "or")
            if line.lstrip().startswith(("if ", "elif ")) or line.strip() == "else":
                line += ":"
            lines.append(line)
        methods[name] = "\n".join(lines)
    return methods


class RotationHandoffTests(unittest.TestCase):
    def setUp(self):
        self.events = []
        env = {
            "rotation": SimpleNamespace(
                resume=lambda: self.events.append("resume"),
                next=lambda: self.events.append("next"),
            ),
            "timer": SimpleNamespace(cancel=lambda token: self.events.append(("cancel", token))),
        }
        methods = load_methods()
        for code in methods.values():
            exec(code, env)
        app_class = type("App", (), {name: env[name] for name in methods})
        self.app = app_class()
        self.app.visible = True
        self.app.held = True
        self.app.manual_timer = None
        self.app.mode = "auto"
        self.app.fail_count = 0
        self.app.show_nodes = False
        self.app.page = 0
        self.app.reset_entry = lambda: None

    def test_repeated_completion_before_hide_advances_once(self):
        # The next loop can run before the transition delivers on_hide.
        self.app.next_page()
        self.app.next_page()
        self.app.on_hide()
        self.assertEqual(self.events, ["resume", "next"])
        self.assertFalse(self.app.visible)
        self.assertFalse(self.app.held)

    def test_final_nodes_page_and_late_timer_advance_once(self):
        self.app.show_nodes = True
        self.app.page = 2
        self.app.next_page()
        self.app.finish_turn()
        self.app.on_hide()
        self.assertEqual(self.events, ["resume", "next"])

    def test_hidden_app_cannot_advance_other_app(self):
        self.app.visible = False
        self.app.finish_turn()
        self.assertEqual(self.events, [])

    def test_pending_manual_timer_cancelled_before_leaving(self):
        self.app.manual_timer = 7
        self.app.finish_turn()
        self.app.on_hide()
        self.assertEqual(self.events, [("cancel", 7), "resume", "next"])
        self.assertIsNone(self.app.manual_timer)


if __name__ == "__main__":
    unittest.main()
