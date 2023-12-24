import httpx
import json
import platform
import os

from pathlib import Path
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.markdown import Markdown
from rich.table import Table

from rapidfuzz import process, fuzz, utils as fuzz_utils

class tldr:
    def __init__(self, home_dir: Path = None, operating_system: str = None, args: str = None):
        self.console = Console(force_terminal=True, legacy_windows=True)
        self.operating_system = operating_system
        self.args = args
        home_dir_path = Path(home_dir)
        tags_list_path = home_dir_path / "tags.json"


        # Load the tags.json file
        with open(tags_list_path, 'r') as f:
            self.tags_list = json.load(f)

        if self.operating_system is None:
            list_operating_system = ['linux', 'common']
        else:
            list_operating_system = [self.operating_system]

        if os_data := next(
            (item for item in self.tags_list if any(os in item.keys() for os in list_operating_system)), None
        ):
            self.tags = [file['tag'] for os in list_operating_system for file in os_data.get(os, [])]
            self.file_names = [file['filename'] for os in list_operating_system for file in os_data.get(os, [])]
        else:
            self.tags = []
            self.file_names = []

    def run(self):
        found = self.search_tldr() if len(self.args.split(" ")) == 1 else None
        if not found:
            found = self.fuzz_search()

        if not found:
            self.console.print("\n[bold red]The command is not found.")
            return None

        get_tldr = self.get_tldr(found)
        if get_tldr is None:
            self.console.print("\n[bold red]Error: tldr is not found. Check your connection or try again later.")
        else:
            self.print_tldr(get_tldr)

    def get_tldr(self, file_name: str):
        base_url = "https://raw.githubusercontent.com/tldr-pages/tldr/master/pages/"
        os_list = [self.operating_system] if isinstance(self.operating_system, str) else (self.operating_system or ["linux", "common"])

        with httpx.Client() as client:
            for os in os_list:
                url = f"{base_url}{os}/{file_name}"
                response = client.get(url)
                if response.status_code == 200:
                    return response.text
        return None

    def print_tldr(self, markdown: str):
        try:
            if "PAGER" not in os.environ and platform.system() != "Windows":
                os.environ["PAGER"] = "less -R"
            with self.console.pager(styles=True):
                self.console.print(Markdown(markdown))
        except KeyboardInterrupt:
            self.console.print("\n[bold red]Exiting program.")

    def search_tldr(self):
        names_with_ext = {os.path.splitext(filename)[0]: filename for filename in self.file_names}
        return names_with_ext.get(self.args, None)
    
    def fuzz_search(self):
        results_filenames = []
        for os_data in self.tags_list:
            if self.operating_system and self.operating_system in os_data:
                for file_dict in os_data.get(self.operating_system, []):
                    file_tags = file_dict.get('tag', '')
                    score = process.extractOne(self.args, [file_tags], scorer=fuzz.token_set_ratio ,processor=fuzz_utils.default_process)
                    if score[1] > 90:
                        results_filenames.append(file_dict['filename'])
            elif 'common' in os_data:
                for file_dict in os_data.get('common', []):
                    file_tags = file_dict.get('tag', '')
                    score = process.extractOne(self.args, [file_tags], scorer=fuzz.token_set_ratio ,processor=fuzz_utils.default_process)
                    if score[1] > 90:
                        results_filenames.append(file_dict['filename'])

        if results_filenames: 
            if len(results_filenames) > 1:
                return self.user_select(results_filenames)[0]
            else: 
                return results_filenames[0] 
        return None

    def user_select(self, choice_list) -> list:
        self.console.print("[bold cyan]Please choose one of the following options:")
        if len(choice_list) <= 1:
            return [choice_list[0]]  # Return a list containing the single element
        options = {str(i): f"{i}. {n[:-3]}" for i, n in enumerate(choice_list, start=1)}  # Strip .md from each filename

        if len(options) > 70:
            if Prompt.ask("The result is over 70. Do you want to continue?", choices=["yes", "no"], default="no") == "no":
                return []

        table = Table(show_header=False, padding=(0, 2))
        for i in range(0, len(options), 3):  # Adjust the range step to change the number of columns
            table.add_row(*[options.get(str(j), "") for j in range(i+1, i+4)])

        self.console.print(table)

        selected = Prompt.ask("Your choice:", choices=options.keys())
        return [
            choice_list[int(selected) - 1]
        ]