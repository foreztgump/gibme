#!/usr/bin/env python3

import argparse
import signal
import sys

from modules.utils import initialize_settings, update_gibme, check_init, fuzz_name
from modules.colors import colors
from modules.gtfobins import list_bins, gtfobins_info
from modules.lolbas import list_exe
from modules.shellgen import gen_shell


def signal_handler(signal, frame):
    print(colors("\n\nYou pressed Ctrl+C!", "red"))
    sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description="gibme - Your CLI tool for generating shells, searching binaries, and more.",
        epilog="""
    Examples:
    python3 gibme.py -b ls    Search for the binary 'ls' on GTFOBins.
    python3 gibme.py -e cmd   Search for the executable 'cmd' on LOLBAS.
    python3 gibme.py -rs bash Generate a reverse shell for bash.
    python3 gibme.py -u       Update Gibme.
    """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    group = parser.add_argument_group("commands")
    group.add_argument(
        "-b", "--bins", metavar="<binary>", help="Search binaries on GTFOBins."
    )
    group.add_argument(
        "-e", "--exe", metavar="<exe>", help="Search Windows exe on LOLBAS."
    )
    group.add_argument(
        "-rs", "--reverse_shell", metavar="<shell>", help="Generate a reverse shell."
    )
    group.add_argument(
        "-hs", "--hoax_shell", metavar="<shell>", help="Generate a hoax shell."
    )
    group.add_argument(
        "-bs", "--bind_shell", metavar="<shell>", help="Generate a bind shell."
    )
    group.add_argument(
        "-msfvenom", metavar="<shell>", help="Generate a msfvenom payload."
    )
    group.add_argument(
        "-ls",
        "--list",
        metavar="<list>",
        help="List all the available binaries or shell.",
        choices=["bins", "exe", "shell"],
    )
    group.add_argument("-u", "--update", help="Update Gibme.")
    parser.add_argument(
        "-s",
        "--shell",
        required=False,
        default="/bin/sh",
        metavar="<shell>",
        help="Specify shell, default is /bin/sh.",
        choices=[
            "sh",
            "/bin/sh",
            "bash",
            "/bin/bash",
            "cmd",
            "powershell",
            "pwsh",
            "ash",
            "bsh",
            "csh",
            "ksh",
            "zsh",
            "pdksh",
            "tcsh",
            "mksh",
            "dash",
        ],
    )
    parser.add_argument(
        "-ip",
        "--ip_address",
        required=False,
        default="10.10.10.10",
        metavar="<ip>",
        help="Specify IP address for reverse shell.",
    )
    parser.add_argument(
        "-p",
        "--port",
        required=False,
        default="9000",
        metavar="<port>",
        help="Specify port for reverse shell.",
    )
    parser.add_argument(
        "-os",
        "--operating_system",
        required=False,
        default="all",
        metavar="<os>",
        help="Specify Operating System for reverse shell.",
    )
    args = parser.parse_args()

    home_dir = check_init()

    if args.bins:
        name = fuzz_name(name=args.bins, type_str="gtfobins", choice_path=home_dir)
        gtfobins_info(name)

    if args.exe:
        name = fuzz_name(name=args.exe, type_str="lolbas", choice_path=home_dir)
        lolbas_info(name)

    if args.list == "bins":
        list_bins(home_dir)
    elif args.list == "exe":
        list_exe(home_dir)
    elif args.list == "shell":
        print("Shell")

    if args.update:
        update_gibme()

    if args.reverse_shell:
        if args.operating_system.lower() == "linux":
            os = "linux"
        elif args.operating_system.lower() == "windows":
            os = "windows"
        elif args.operating_system.lower() == "mac":
            os = "mac"
        elif args.operating_system.lower() == "win":
            os = "windows"
        else:
            os = "all"
        name_list = fuzz_name(name=args.reverse_shell, type_str="reverse")
        gen_shell(
            name_list,
            "reverse",
            args.ip_address,
            args.port,
            os,
            args.shell,
        )

    if args.bind_shell:
        name_list = fuzz_name(name=args.bind_shell, type_str="bind")
        gen_shell(
            name_list,
            "bind",
            None,
            args.port,
            None,
            None,
        )

    if args.msfvenom:
        name_list = fuzz_name(name=args.msfvenom, type_str="msfvenom")
        gen_shell(
            name_list,
            "msfvenom",
            args.ip_address,
            args.port,
            None,
            None,
        )

    if args.hoax_shell:
        name_list = fuzz_name(name=args.hoax_shell, type_str="hoax")
        gen_shell(
            name_list,
            "hoax",
            args.ip_address,
            args.port,
            None,
            None,
        )

    if args.help:
        parser.print_help()


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
