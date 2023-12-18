import httpx
import json

from yaml import load_all, SafeLoader
from bs4 import BeautifulSoup
from pathlib import Path
from .colors import colors
from prettytable import PrettyTable, ALL


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
        print(colors(f"[-] Error: {e}", "red"))
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
        table = PrettyTable()
        table.hrules = ALL
        table.field_names = [colors(f"EXE {i+1}", "green") for i in range(5)]

        for i in range(0, len(exe), 5):
            row = exe[i : i + 5]
            row += [""] * (5 - len(row))
            table.add_row(row)
        print(table)
    except Exception as e:
        if isinstance(e, json.JSONDecodeError):
            print(
                colors(
                    "[-] Error: Invalid JSON file - Please run 'gibme -update' to update modules",
                    "red",
                )
            )


def lolbas_info(exe_name: str):
    exe_name = exe_name.lower()

    try:
        with httpx.Client() as client:
            _lolbas_parse_info(client, exe_name)
    except Exception as e:
        print(f"An error occurred: {e}")


def _lolbas_parse_info(client, exe_name):
    raw_url = f"https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS-Project.github.io/master/_lolbas/{exe_name}.md"
    response = client.get(raw_url)
    data = list(load_all(response.text, Loader=SafeLoader))[0]

    print(colors("Name:", "white"), colors(f"\t\t{data['Name']}", "red"))
    print(colors("Description:", "white"), colors(f"\t{data['Description']}", "yellow"))
    print(colors("Author:", "white"), colors(f"\t\t{data['Author']}", "green"))
    print(colors("Created:", "white"), colors(f"\t\t{data['Created']}", "green"))

    for command in data["Commands"]:
        print(colors("Command:", "white"), colors(f"\t{command['Command']}", "cyan"))
        print(
            colors("Description:", "white"),
            colors(f"\t{command['Description']}", "yellow"),
        )
        print(colors("Usecase:", "white"), colors(f"\t{command['Usecase']}", "yellow"))
        print(
            colors("Category:", "white"), colors(f"\t{command['Category']}", "yellow")
        )
        print(
            colors("Privileges:", "white"),
            colors(f"\t{command['Privileges']}", "yellow"),
        )
        print(colors("MitreID:", "white"), colors(f"\t{command['MitreID']}", "yellow"))
        print(
            colors("OperatingSystem:", "white"),
            colors(f"\t{command['OperatingSystem']}", "yellow"),
        )

    for path in data["Full_Path"]:
        print(colors("Path:", "white"), colors(f"\t{path['Path']}", "green"))

    for code in data["Code_Sample"]:
        print(colors("Code:", "white"), colors(f"\t{code['Code']}", "green"))

    for detection in data["Detection"]:
        print(colors("Sigma:", "white"), colors(f"\t{detection['Sigma']}", "green"))

    for resource in data["Resources"]:
        print(colors("Link:", "white"), colors(f"\t{resource['Link']}", "green"))

    for acknowledgement in data["Acknowledgement"]:
        print(
            colors("Person:", "white"),
            colors(f"\t{acknowledgement['Person']}", "green"),
        )
        print(
            colors("Handle:", "white"),
            colors(f"\t{acknowledgement['Handle']}", "green"),
        )
