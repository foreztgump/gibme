import urllib.parse
import base64

from .shell_data import (
    reverse_shell,
    bind_shell,
    hoax_shell,
    shells,
    msfvenom,
    listenerCommands,
)
from rich.console import Console
from rich.table import Table
from rich.text import Text


def generate_shell(
    shell_names: list,
    shell_type: str,
    ip_address: str,
    port_number: str,
    operating_system: str,
    shell: str,
    encode: str = None,
    listener: str = None,
):
    listener_text = None
    if listener:
        for each_listener in listenerCommands:
            if each_listener[0] == listener:
                try:
                    listener_text = each_listener[1].format(port=port_number)
                except Exception:
                    listener_text = each_listener[1].replace("{port}", port_number)

    for name in shell_names:
        if shell_type == "reverse":
            for each_shell in reverse_shell:
                shell_command_encoded = None
                if each_shell["name"] == name[0]:
                    if (
                        operating_system != "all"
                        and operating_system not in each_shell["meta"]
                    ):
                        continue
                    try:
                        shell_command = each_shell["command"].format(
                            ip=ip_address, port=port_number, shell=shell
                        )
                        if encode:
                            shell_command_encoded = encode_str(shell_command, encode)
                    except Exception:
                        shell_command = (
                            each_shell["command"]
                            .replace("{ip}", ip_address)
                            .replace("{port}", port_number)
                            .replace("{shell}", shell)
                        )
                        if encode:
                            shell_command_encoded = encode_str(shell_command, encode)
                    for _i in each_shell["meta"]:
                        os_string = ", ".join(each_shell["meta"])

                    _print_shell(
                        name=name[0],
                        shell_command=shell_command,
                        os_string=os_string,
                        encoded=shell_command_encoded,
                        listener_text=listener_text,
                    )

        elif shell_type == "bind":
            for each_shell in bind_shell:
                if each_shell["name"] == name[0]:
                    try:
                        shell_command = each_shell["command"].format(port=port_number)
                    except Exception:
                        shell_command = each_shell["command"].replace(
                            "{port}", port_number
                        )
                    os_string = "Linux, Windows, Mac"

                    _print_shell(
                        name=name[0],
                        shell_command=shell_command,
                        os_string=os_string,
                        listener_text=listener_text,
                    )

        elif shell_type == "hoax":
            for each_shell in hoax_shell:
                if each_shell["name"] == name[0]:
                    try:
                        shell_command = each_shell["command"].format(
                            ip=ip_address, port=port_number
                        )
                    except Exception:
                        shell_command = (
                            each_shell["command"]
                            .replace("{ip}", ip_address)
                            .replace("{port}", port_number)
                        )
                    os_string = "Windows"

                    _print_shell(
                        name=name[0],
                        shell_command=shell_command,
                        os_string=os_string,
                        listener_text=listener_text,
                    )

        elif shell_type == "msfvenom":
            for each_shell in msfvenom:
                if each_shell["name"] == name[0]:
                    try:
                        shell_command = each_shell["command"].format(
                            ip=ip_address, port=port_number
                        )
                    except Exception:
                        shell_command = (
                            each_shell["command"]
                            .replace("{ip}", ip_address)
                            .replace("{port}", port_number)
                        )
                    os_string = "Linux, Windows, Mac"

                    _print_shell(
                        name=name[0],
                        shell_command=shell_command,
                        os_string=os_string,
                        listener_text=listener_text,
                    )


def _print_shell(
    name: str,
    shell_command: str,
    os_string: str,
    listener_text: str = None,
    encoded: str = None,
):
    # Initialize console
    console = Console()

    # Prepare shell details
    shell_details = (
        Text("\nReverse Shell: ", style="bold")
        + Text(name, style="cyan")
        + Text(" | OS: ", style="bold")
        + Text(os_string, style="cyan")
    )

    # Prepare shell command
    shell_command_text = Text("\nCommand:\n", style="bold") + Text(
        shell_command, style="green"
    )

    # Print shell details and command
    console.print(shell_details)
    console.print(shell_command_text)

    # Encode the shell command if required
    if encoded:
        shell_command_encoded_text = Text("\nEncoded:\n", style="bold") + Text(
            encoded, style="yellow"
        )
        console.print(shell_command_encoded_text)

    # Print listener command
    if listener_text:
        listener_command_text = Text("\nListener:\n", style="bold") + Text(
            listener_text, style="red"
        )
        console.print(listener_command_text)

    # Print separator
    console.print("\n")
    console.print(Text("=" * 50, style="dim"))
    console.print("\n")


def encode_str(text: str, encode_type: str):
    if encode_type == "base64":
        return base64.b64encode(text.encode()).decode()
    elif encode_type == "url":
        return urllib.parse.quote(text)


def list_shells():
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Type", style="yellow")
    table.add_column("Shell Name", style="cyan")
    table.add_column("Meta", style="blue")

    for shell_type, shells in [("Reverse", reverse_shell), ("Bind", bind_shell), ("Hoax", hoax_shell), ("MSFVenom", msfvenom)]:
        for shell in shells:
            table.add_row(shell_type, shell["name"], ", ".join(shell["meta"]))

    console.print(table)

def list_listeners():
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Listener Name", style="cyan")
    table.add_column("Command", style="green")

    for listener in listenerCommands:
        table.add_row(listener[0], listener[1])

    console.print(table)
