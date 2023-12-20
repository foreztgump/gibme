# use rich to print test.md to cli
import os
from rich.console import Console
from rich.markdown import Markdown
from rich.pager import Pager
import getpass


script_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(script_dir, "test.md")

console = Console()

with open(file_path) as f:
    markdown = f.read()
try:
    sections = markdown.split("\n\n")

    for section in sections:
        console.print(Markdown(section))
        console.print("Press enter to continue...", end="")
        getpass.getpass(prompt="")
        print("\r" + " " * 30, end="\r")
except KeyboardInterrupt:
    print("\nExiting program.")
