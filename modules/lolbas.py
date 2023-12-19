import httpx
import json

from yaml import load_all, SafeLoader
from bs4 import BeautifulSoup
from pathlib import Path
from rich import print
from rich.table import Table
from rich.console import Console


def get_exe():
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
        exit(1)


def list_exe(home_dir: Path):
    settings_file = home_dir / "settings.json"
    with open(settings_file, "r") as f:
        settings = json.load(f)
        exe_list_file = settings["lolbas_file"]

    with open(exe_list_file, "r") as f:
        _exe_list(f)


def _exe_list(f):
    try:
        data = json.load(f)
        exe = list(data["exe"].keys())
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("EXE 1", style="green")
        table.add_column("EXE 2", style="green")
        table.add_column("EXE 3", style="green")
        table.add_column("EXE 4", style="green")
        table.add_column("EXE 5", style="green")

        for i in range(0, len(exe), 5):
            row = exe[i : i + 5]
            row += [""] * (5 - len(row))
            table.add_row(*row)
        console = Console()
        console.print(table)
    except Exception as e:
        if isinstance(e, json.JSONDecodeError):
            console = Console()
            console.print(
                "[-] Error: Invalid JSON file - Please run 'gibme -update' to update modules",
                style="red",
            )


def lolbas_info(exe_name: str):
    exe_name = exe_name.lower()

    try:
        with httpx.Client() as client:
            _lolbas_parse_info(client, exe_name)
    except Exception as e:
        console = Console()
        console.print(f"An error occurred: {e}")


def _lolbas_parse_info(client, exe_name):
    raw_url = f"https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS-Project.github.io/master/_lolbas/{exe_name}.md"
    response = client.get(raw_url)
    data = list(load_all(response.text, Loader=SafeLoader))[0]

    console = Console()
    console.print("Name:", style="white", end="\t\t")
    console.print(data["Name"], style="red")
    console.print("Description:", style="white", end="\t")
    console.print(data["Description"], style="yellow")
    console.print("Author:", style="white", end="\t\t")
    console.print(data["Author"], style="green")
    console.print("Created:", style="white", end="\t\t")
    console.print(data["Created"], style="green")

    for command in data["Commands"]:
        console.print("Command:", style="white", end="\t")
        console.print(command["Command"], style="cyan")
        console.print("Description:", style="white", end="\t")
        console.print(command["Description"], style="yellow")
        console.print("Usecase:", style="white", end="\t\t")
        console.print(command["Usecase"], style="yellow")
        console.print("Category:", style="white", end="\t")
        console.print(command["Category"], style="yellow")
        console.print("Privileges:", style="white", end="\t")
        console.print(command["Privileges"], style="yellow")
        console.print("MitreID:", style="white", end="\t")
        console.print(command["MitreID"], style="yellow")
        console.print("OperatingSystem:", style="white", end="\t")
        console.print(command["OperatingSystem"], style="yellow")

    for path in data["Full_Path"]:
        console.print("Path:", style="white", end="\t\t")
        console.print(path["Path"], style="green")

    for code in data["Code_Sample"]:
        console.print("Code:", style="white", end="\t\t")
        console.print(code["Code"], style="green")

    for detection in data["Detection"]:
        console.print("Sigma:", style="white", end="\t\t")
        console.print(detection["Sigma"], style="green")

    for resource in data["Resources"]:
        console.print("Link:", style="white", end="\t\t")
        console.print(resource["Link"], style="green")

    for acknowledgement in data["Acknowledgement"]:
        console.print("Person:", style="white", end="\t")
        console.print(acknowledgement["Person"], style="green")
        console.print("Handle:", style="white", end="\t")
        console.print(acknowledgement["Handle"], style="green")
