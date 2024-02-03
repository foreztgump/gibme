from __future__ import annotations
from textual.app import App, ComposeResult
from textual.containers import Horizontal
from textual.widget import Widget
from textual.widgets import Footer, Label, Markdown
from textual.binding import Binding
from textual.screen import Screen

from screens.about_screen import About
from screens.gtfo_screen import GTFO
from screens.lol_screen import LOL
from screens.tldr_screen import TLDR
from screens.rev_screen import Rev
from screens.cve_screen import CVE
from screens.cheat_screen import Cheat

class GibmeHeader(Widget):
    
    def compose(self) -> ComposeResult:
        with Horizontal():
            title = Label(self.app.title, id="app_title")
            yield title

class Gibme(Screen):
    BINDINGS = [
        Binding("g", "push_screen('gtfo')", "GTFO_Bin"),
        Binding("l", "push_screen('lol')", "LOLBAS"),
        Binding("r", "push_screen('rev')", "Reverse shell"),
        Binding("t", "push_screen('tldr')", "TLDR"),
        Binding("s", "push_screen('cve')", "CVE Search"),
        Binding("c", "push_screen('cheat')", "Cheat Sheet"),
        Binding("q", "quit", "Quit"),
        Binding("question_mark", "push_screen('about')", "About", key_display="?"),
    ]
    HELP_MARKDOWN = """\
Here are the key bindings for this application:

- **g:** GTFO_Bin
- **l:** LOLBAS
- **r:** Reverse shell
- **t:** TLDR
- **s:** CVE Search
- **c:** Cheat Sheet
- **q:** Quit
- **?:** About
"""
    
    def compose(self) -> ComposeResult:
        yield GibmeHeader()
        yield Footer()
        yield Markdown(self.HELP_MARKDOWN)

    def action_tldr() -> None:
        pass

    def action_quit() -> None:
        pass

class GibmeApp(App[None]):

    CSS_PATH = "gibme.tcss"
    TITLE = "Gibme TUI"

    SCREENS = {
        "about": About,
        "gtfo": GTFO,
        "lol": LOL,
        "tldr": TLDR,
        "rev": Rev,
        "cve": CVE,
        "cheat": Cheat,
    }

    def on_mount(self) -> None:
        self.push_screen(Gibme())
    

if __name__ == "__main__":
    app = GibmeApp()
    app.run()