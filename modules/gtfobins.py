import httpx
import json
import sys

from yaml import load_all, SafeLoader
from bs4 import BeautifulSoup
from pathlib import Path
from rich.table import Table
from rich.console import Console
from rich.text import Text


def get_bins():
    """
    Retrieves a list of binary names from the gtfobins website.

    Returns:
        list: A list of binary names.
    """
    try:
        url = "https://gtfobins.github.io/"
        with httpx.Client() as client:
            response = client.get(url)
            soup = BeautifulSoup(response.text, "lxml")
            tds = soup.find_all("a", class_="bin-name")
            return [i.text for i in tds]

    except Exception as e:
        console = Console()
        console.print(f"[-] Error: {e}", style="bold red")
        sys.exit(0)


def list_bins(home_dir: Path):
    """
    Lists the bins from the gtfobins file specified in the settings.

    Args:
        home_dir (Path): The home directory path.

    Returns:
        None
    """
    settings_file = home_dir / "settings.json"
    with open(settings_file, "r") as f:
        settings = json.load(f)
        bin_list_file = settings["gtfobins_file"]

    with open(bin_list_file, "r") as f:
        _bins_list(f)


def _bins_list(f):
    """
    Display a table of binaries from a JSON file.

    Args:
        f (file): The JSON file containing the binary data.

    Raises:
        json.JSONDecodeError: If the JSON file is invalid.

    """
    try:
        data = json.load(f)
        bins = data["bins"]
        table = Table(
            show_header=False, header_style="bold magenta", title="\nBinaries List"
        )
        for _ in range(7):
            table.add_column(justify="center")

        for i in range(0, len(bins), 8):
            row = bins[i : i + 8]
            row += [""] * (8 - len(row))
            table.add_row(*[Text(x, style="green") for x in row])
        console = Console()
        console.print(table)
    except Exception as e:
        if isinstance(e, json.JSONDecodeError):
            console = Console()
            console.print(
                "[-] Error: Invalid JSON file - Please run 'gibme -update' to update modules",
                style="bold red",
            )


def gtfobins_info(bin_name: str):
    """
    Retrieves information about a specific binary from the GTFOBins website.

    Args:
        bin_name (str): The name of the binary to retrieve information for.

    Raises:
        Exception: If an error occurs during the retrieval process.

    Returns:
        None
    """
    bin_name = bin_name.lower()

    try:
        with httpx.Client() as client:
            _gtfobins_parse_info(client, bin_name)
    except Exception as e:
        print(f"An error occurred: {e}")


def _gtfobins_parse_info(client, bin_name):
    """
    Parse information about a specific GTFOBin.

    Args:
        client (object): The HTTP client used to make the request.
        bin_name (str): The name of the GTFOBin.

    Returns:
        None
    """
    raw_url = f"https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/{bin_name}.md"
    response = client.get(raw_url)
    data = list(load_all(response.text, Loader=SafeLoader))[0]

    console = Console()
    for function, codes in data["functions"].items():
        console.print(f"[white]Type:[/white] [red]\t\t{function}[/red]")

        for code in codes:
            if description := code.get("description", None):
                console.print(
                    f"[white]Description:[/white] [yellow]\t{description}[/yellow]"
                )

            code_lines = code["code"].split("\n")
            formatted_code = "\n".join("\t\t" + line for line in code_lines)
            console.print(f"[white]Code:[/white] [green]{formatted_code}[/green]")
