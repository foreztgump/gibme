import httpx
from textual import work
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Markdown, Input, Header, Footer
from textual.containers import VerticalScroll
from yaml import load_all, SafeLoader
from bs4 import BeautifulSoup
from rapidfuzz import process, fuzz, utils as fuzz_utils

class GTFO(Screen):

    BINDINGS = [("escape", "pop_screen", "Close")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Input(placeholder="Search for GTFO Bins")
        with VerticalScroll(id="results-container"):
            yield Markdown(id="results")

    async def on_mount(self) -> None:
        """Called when app starts."""
        self.query_one(Input).focus()
        self.title = "Gibme"
        self.sub_title = "GTFO Bins"
        self.bins_list = await self.get_bins()

    async def on_input_changed(self, message: Input.Changed) -> None:
        """A coroutine to handle a text changed message."""
        if message.value:
            # self.gtfobins_info(message.value)
            fuzz_result = await self.fuzz_bin(message.value)
            if len(fuzz_result) == 0:
                self.query_one("#results", Markdown).update(f"**Not Found**")
            elif len(fuzz_result) == 1 and len(fuzz_result[0]) == 1:
                self.gtfobins_info(fuzz_result[0][0])
            else:
                self.query_one("#results", Markdown).update(self.fuzz_result_markdown(fuzz_result))
        else:
            # Clear the results
            self.query_one("#results", Markdown).update("")

    @work(exclusive=True)
    async def gtfobins_info(self, bin_name: str) -> None:
        bin_name = bin_name.lower()
        raw_url = f"https://raw.githubusercontent.com/GTFOBins/GTFOBins.github.io/master/_gtfobins/{bin_name}.md"

        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(raw_url)

            except Exception:
                self.query_one("#results", Markdown).update(response.text)

        if bin_name == self.query_one(Input).value:
            markdown = self.make_word_markdown(response, bin_name)
            self.query_one("#results", Markdown).update(markdown)

    def make_word_markdown(self, response: httpx.Response, bin_name: str) -> str:
        """Make a markdown string for a word."""
        if response.status_code == 404:
            return "### Not Found"

        data = list(load_all(response.text, Loader=SafeLoader))[0]
        markdown = f"# **{bin_name}**\n\n"
        for function, details in data["functions"].items():
            markdown += f"- **{function}**\n\n"
            for detail in details:
                if "description" in detail:
                    formatted_description = detail["description"]
                    markdown += f"**Description:** *{formatted_description}*\n\n"
                if "code" in detail:
                    formatted_code = detail["code"].split('\n')
                    markdown += "```\n"
                    for line in formatted_code:
                        markdown += f"{line}\n"
                    markdown += "```\n\n"
            markdown += "\n---\n\n"
        return markdown
    
    async def get_bins(self):
        URL = "https://gtfobins.github.io/"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(URL)
                soup = BeautifulSoup(response.text, "lxml")
                tds = soup.find_all("a", class_="bin-name")
                return [i.text for i in tds]

            except Exception as e:
                self.query_one("#results", Markdown).update(f"**Check your internet connection - Error: {e}**")

    async def fuzz_bin(self, bin_name: str) -> list:
        choices = list(self.bins_list)
        bin_name = bin_name.lower()
        results = process.extract(
                bin_name, 
                choices, 
                scorer=fuzz.ratio,
                limit=10,
                score_cutoff=70,
                processor=fuzz_utils.default_process,)
        if results:
            highest_similarity = max(results, key=lambda x: x[1])
            if highest_similarity[1] > 90:
                return [(highest_similarity[0],)]
            else:
                return results
        else:
            return results
            
    def fuzz_result_markdown(self, results: list) -> str:
        markdown = ""
        for result in results:
            markdown += f"**{result[0]}**\n\n"
        return markdown