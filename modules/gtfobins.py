import httpx
import json

from yaml import load_all, SafeLoader
from bs4 import BeautifulSoup
from pathlib import Path
from .colors import colors
from prettytable import PrettyTable, ALL


def get_bins():
    try:
        url = "https://gtfobins.github.io/"
        with httpx.Client() as client:
            response = client.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            tds = soup.find_all("a", class_="bin-name")
            return [i.text for i in tds]

    except Exception as e:
        print(colors(f"[-] Error: {e}", "red"))
        exit(1)


def list_bins(home_dir: Path):
    settings_file = home_dir / "settings.json"
    with open(settings_file, "r") as f:
        settings = json.load(f)
        bin_list_file = settings["gtfobins_file"]

    with open(bin_list_file, "r") as f:
        _bins_list(f)


def _bins_list(f):
    try:
        data = json.load(f)
        bins = data["bins"]
        table = PrettyTable()
        table.hrules = ALL
        table.field_names = [colors(f"Binaries {i+1}", "green") for i in range(10)]

        # Group the binaries into chunks of 10
        for i in range(0, len(bins), 10):
            row = bins[i : i + 10]
            row += [""] * (10 - len(row))
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


def gtfobins_info(bin_name: str):
    bin_name = bin_name.lower()

    try:
        with httpx.Client() as client:
            _gtfobins_parse_info(client, bin_name)
    except Exception as e:
        print(f"An error occurred: {e}")


def _gtfobins_parse_info(client, bin_name):
    raw_url = f"https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/{bin_name}.md"
    response = client.get(raw_url)
    data = list(load_all(response.text, Loader=SafeLoader))[0]

    for function, codes in data["functions"].items():
        print(colors("Type:", "white"), colors(f"\t\t{function}", "red"))

        for code in codes:
            if description := code.get("description", None):
                print(
                    colors("Description:", "white"),
                    colors(f"\t{description}", "yellow"),
                )

            code_lines = code["code"].split("\n")
            formatted_code = "\n".join("\t\t" + line for line in code_lines)
            print(colors("Code:", "white"), colors(formatted_code, "green"))
