from .shell_data import reverse_shell, bind_shell, hoax_shell, shells, msfvenom
from .colors import colors


def gen_shell(
    name_list: list, shell_type: str, ip: str, port: str, os: str, shell: str
):
    for name in name_list:
        if shell_type == "reverse":
            for each_shell in reverse_shell:
                if each_shell["name"] == name[0]:
                    if os != "all" and os not in each_shell["meta"]:
                        continue
                    try:
                        shell_command = each_shell["command"].format(
                            ip=ip, port=port, shell=shell
                        )
                    except Exception:
                        shell_command = (
                            each_shell["command"]
                            .replace("{ip}", ip)
                            .replace("{port}", port)
                            .replace("{shell}", shell)
                        )
                    for _i in each_shell["meta"]:
                        os_string = ", ".join(each_shell["meta"])

                    _print_shell(name[0], shell_command, os_string)

        elif shell_type == "bind":
            for each_shell in bind_shell:
                if each_shell["name"] == name[0]:
                    try:
                        shell_command = each_shell["command"].format(port=port)
                    except Exception:
                        shell_command = each_shell["command"].replace("{port}", port)
                    os_string = "Linux, Windows, Mac"

                    _print_shell(name[0], shell_command, os_string)

        elif shell_type == "hoax":
            for each_shell in hoax_shell:
                if each_shell["name"] == name[0]:
                    try:
                        shell_command = each_shell["command"].format(ip=ip, port=port)
                    except Exception:
                        shell_command = (
                            each_shell["command"]
                            .replace("{ip}", ip)
                            .replace("{port}", port)
                        )
                    os_string = "Windows"

                    _print_shell(name[0], shell_command, os_string)

        elif shell_type == "msfvenom":
            for each_shell in msfvenom:
                if each_shell["name"] == name[0]:
                    try:
                        shell_command = each_shell["command"].format(ip=ip, port=port)
                    except Exception:
                        shell_command = (
                            each_shell["command"]
                            .replace("{ip}", ip)
                            .replace("{port}", port)
                        )
                    os_string = "Linux, Windows, Mac"

                    _print_shell(name[0], shell_command, os_string)


def _print_shell(name: str, shell_command: str, os_string: str):
    print(
        colors("\n[+] ", "red")
        + colors("Reverse Shell:\t", "white")
        + colors(name, "green")
    )
    print(
        colors("[+] ", "red")
        + colors("OS:\t\t\t", "white")
        + colors(os_string, "green")
    )
    print(colors("[+] ", "red") + colors("Command:", "white"))
    print(colors("\n" + shell_command + "\n", "blue"))
    print(colors("-" * 70, "yellow"))
