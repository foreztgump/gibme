import httpx
import ipaddress
import execjs
import pyperclip
from textual import on
from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Markdown, Input, Header, Checkbox, Label, Footer, TabbedContent, TabPane, Select, ListView,ListItem, Button, TextArea
from textual.containers import Horizontal, Vertical, HorizontalScroll
from rapidfuzz import process, fuzz, utils as fuzz_utils

class Rev(Screen):

    BINDINGS = [
        ("escape", "pop_screen", "Close"),
        ("f6", "select_line", "Select Line"),
        ("f7", "select_all", "Select All"),
    ]

    def validate_ip(self, ip: str) -> bool:
        try:
            ipaddress.ip_address(ip)
            return True
        except ValueError:
            return False

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
        with HorizontalScroll(id="border"):
            with Vertical():
                yield Input(placeholder="IP Address", id="input-ip", restrict=r"^[0-9.]*$")
            with Vertical():
                yield Input(placeholder="Port", id="input-port", restrict=r"^(6553[0-5]|655[0-2]\d|65[0-4]\d{2}|6[0-4]\d{3}|[1-5]\d{4}|[1-9]\d{0,3}|0)$")
        
            with Vertical():
                with Horizontal():
                    with Vertical():
                        yield Label(id="listen-label")
                    with Vertical(id="copy-box"):
                        yield Button("Copy", id="copy-listener")
            
            with Vertical():
                yield Select([], prompt="Select Listener", id="select-listener")
                
        with HorizontalScroll(id="results-container"):
            with TabbedContent():
                with TabPane("Reverse", id="reverse"):
                    with Horizontal():
                        with Vertical(id="left-bottom"):
                            yield Input(placeholder="Search Name", id="reverse-input-search")
                            yield ListView(id="reverse-shell-list")
                        with Vertical():
                            with Horizontal(id="checkbox"):
                                yield from self.generate_checkboxes('reverse')
                                yield Select([], prompt="Select Shell", id="select-reverse")
                            with HorizontalScroll():
                                yield TextArea(id="results-reverse")
                with TabPane("Bind", id="bind"):
                    with Horizontal():
                        with Vertical(id="left-bottom"):
                            yield Input(placeholder="Search Name", id="bind-input-search")
                            yield ListView(id="bind-shell-list")
                        with Vertical():
                            with Horizontal(id="checkbox"):
                                yield from self.generate_checkboxes('bind')
                            with HorizontalScroll():
                                yield TextArea(id="results-bind")
                with TabPane("MSFVenom", id="msfvenom"):
                    with Horizontal():
                        with Vertical(id="left-bottom"):
                            yield Input(placeholder="Search Name", id="msfvenom-input-search")
                            yield ListView(id="msfvenom-list")
                        with Vertical():
                            with Horizontal(id="checkbox"):
                                yield from self.generate_checkboxes('msfvenom')
                            with HorizontalScroll():
                                yield TextArea(id="results-msfvenom")
                with TabPane("hoaxShell", id="hoax"):
                    with Horizontal():
                        with Vertical(id="left-bottom"):
                            yield Input(placeholder="Search Name", id="hoax-input-search")
                            yield ListView(id="hoax-shell-list")
                        with Vertical():
                            with Horizontal(id="checkbox"):
                                yield from self.generate_checkboxes('hoax')
                            with HorizontalScroll():
                                yield TextArea(id="results-hoax")
                
        

    async def on_mount(self) -> None:
        """Called when app starts."""
        self.title = "Gibme"
        self.sub_title = "Reverse Shell Generator"

        self.ip = '10.10.10.10'
        self.port = '4444'
        self.selected_listener = 'nc'
        self.selected_shell = 'sh'

        self.rev_data = await self.parse_rev_data()
        self.populate_listener_data(self.rev_data)
        self.populate_tabs_shell_list()

        self.populate_tabs_shell_data(['all'], None)
        self.update_listener(self.selected_listener)

        self.active_tab = self.query_one(TabbedContent).active
        self.active_tab = self.active_tab.lower()
        if self.active_tab == 'reverse':
            self.list_id = 'reverse-shell-list'
            self.selected_rev_shell = self.query_one(f'#{self.list_id}', ListView).children[0].id


    async def on_button_pressed(self, event: Button.Pressed) -> None:
        button_id = event.button.id
        if button_id == 'copy-listener':
            # get listener text from label and remove Listener: from text
            pyperclip.copy(self.listener_text)


    async def on_checkbox_changed(self) -> None:
        # get checked boxes
        checkboxes = self.query(Checkbox)
        self.checked_boxes = [checkbox.id for checkbox in checkboxes if checkbox.value]

        # get active tab
        self.active_tab = self.query_one(TabbedContent).active

        # update os list to match only os with active tab to tabname and remove tab name
        self.active_tab = self.active_tab.lower()
        self.checked_boxes = [x.replace(f'-{self.active_tab}', '') for x in self.checked_boxes if self.active_tab in x]

        self.populate_tabs_shell_data(self.checked_boxes, None)


    async def on_input_changed(self, event: Input.Changed) -> None:
        # get input event id
        input_id = event.input.id

        # get input value for both ip and port
        if input_id == 'input-ip':
            if self.validate_ip(self.query_one("#input-ip").value):
                self.ip = self.query_one("#input-ip").value
            else:
                self.ip = '10.10.10.10'

        #self.ip = self.query_one("#input-ip").value
        if input_id == 'input-port':
            self.port = self.query_one("#input-port").value

            if self.port == '':
                self.port = '4444'
            elif int(self.port) > 65535:
                self.port = '4444'
            
            if self.ip == '':
                self.ip = '10.10.10.10'

        # fuzz search for shell
        self.active_tab = self.query_one(TabbedContent).active
        self.active_tab = self.active_tab.lower()
        if input_id == f'{self.active_tab}-input-search':
            rev_shell_name = self.query_one(f"#{input_id}").value
            if rev_shell_name == '':
                self.populate_tabs_shell_data(['all'], None)
            else:
                if self.active_tab == 'reverse':
                    choices = self.reverse_shell_list
                elif self.active_tab == 'bind':
                    choices = self.bind_shell_list
                elif self.active_tab == 'msfvenom':
                    choices = self.msfvenom_list
                elif self.active_tab == 'hoax':
                    choices = self.hoax_shell_list
                
                fuzz_result = await self.fuzz_shell(rev_shell_name, choices)
                self.populate_tabs_shell_data(['all'], fuzz_result)


        self.update_listener(self.selected_listener)

        if self.selected_rev_shell:
            self.update_results(self.list_id, self.selected_rev_shell, self.selected_shell)


    async def on_select_changed(self, event: Select.Changed) -> None:
        select_id = event.select.id

        # get selected listener
        if select_id == 'select-listener':
            self.selected_listener = self.query_one('#select-listener', Select).value
            self.update_listener(self.selected_listener)
        elif select_id == 'select-reverse':
            self.selected_shell = self.query_one('#select-reverse', Select).value

            if self.selected_rev_shell:
                self.update_results(self.list_id, self.selected_rev_shell, self.selected_shell)


    async def on_list_view_selected(self, event: ListView.Selected) -> None:
        self.list_id = event.list_view.id
        #self.query_one(Markdown).update(f'{event.item.children[0].id}')
        self.selected_rev_shell = event.item.children[0].name

        if self.selected_rev_shell:
            self.update_results(self.list_id, self.selected_rev_shell, self.selected_shell)

    @on(TabbedContent.TabActivated)
    def clear_input(self) -> None:
        self.active_tab = self.query_one(TabbedContent).active
        self.populate_tabs_shell_data(['all'], None)
        tab_id = ['reverse', 'bind', 'msfvenom', 'hoax']
        for id in tab_id:
            if id != self.active_tab:
                self.query_one(f"#{id}-input-search", Input).value = ''

    def update_listener(self, listener: str) -> None:
        # get match listener data from listener list
        listener_data = [listener for listener in self.rev_data['rsgData']['listenerCommands'] if listener[0] == self.selected_listener][0]

        # edit port and display listener data
        self.listener_text = listener_data[1].replace('{port}', self.port)
        if int(self.port) < 1024:
            self.listener_text = f'sudo {self.listener_text}'

        self.query_one("#listen-label", Label).update(f"Listener: {self.listener_text}")


    def update_results(self, list_id: str, rev_shell: str, shell:str) -> None:
        if list_id == 'reverse-shell-list':
            tab = 'reverse'
        elif list_id == 'bind-shell-list':
            tab = 'bind'
        elif list_id == 'msfvenom-list':
            tab = 'msfvenom'
        elif list_id == 'hoax-shell-list':
            tab = 'hoax'

        if tab == 'reverse':
            shell_data = [shell for shell in self.rev_data['reverseShellCommands'] if shell['name'] == rev_shell][0]['command']
        elif tab == 'bind':
            shell_data = [shell for shell in self.rev_data['bindShellCommands'] if shell['name'] == rev_shell][0]['command']
        elif tab == 'msfvenom':
            shell_data = [shell for shell in self.rev_data['msfvenomCommands'] if shell['name'] == rev_shell][0]['command']
        elif tab == 'hoax':
            shell_data = [shell for shell in self.rev_data['hoaxShellCommands'] if shell['name'] == rev_shell][0]['command']

        # replace {ip} {port} {shell} with user input if there exists
        if '{ip}' in shell_data:
            shell_data = shell_data.replace('{ip}', self.ip)
        if '{port}' in shell_data:
            shell_data = shell_data.replace('{port}', self.port)
        if '{shell}' in shell_data:
            shell_data = shell_data.replace('{shell}', shell)

        self.query_one(f"#results-{tab}", TextArea).clear()
        self.query_one(f"#results-{tab}", TextArea).load_text(f'{shell_data}')


    def generate_checkboxes(self, tab_name: str) -> None:
        yield Checkbox("All", "True", id=f"all-{tab_name}")
        yield Checkbox("Linux", id=f"linux-{tab_name}")
        yield Checkbox("MacOSX", id=f"mac-{tab_name}")
        yield Checkbox("Windows", id=f"windows-{tab_name}")


    def populate_listener_data(self, data: list) -> None:
        listener_select_list = []
        for listener in data['rsgData']['listenerCommands']:
            listener_select_list.append((listener[0], listener[0]))

        self.query_one('#select-listener', Select).set_options(listener_select_list)
        self.query_one('#select-listener', Select).value = listener_select_list[0][0]


    def populate_tabs_shell_list(self) -> None:
        shell_select_list = []
        for shell in self.rev_data['rsgData']['shells']:
            shell_select_list.append((shell, shell))

        self.query_one('#select-reverse', Select).set_options(shell_select_list)
        self.query_one('#select-reverse', Select).value = shell_select_list[0][0]


    def _update_list_view(self, list_id: str, shell_list: list) -> None:
        list_view = self.query_one(f'#{list_id}', ListView)
        list_view.clear()
        list_view.extend([ListItem(Label(shell, name=shell)) for shell in shell_list])
        list_view.index = 0


    def populate_tabs_shell_data(self, os: list, fuzz_list: list) -> None:
        self.reverse_shell_list = self._get_shell_list('reverseShellCommands', os)
        self.bind_shell_list = self._get_shell_list('bindShellCommands', os)
        self.msfvenom_list = self._get_shell_list('msfvenomCommands', os)
        self.hoax_shell_list = self._get_shell_list('hoaxShellCommands', os)

        # Reverse Shell
        if fuzz_list:
            self._update_list_view('reverse-shell-list', fuzz_list)
        else:
            self._update_list_view('reverse-shell-list', self.reverse_shell_list)

        # Bind Shell
        
        if fuzz_list:
            self._update_list_view('bind-shell-list', fuzz_list)
        else:
            self._update_list_view('bind-shell-list', self.bind_shell_list)

        # MSFVenom
        
        if fuzz_list:
            self._update_list_view('msfvenom-list', fuzz_list)
        else:
            self._update_list_view('msfvenom-list', self.msfvenom_list)

        # HoaxShell
        
        if fuzz_list:
            self._update_list_view('hoax-shell-list', fuzz_list)
        else:
            self._update_list_view('hoax-shell-list', self.hoax_shell_list)


    def _get_shell_list(self, shell_type: str, os: list = None) -> list:
        shell_list = []
        for shell in self.rev_data[shell_type]:
            if os and 'all' not in os:
                if any(os_item in shell['meta'] for os_item in os):
                    shell_list.append(shell['name'])
            elif 'all' in os:
                shell_list.append(shell['name'])
            else:
                shell_list = []
        return shell_list


    async def fuzz_shell(self, shell_name: str, choices: list) -> list:
        shell_name = shell_name.lower()
        results = process.extract(
                shell_name, 
                choices, 
                scorer=fuzz.QRatio,
                limit=10,
                score_cutoff=40,
                processor=fuzz_utils.default_process,)
        if results:
            highest_similarity = max(results, key=lambda x: x[1])
            if highest_similarity[1] > 90:
                return [highest_similarity[0]]
            else:
                return [result[0] for result in results]
        else:
            return None
            

    async def parse_rev_data(self) -> list:
        try:
            runtime = execjs.get()
            async with httpx.AsyncClient() as client:
                response = await client.get("https://raw.githubusercontent.com/0dayCTF/reverse-shell-generator/main/js/data.js")
                context = runtime.compile(response.text)
                commands = {
                'reverseShellCommands': context.eval('reverseShellCommands'),
                'bindShellCommands': context.eval('bindShellCommands'),
                'msfvenomCommands': context.eval('msfvenomCommands'),
                'hoaxShellCommands': context.eval('hoaxShellCommands'),
                'rsgData': context.eval('rsgData')
            }
            return commands

        except Exception as e:
            self.query_one("#results", Markdown).update(f"**Error getting reverse shell data**\n\nError: {e}")