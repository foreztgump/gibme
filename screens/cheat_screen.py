from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Markdown, Header, Footer

class Cheat(Screen):
    BINDINGS = [("escape,space,q,question_mark", "pop_screen", "Close")]

    COMING_SOON_MARKDOWN = """\
# Pentesting Cheatsheet Screen

This screen will provide a searchable cheatsheet for various pentesting subjects.

## Coming Soon

Stay tuned for more updates!
"""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Markdown(self.COMING_SOON_MARKDOWN)

    async def on_mount(self) -> None:
        """Called when app starts."""
        self.title = "Gibme"
        self.sub_title = "Cheat Sheet"