import httpx
import asyncio
import json
import platform
import os
import sys

from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown
from rich.tree import Tree

default_notes_links = [
    {
        "name": "Active Directory Attack.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Active%20Directory%20Attack.md",
    },
    {
        "name": "Cloud - AWS Pentest.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Cloud%20-%20AWS%20Pentest.md",
    },
    {
        "name": "Cloud - Azure Pentest.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Cloud%20-%20Azure%20Pentest.md",
    },
    {
        "name": "Cobalt Strike - Cheatsheet.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Cobalt%20Strike%20-%20Cheatsheet.md",
    },
    {
        "name": "Linux - Evasion.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Linux%20-%20Evasion.md",
    },
    {
        "name": "Linux - Persistence.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Linux%20-%20Persistence.md",
    },
    {
        "name": "Linux - Privilege Escalation.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md",
    },
    {
        "name": "Metasploit - Cheatsheet.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Metasploit%20-%20Cheatsheet.md",
    },
    {
        "name": "Methodology and enumeration.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Methodology%20and%20enumeration.md",
    },
    {
        "name": "Network Pivoting Techniques.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Network%20Pivoting%20Techniques.md",
    },
    {
        "name": "Network Discovery.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Network%20Discovery.md",
    },
    {
        "name": "Reverse Shell Cheatsheet.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md",
    },
    {
        "name": "Subdomains Enumeration.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Subdomains%20Enumeration.md",
    },
    {
        "name": "Windows - AMSI Bypass.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Windows%20-%20AMSI%20Bypass.md",
    },
    {
        "name": "Windows - DPAPI.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Windows%20-%20DPAPI.md",
    },
    {
        "name": "Windows - Download and Execute.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Windows%20-%20Download%20and%20Execute.md",
    },
    {
        "name": "Windows - Mimikatz.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Windows%20-%20Mimikatz.md",
    },
    {
        "name": "Windows - Persistence.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Windows%20-%20Persistence.md",
    },
    {
        "name": "Windows - Privilege Escalation.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md",
    },
    {
        "name": "Using credentials.md",
        "link": "https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/master/Methodology%20and%20Resources/Windows%20-%20Using%20credentials.md",
    },
]


async def download_file(url: str, dest: Path):
    async with httpx.AsyncClient() as session:
        response = await session.get(url)
        dest.write_text(response.text, encoding="utf-8")


async def get_notes(note_dir: Path, notes: list):
    tasks = []
    for note in notes:
        url = note["link"]
        filename = note["name"]
        dest = note_dir / filename
        tasks.append(download_file(url, dest))
    await asyncio.gather(*tasks)


def download_default_notes(note_dir: Path):
    asyncio.run(get_notes(note_dir, default_notes_links))


def print_note(home_dir: Path, note_name: str, note_mode: str):
    settings_file = home_dir / "settings.json"
    with settings_file.open() as f:
        settings = json.load(f)
        default_note_dir = Path(settings["default_notes_dir"])
        custom_notes_dir = settings["custom_notes_dir"]

    if note_mode == "default":
        note_file_path = next(
            (
                Path(root) / note_name
                for root, dirs, files in os.walk(default_note_dir)
                if note_name in files
            ),
            None,
        )
    elif note_mode == "custom":
        note_file_path = next(
            (
                Path(root) / note_name
                for root, dirs, files in os.walk(custom_notes_dir)
                if note_name in files
            ),
            None,
        )

    if not note_file_path:
        console = Console()
        console.print(
            f"[bold red]Error: [bold]'{note_name}'[bold red] not found in '{note_mode}' directory."
        )
        sys.exit(0)

    console = Console(force_terminal=True, legacy_windows=True)

    print(note_file_path)
    markdown = Path(note_file_path).read_text(encoding="utf-8")
    try:
        # Set the PAGER environment variable to less -R for rich markdown support
        if "PAGER" not in os.environ and platform.system() != "Windows":
            os.environ["PAGER"] = "less -R"
        with console.pager(styles=True):
            console.print(Markdown(markdown))
    except KeyboardInterrupt:
        console.print("\n[bold red]Exiting program.")


def list_notes(home_dir: Path):
    # get default_notes_dir and custom_notes_dir from settings.json
    settings_file = home_dir / "settings.json"
    with settings_file.open() as f:
        settings = json.load(f)
        default_note_dir = Path(settings["default_notes_dir"])
        custom_notes_dir = settings["custom_notes_dir"]

    default_tree = _get_notes_tree(
        default_note_dir, "[bold magenta]Default Directory ("
    )
    # Check if custom_notes_dir is not empty
    if custom_notes_dir:
        custom_notes_dir = Path(custom_notes_dir)

        custom_tree = _get_notes_tree(
            custom_notes_dir, "[bold magenta]Custom Directory ("
        )
        # Print the custom tree
        console = Console()
        console.print(custom_tree)

    # Print the default tree
    console = Console()
    console.print(default_tree)


def _get_notes_tree(directory: Path, header_style: str) -> Tree:
    # Walk the custom directory and add all the folders and files to the tree
    custom_directory_dict = walk_directory(directory)
    result = Tree(f"{header_style}{directory})")
    for folder, files in custom_directory_dict.items():
        folder_node = result.add(f"[green]{folder}")
        for file in files:
            folder_node.add(f"[blue]{file}")
    return result


def walk_directory(directory: Path) -> dict:
    return {Path(root).name: files for root, dirs, files in os.walk(directory)}
