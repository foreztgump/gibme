import httpx
from textual import work
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Markdown, Input, Header, Footer
from textual.containers import VerticalScroll
from yaml import load_all, SafeLoader
from bs4 import BeautifulSoup
from rapidfuzz import process, fuzz, utils as fuzz_utils

class LOL(Screen):

    BINDINGS = [("escape", "pop_screen", "Close")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Input(placeholder="Search for LOL Bins")
        with VerticalScroll(id="results-container"):
            yield Markdown(id="results")

    async def on_mount(self) -> None:
        """Called when app starts."""
        self.query_one(Input).focus()
        self.title = "Gibme"
        self.sub_title = "LOL Bins"
        self.exe_list = await self.get_exe()

    async def on_input_changed(self, message: Input.Changed) -> None:
        """A coroutine to handle a text changed message."""
        if message.value:
            fuzz_result = await self.fuzz_exe(message.value)
            if len(fuzz_result) == 0:
                self.query_one("#results", Markdown).update(f"**Not Found**")
            elif len(fuzz_result) == 1:
                if '.exe' in fuzz_result[0]:
                    exe_name = fuzz_result[0].replace(".exe", "")
                self.lolbas_info(exe_name)
            else:
                self.query_one("#results", Markdown).update(self.fuzz_result_markdown(fuzz_result))
        else:
            # Clear the results
            self.query_one("#results", Markdown).update("")

    @work(exclusive=True)
    async def lolbas_info(self, exe_name: str) -> None:
        self.query_one("#results", Markdown).update(f'**{exe_name}**')
        raw_url = f"https://raw.githubusercontent.com/LOLBAS-Project/LOLBAS/master/yml/OSBinaries/{exe_name}.yml"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(raw_url)
                markdown = self.make_word_markdown(response)
                self.query_one("#results", Markdown).update(markdown)
            except Exception:
                self.query_one("#results", Markdown).update(response.text)

    def make_word_markdown(self, response: httpx.Response) -> str:
        """Make a markdown string for a word."""
        if response.status_code == 404:
            return "### Not Found"

        data = list(load_all(response.text, Loader=SafeLoader))[0]
        markdown = f"# **{data['Name']}**\n\n"
        markdown += f"**Description:** *{data['Description']}*\n\n"
        markdown += f"**Author:** *{data['Author']}*\n\n"
        markdown += f"**Created:** *{data['Created']}*\n\n"

        for command in data["Commands"]:
            markdown += f"- **Command:**\n\n```\n{command['Command']}\n```\n\n"
            markdown += f"**Description:** *{command['Description']}*\n\n"
            markdown += f"**Usecase:** *{command['Usecase']}*\n\n"
            markdown += f"**Category:** *{command['Category']}*\n\n"
            markdown += f"**Privileges:** *{command['Privileges']}*\n\n"
            markdown += f"**MitreID:** *{command['MitreID']}*\n\n"
            markdown += f"**OperatingSystem:** *{command['OperatingSystem']}*\n\n"
            markdown += "\n---\n\n"

        return markdown
    
    async def get_exe(self) -> list:
        URL = "https://lolbas-project.github.io/"
        exe = {}
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(URL)
                soup = BeautifulSoup(response.text, "lxml")
                tds = soup.find_all("a", class_="bin-name")
                for i in tds:
                    exe[i.text] = i["href"][8:][:-1]

                return exe
            except Exception as e:
                self.query_one("#results", Markdown).update(f"**Check your internet connection - Error: Cound not connect to https://lolbas-project.github.io/ error: {e}**")

    async def fuzz_exe(self, exe_name: str) -> list:
        if '.exe' not in exe_name:
            exe_name = f'{exe_name}.exe'
        choices = list(self.exe_list.keys())
        results = process.extract(
            exe_name, 
            choices, 
            scorer=fuzz.ratio,
            limit=10,
            score_cutoff=70,
            processor=fuzz_utils.default_process,)
        if results:
            highest_similarity = max(results, key=lambda x: x[1])
            if highest_similarity[1] > 90:
                return [highest_similarity[0]]
            else:
                return results
        else:
            return results

    def fuzz_result_markdown(self, results: list) -> str:
        markdown = ""
        for result in results:
            markdown += f"**{result[0]}**\n\n"
        return markdown