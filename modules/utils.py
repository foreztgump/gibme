import json
import re

from rich.console import Console
from pathlib import Path

# from git import Repo, Blob
from .gtfobins import get_bins
from .lolbas import get_exe
from rich.console import Console
from rich.prompt import Prompt
from .shell_data import reverse_shell, bind_shell, hoax_shell, msfvenom
from .cheatsheet import download_default_notes, walk_directory
from rapidfuzz import process, fuzz, utils as fuzz_utils


def check_init():
    home_dir = Path.home()
    gibnme_dir = home_dir / ".gibme"
    settings_file = home_dir / ".gibme/settings.json"
    if not gibnme_dir.exists():
        initialize_settings()

    if not settings_file.exists():
        initialize_settings()

    return gibnme_dir


def initialize_settings():
    print("Initializing settings...")
    home_dir = Path.home()
    gibnme_dir = home_dir / ".gibme"
    if not gibnme_dir.exists():
        gibnme_dir.mkdir()

    gtfobins_file = gibnme_dir / "gtfobins.json"
    if not gtfobins_file.exists():
        gtfobins_file.touch()
        # update_gtfo(gtfobins_file)

    lolbas_file = gibnme_dir / "lolbas.json"
    if not lolbas_file.exists():
        lolbas_file.touch()
        # update_lolbas(lolbas_file)

    note_dir = gibnme_dir / "default_notes"
    if not note_dir.exists():
        note_dir.mkdir()
        update_notes(note_dir)

    settings_file = gibnme_dir / "settings.json"
    if not settings_file.exists():
        settings_file.touch()
        with open(settings_file, "w") as f:
            data = {
                "gtfobins_file": str(gtfobins_file),
                "lolbas_file": str(lolbas_file),
                "default_notes_dir": str(note_dir),
                "custom_notes_dir": "None",
            }
            json.dump(data, f)

    print("Settings initialized successfully")


# def update_gtfo_local(gibnme_dir: Path):
#     print('Updating GTFOBins...')

#     with tempfile.TemporaryDirectory() as temp_dir:
#         repo_url = "https://github.com/GTFOBins/GTFOBins.github.io.git"

#         repo = Repo.clone_from(repo_url, temp_dir, branch='master', depth=1)

#         tree = repo.head.commit.tree

#         for item in tree:
#             if item.path == '_gtfobins':
#                 for sub_item in item:
#                     if isinstance(sub_item, Blob):
#                         shutil.copy(sub_item.abspath, gibnme_dir / 'gtfobins' / sub_item.name)

#         repo.close()


def update_notes(note_dir: Path):
    if not note_dir.exists():
        note_dir.mkdir()

    download_default_notes(note_dir)


def update_lolbas(lolbas_json_file: Path):
    if not lolbas_json_file.exists():
        initialize_settings()

    lolbas_choice = get_exe()
    data = {"exe": lolbas_choice}

    with lolbas_json_file.open("w") as f:
        json.dump(data, f)


def update_gtfo(gtfo_json_file: Path):
    if not gtfo_json_file.exists():
        initialize_settings()

    gtfo_choice = get_bins()
    data = {"bins": gtfo_choice}

    with gtfo_json_file.open("w") as f:
        json.dump(data, f)


def update_gibme():
    console = Console()
    home_dir = Path.home()
    gibnme_dir = home_dir / ".gibme"
    settings_file = gibnme_dir / "settings.json"
    with open(settings_file, "r") as f:
        settings = json.load(f)
        gtfobins_file = settings["gtfobins_file"]
        lolbas_file = settings["lolbas_file"]

    console.print("[bold cyan]Updating GTFOBins...[/bold cyan]")
    update_gtfo(Path(gtfobins_file))
    console.print("[bold green]GTFOBins updated successfully![/bold green]")

    console.print("[bold cyan]Updating LOLBAS...[/bold cyan]")
    update_lolbas(Path(lolbas_file))
    console.print("[bold green]LOLBAS updated successfully![/bold green]")

    console.print("[bold cyan]Updating default notes...[/bold cyan]")
    update_notes(Path(settings["default_notes_dir"]))
    console.print("[bold green]Default notes updated successfully![/bold green]")
    console.print("[bold green]Gibme updated successfully![/bold green]")


def fuzz_name(
    name: str, type_str: str, home_dir: Path = None, choice_path: Path = None
) -> list:
    if home_dir != None:
        if choice_path == "default":
            settings_file = home_dir / "settings.json"
            with open(settings_file, "r") as settings_file:
                return _get_notes_fuzz(settings_file, "default_notes_dir", name)[0]
        elif choice_path == "custom":
            settings_file = home_dir / "settings.json"
            with open(settings_file, "r") as settings_file:
                return _get_notes_fuzz(settings_file, "custom_notes_dir", name)[0]
        else:
            choice_path = home_dir / f"{type_str}.json"

            with open(choice_path, "r") as f:
                if type_str == "gtfobins":
                    data = json.load(f)
                    choice = data["bins"]
                    return _fuzz_result(name, choice, "ratio")

                elif type_str == "lolbas":
                    data = json.load(f)
                    choice = list(data["exe"].keys())
                    return _fuzz_result(name, choice, "ratio")

    elif type_str == "reverse":
        rs_shell_choice = [shell["name"] for shell in reverse_shell]
        if re.fullmatch("py", name):
            name = name.replace("py", "python")

        if re.fullmatch("ps", name):
            name = name.replace("ps", "powershell")

        return _fuzz_result(name, rs_shell_choice, "token")

    elif type_str == "bind":
        if re.fullmatch("py", name):
            name = name.replace("py", "python3")

        if re.fullmatch("python", name):
            name = name.replace("python", "python3")

        rs_shell_choice = [shell["name"] for shell in bind_shell]
        return _fuzz_result(name, rs_shell_choice, "token")

    elif type_str == "hoax":
        if re.search("ps", name):
            name = name.replace("ps", "PowerShell")

        rs_shell_choice = [shell["name"] for shell in hoax_shell]
        return _fuzz_result(name, rs_shell_choice, "token")

    elif type_str == "msfvenom":
        rs_shell_choice = [shell["name"] for shell in msfvenom]
        return _fuzz_result(name, rs_shell_choice, "token")


def _get_notes_fuzz(settings_file, directory_mode: str, name: str):
    settings = json.load(settings_file)
    default_note_dir = Path(settings[directory_mode])
    choice_data = walk_directory(default_note_dir)
    choice = []
    for folder, files in choice_data.items():
        choice.append(folder)
        choice.extend(iter(files))
    if len(_fuzz_result(name, choice, "token")) > 1:
        return _user_select(_fuzz_result(name, choice, "token"))
    else:
        return _fuzz_result(name, choice, "token")


def _fuzz_result(name: str, choice: list, fuzz_type: str) -> list:
    if fuzz_type == "ratio":
        fuzz_similarity = process.extract(
            name,
            choice,
            scorer=fuzz.ratio,
            limit=10,
            score_cutoff=30,
            processor=fuzz_utils.default_process,
        )
        highest_similarity = max(fuzz_similarity, key=lambda x: x[1])

        if highest_similarity[1] > 90:
            return [highest_similarity]

        console = Console()
        console.print("Did you mean one of these?", style="yellow")

        for name, similarity, index in fuzz_similarity:
            console.print(f"{name}:", style="green", end=" ")
            console.print(f"{format(similarity, '.1f')}% similarity", style="cyan")
        exit(0)

    elif fuzz_type == "token":
        fuzz_similarity = process.extract(
            name,
            choice,
            scorer=fuzz.token_set_ratio,
            limit=10,
            score_cutoff=10,
            processor=fuzz_utils.default_process,
        )

        if high_score_matches := [
            match for match in fuzz_similarity if match[1] >= 70.0
        ]:
            return high_score_matches
        return _user_select(fuzz_similarity)


def _user_select(notes_list) -> list:
    console = Console()
    if len(notes_list) <= 1:
        return [notes_list[0]]  # Return a list containing the single element
    options = {str(i): f"{i}. {n[0]}" for i, n in enumerate(notes_list, start=1)}
    console.print("[bold cyan]Please choose one of the following options:")
    for option in options.values():
        console.print(f"[bold green]{option}")
    selected = Prompt.ask("Your choice:", choices=options.keys())
    return [
        notes_list[int(selected) - 1]
    ]  # Return a list containing the selected element
