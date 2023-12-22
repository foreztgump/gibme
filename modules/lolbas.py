import httpx
import json
import re
import sys

from yaml import load_all, SafeLoader
from bs4 import BeautifulSoup
from pathlib import Path
from rich.table import Table
from rich.console import Console
from rich.text import Text
from rich.panel import Panel


def get_exe():
    """
    Retrieves a dictionary of executable names and their corresponding URLs from the LOLBAS website.

    Returns:
        dict: A dictionary containing executable names as keys and their corresponding URLs as values.
    """
    try:
        URL = "https://lolbas-project.github.io/"
        exe = {}
        with httpx.Client() as client:
            response = client.get(URL)
            soup = BeautifulSoup(response.text, "lxml")
            tds = soup.find_all("a", class_="bin-name")
            for i in tds:
                exe[i.text] = i["href"][8:][:-1]

            return exe

    except Exception as e:
        console = Console()
        console.print(f"[-] Error: {e}", style="red")
        sys.exit(0)


def list_exe(home_dir: Path):
    """
    Lists the executables from the LOLBAS file specified in the settings.

    Args:
        home_dir (Path): The home directory where the settings file is located.

    Returns:
        None
    """
    settings_file = home_dir / "settings.json"
    with open(settings_file, "r") as f:
        settings = json.load(f)
        exe_list_file = settings["lolbas_file"]

    with open(exe_list_file, "r") as f:
        _exe_list(f)


def _exe_list(f):
    """
    Display a table of executable names from a JSON file.

    Args:
        f (file): The JSON file to read from.

    Raises:
        json.JSONDecodeError: If the JSON file is invalid.

    """
    try:
        data = json.load(f)
        exe = list(data["exe"].keys())
        table = Table(
            show_header=False, header_style="bold magenta", title="\nExecutable List"
        )
        for _ in range(5):
            table.add_column(justify="center")

        for i in range(0, len(exe), 5):
            row = exe[i : i + 5]
            row += [""] * (5 - len(row))
            table.add_row(*[Text(x, style="green") for x in row])
        console = Console()
        console.print(table)
    except Exception as e:
        if isinstance(e, json.JSONDecodeError):
            console = Console()
            console.print(
                "[bold red][-] Error: Invalid JSON file - Please run 'gibme -update' to update modules",
            )


def lolbas_info(exe_name: str, home_dir: Path):
    """
    Retrieve information about a LOLBAS (Living Off The Land Binaries and Scripts) executable.

    Args:
        exe_name (str): The name of the LOLBAS executable.
        home_dir (Path): The path to the home directory.

    Raises:
        SystemExit: If the specified executable is not in the list of executables.

    Returns:
        None
    """
    with open(home_dir / "lolbas.json", "r") as f:
        data = json.load(f)
        exe = data["exe"]
        if exe_name not in exe:
            console = Console()
            console.print(
                f"[-] Error: {exe_name} is not in the list of executables. Please run 'gibme -update' to update modules",
                style="bold red",
            )
            sys.exit(0)
        else:
            exe_name = exe[exe_name]
            if "OtherMSBinaries" not in exe_name:
                exe_name = f"OS{exe_name}"

    try:
        with httpx.Client() as client:
            _lolbas_parse_info(client, exe_name)
    except Exception as e:
        console = Console()
        console.print(f"An error occurred: {e}")


def _lolbas_parse_info(client, exe_name):
    """
    Parses LOLBAS information for a given executable.

    Args:
        client (object): The HTTP client used to make the request.
        exe_name (str): The name of the executable.

    Returns:
        None
    """
    raw_url = f"https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS/master/yml/{exe_name}.yml"
    response = client.get(raw_url)
    data = list(load_all(response.text, Loader=SafeLoader))[0]

    console = Console()

    console.print(Panel(Text(data["Name"], style="bold blue"), expand=False))

    console.print("\n[bold underline cyan]General Information:[/bold underline cyan]")
    console.print(
        f"  Description: [spring_green3]{data['Description']}[/spring_green3]"
    )
    console.print(f"  Author: [spring_green3]{data['Author']}[/spring_green3]")
    console.print(f"  Created: [spring_green3]{str(data['Created'])}[/spring_green3]")

    for i, command in enumerate(data["Commands"], start=1):
        console.print(f"\n[bold underline cyan]Command {i}:[/bold underline cyan]")
        for key, value in command.items():
            if key in ["Command", "Code", "Path"]:
                console.print(f"  {key}: [bold yellow]{value}[/bold yellow]")
            else:
                value = re.sub(
                    r'"(.*?)"', r"[bold magenta]\1[/bold magenta]", str(value)
                )
                console.print(f"  {key}: [spring_green3]{value}[/spring_green3]")

    for section in [
        "Full_Path",
        "Code_Sample",
        "Detection",
        "Resources",
        "Acknowledgement",
    ]:
        if section in data:
            for i, item in enumerate(data[section], start=1):
                console.print(
                    f"\n[bold underline cyan]{section} {i}:[/bold underline cyan]"
                )
                for key, value in item.items():
                    if key in ["Command", "Code", "Path"]:
                        console.print(f"  {key}: [bold yellow]{value}[/bold yellow]")
                    elif key == "IOC":
                        console.print(f"  {key}: [bold red]{value}[/bold red]")
                    else:
                        value = re.sub(
                            r'"(.*?)"', r"[bold magenta]\1[/bold magenta]", str(value)
                        )
                        console.print(
                            f"  {key}: [spring_green3]{value}[/spring_green3]"
                        )
