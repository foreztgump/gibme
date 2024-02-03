import httpx
from textual import work
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Markdown, Input, Header, Checkbox, Footer
from textual.containers import VerticalScroll, Horizontal
from rapidfuzz import process, fuzz, utils as fuzz_utils

class TLDR(Screen):

    BINDINGS = [("escape", "pop_screen", "Close")]

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        yield Input(placeholder="Search for TLDR Pages")
        with Horizontal(id="checkbox"):
            yield Checkbox("Common", "True", id="common")
            yield Checkbox("Linux", id="linux")
            yield Checkbox("MacOSX", id="macosx")
            yield Checkbox("Windows", id="windows")
            yield Checkbox("Android", id="android")
            yield Checkbox("OpenBSD", id="openbsd")
            yield Checkbox("FreeBSD", id="freebsd")
            yield Checkbox("Sunos", id="sunos")
            yield Checkbox("NetBSD", id="netbsd")

        with VerticalScroll(id="results-container"):
            yield Markdown(id="results")

    async def on_mount(self) -> None:
        """Called when app starts."""
        self.query_one(Input).focus()
        self.title = "Gibme"
        self.sub_title = "TLDR Lookup"
        self.tldr_dict = await self.get_tldr()

    async def on_checkbox_changed(self) -> None:
        checkboxes = self.query(Checkbox)
        self.checked_boxes = [checkbox.id for checkbox in checkboxes if checkbox.value]

    async def on_input_changed(self, message: Input.Changed) -> None:
        if message.value:
            checkboxes = self.query(Checkbox)
            self.checked_boxes = [checkbox.id for checkbox in checkboxes if checkbox.value]
            
            # Filter the platforms based on the checked boxes
            platforms_to_fuzz = {platform: pages for platform, pages in self.tldr_dict.items() if platform in self.checked_boxes}
            
            # Fuzz the names in the filtered platforms
            fuzzed_names = await self.fuzz_tldr(message.value, platforms_to_fuzz)
            
            if len(fuzzed_names) == 0:
                self.query_one("#results", Markdown).update(f"**Not Found**")
            elif len(fuzzed_names) == 1 and len(fuzzed_names[0]) == 2:
                self.get_tldr_info(fuzzed_names[0])
            else:
                self.query_one("#results", Markdown).update(self.fuzz_result_markdown(fuzzed_names))
        else:
            # Clear the results
            self.query_one("#results", Markdown).update("")

    @work(exclusive=True)
    async def get_tldr_info(self, tldr_name: tuple) -> None:
        raw_url = f"https://raw.githubusercontent.com/tldr-pages/tldr/master/pages/{tldr_name[1]}/{tldr_name[0]}.md"
        async with httpx.AsyncClient() as client:
            try:
                response = await client.get(raw_url)
                self.query_one("#results", Markdown).update(response.text)
            except Exception as e:
                self.query_one("#results", Markdown).update(f"**{tldr_name[0]}**\n\n**{tldr_name[1]}**\n\nNot Found\n\nError: {e}")

    async def fuzz_tldr(self, tldr_name: str, platforms_to_fuzz: dict) -> list:
        # Initialize an empty list for the results
        results = []

        # Iterate over the platforms and their pages
        for platform, pages in platforms_to_fuzz.items():
            # Use fuzzy matching to find the best matches for tldr_name in the pages
            matches = process.extract(
                tldr_name, 
                pages, 
                scorer=fuzz.ratio,
                limit=10,
                score_cutoff=70,
                processor=fuzz_utils.default_process,
            )

            # Add the platform to the matches and append them to the results
            results.extend((match, score, platform) for match, score, _ in matches)

        if results:
            highest_similarity = max(results, key=lambda x: x[1])
            if highest_similarity[1] > 90:
                return [(highest_similarity[0], highest_similarity[2])]
            else:
                return results
        else:
            return results

    async def get_tldr(self) -> dict:
        """Get the list of tldr pages."""
        tldr_dict = {}
        async with httpx.AsyncClient() as client:
            response = await client.get("https://tldr.sh/assets/index.json")
            data = response.json()
            for command in data["commands"]:
                for platform in command["platform"]:
                    if platform not in tldr_dict:
                        tldr_dict[platform] = []
                    tldr_dict[platform].append(command["name"])
        return tldr_dict
    
    def fuzz_result_markdown(self, results: list) -> str:
        markdown = ""
        for result in results:
            markdown += f"**{result[0]}**\n\n"
        return markdown