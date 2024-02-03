import json
from textual import work
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Markdown, Input, Header, ListView, ListItem, Markdown, Footer
from textual.containers import VerticalScroll, Container
from meilisearch_python_sdk import AsyncClient
from meilisearch_python_sdk.models.search import Hybrid

class CVE(Screen):
    
        BINDINGS = [("escape", "pop_screen", "Close")]
    
        def compose(self) -> ComposeResult:
            yield Header()
            yield Footer()
            yield Input(placeholder="Search for CVEs")
            with Container(id="app-grid"):
                with VerticalScroll(id="left-pane"):
                    yield ListView(id="cve-list")

                with VerticalScroll(id="right-pane"):
                    yield Markdown(id="results")


        async def on_mount(self) -> None:
            """Called when app starts."""
            self.query_one(Input).focus()
            self.title = "Gibme"
            self.sub_title = "CVE Search"
            self.result = None
        
        async def on_input_changed(self, message: Input.Changed) -> None:
            if message.value:
                self.search_cve(message.value)
                
        async def on_list_view_selected(self, event: ListView.Selected) -> None:
            cve_id = event.item.children[0].id
            await self.display_results(cve_id)

        async def display_results(self, cve_id: str) -> None:
            cve = [cve for cve in self.result if cve["id"] == cve_id]
            if cve:
                cve = cve[0]
                description = cve.get('description', '')
                references = '\n'.join(['- ' + ref for ref in cve.get('references', [])])
                poc_references = '\n'.join(['- ' + ref for ref in cve.get('poc', {}).get('reference', [])])
                github_links = '\n'.join(['- ' + link for link in cve.get('poc', {}).get('github', [])])
                self.query_one("#results", Markdown).update(f"**ID:** {cve['id']}\n\n**Description:**\n{description}\n\n**References:**\n{references}\n\n**Proof of Concept References:**\n{poc_references}\n\n**GitHub Links:**\n{github_links}")
            else:
                self.query_one("#results", Markdown).update(f"**{cve_id}** not found")
            

        @work(exclusive=True)    
        async def search_cve(self, query: str) -> None:
            url = "https://cve.teecybervault.com"
            search_key = "531c533fe69dd6af154008aa1d62a1f19df34233c21bbff168a26a130e6dab16"
            try:
                async with AsyncClient(url=url, api_key=search_key) as client:
                    index = client.index("cve")
                    hybrid = Hybrid(semantic_ratio=0.5, embedder="default")
                    response = await index.search(query, limit=30, hybrid=hybrid)
                    self.result = response.hits
                    
            except Exception as e:
                self.query_one("#results", Markdown).update(f"**Error:** {e}")
                
            if self.result:
                await self.populate_list_view(self.result)

        async def populate_list_view(self, cve_list: list) -> None:
            # parse id and description from cve_list
            cve_list = [(cve["id"], cve.get("description", "")) for cve in cve_list if "id" in cve]
            list_view = self.query_one("#cve-list", ListView)
            list_view.clear()
            list_view.extend([ListItem(Markdown(f'**{cve_id}**\n\n{description[:100]}...', id=cve_id)) for cve_id, description in cve_list])
            list_view.index = 0
            await self.display_results(cve_list[0][0])