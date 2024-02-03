from textual.screen import Screen
from textual.app import ComposeResult
from textual.widgets import Markdown, Header, Footer

class About(Screen):
    BINDINGS = [("escape,space,q,question_mark", "pop_screen", "Close")]

    ABOUT_MARKDOWN = """\
# About Gibme

Gibme is a tool developed by [foreztgump (https://github.com/foreztgump)](https://github.com/foreztgump).

## Version

The current version of Gibme is 0.7.14

## Project Page

For more information about Gibme, visit the [project page (https://github.com/foreztgump/gibme)](https://github.com/foreztgump/gibme).
"""

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Markdown(self.ABOUT_MARKDOWN)

    async def on_mount(self) -> None:
        """Called when app starts."""
        self.title = "Gibme"
        self.sub_title = "Help"