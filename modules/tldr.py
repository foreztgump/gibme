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

        if os_data := next(
            (item for item in self.tags_list if self.operating_system in item), None
        ):
            self.tags = [item['tag'] for item in os_data[self.operating_system]]
            self.file_names = [item['filename'] for item in os_data[self.operating_system]]
        else:
            self.tags = []
            self.file_names = []

    # this function will run on default
    def run(self):
        found = self.search_tldr()
        if not found:
            found = self.fuzz_search()[0]
        get_tldr = self.get_tldr(found)
        if get_tldr is None:
            self.console.print("\n[bold red]Error: tldr is not found. Check your connection or try again later.")
        else:
            self.print_tldr(get_tldr)

    def get_tldr(self, file_name: str):
        base_url = "https://raw.githubusercontent.com/tldr-pages/tldr/master/pages/"
        os_list = [self.operating_system, "common"] if self.operating_system else ["linux", "common"]

        with httpx.Client() as client:
            for os in os_list:
                response = client.get(f"{base_url}{os}/{file_name}")
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
        names_without_ext = [os.path.splitext(filename)[0] for filename in self.file_names]
        return f"{self.args}.md" if self.args in names_without_ext else None
    
    def fuzz_search(self):
        if not self.operating_system:
            self.operating_system = 'linux'
        results_filenames = []
        for os_data in self.tags_list:
            if self.operating_system in os_data or 'common' in os_data:
                for file_dict in (os_data.get(self.operating_system, []) if self.operating_system else []) + os_data.get('common', []):
                    file_tags = file_dict.get('tag', '')
                    score = process.extractOne(self.args, [file_tags], scorer=fuzz.token_set_ratio ,processor=fuzz_utils.default_process)
                    if score[1] > 90:
                        results_filenames.append(file_dict['filename'])

        if results_filenames: 
            if len(results_filenames) > 1:
                return self.user_select(results_filenames)
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