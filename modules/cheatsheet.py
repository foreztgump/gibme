import httpx
import asyncio

import os
from pathlib import Path
from rich.console import Console
from rich.markdown import Markdown

default_notes_links = [
    {
      "name": "Active Directory Attack.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Active%20Directory%20Attack.md"
    },
    {
      "name": "Cloud - AWS Pentest.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Cloud%20-%20AWS%20Pentest.md"
    },
    {
      "name": "Cloud - Azure Pentest.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Cloud%20-%20Azure%20Pentest.md"
    },
    {
      "name": "Cobalt Strike - Cheatsheet.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Cobalt%20Strike%20-%20Cheatsheet.md"
    },
    {
      "name": "Linux - Evasion.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Evasion.md"
    },
    {
      "name": "Linux - Persistence.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Persistence.md"
    },
    {
      "name": "Linux - Privilege Escalation.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Linux%20-%20Privilege%20Escalation.md"
    },
    {
      "name": "Metasploit - Cheatsheet.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Metasploit%20-%20Cheatsheet.md"
    },
    {
      "name": "Methodology and enumeration.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Methodology%20and%20enumeration.md"
    },
    {
      "name": "Network Pivoting Techniques.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Network%20Pivoting%20Techniques.md"
    },
    {
      "name": "Network Discovery.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Network%20Discovery.md"
    },
    {
      "name": "Reverse Shell Cheatsheet.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Reverse%20Shell%20Cheatsheet.md"
    },
    {
      "name": "Subdomains Enumeration.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Subdomains%20Enumeration.md"
    },
    {
      "name": "Windows - AMSI Bypass.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20AMSI%20Bypass.md"
    },
    {
      "name": "Windows - DPAPI.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20DPAPI.md"
    },
    {
      "name": "Windows - Download and Execute.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Download%20and%20Execute.md"
    },
    {
      "name": "Windows - Mimikatz.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Mimikatz.md"
    },
    {
      "name": "Windows - Persistence.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Persistence.md"
    },
    {
      "name": "Windows - Privilege Escalation.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Privilege%20Escalation.md"
    },
    {
      "name": "Using credentials.md",
      "link": "https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Windows%20-%20Using%20credentials.md"
    }
]

async def download_file(url: str, dest: Path):
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        r.raise_for_status()
        dest.write_text(r.text)

async def get_notes(note_dir: Path, urls: list):
    tasks = []
    for url in urls:
        filename = url.rsplit('/', 1)[-1]
        dest = note_dir / filename
        tasks.append(download_file(url, dest))
    await asyncio.gather(*tasks)

def download_default_notes(note_dir: Path, urls: list):
    asyncio.run(get_notes(note_dir, urls))

def print_note(note_dir: Path, note_name: str):
    note_file = note_dir / note_name
    console = Console(force_terminal=True, legacy_windows=True)

    markdown = Path(note_file).read_text()
    try:
        with console.pager(styles=True):
            console.print(Markdown(markdown))
    except KeyboardInterrupt:
        print("\nExiting program.")

def list_notes(note_dir: Path):
    pass