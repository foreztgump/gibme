#!/usr/bin/env python3

import argparse
import signal
import sys

from modules.utils import update_gibme, check_init, fuzz_name
from modules.gtfobins import list_bins, gtfobins_info
from modules.lolbas import list_exe, lolbas_info
from modules.shellgen import generate_shell
from modules.shell_data import listenerCommands, shells
from modules.cheatsheet import list_notes, print_note
from rich import print


def signal_handler(signal, frame):
    print("[red]\n\nYou pressed Ctrl+C![/red]")
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
        choices=["bins", "exe", "shell", "notes"],
    )
    group.add_argument(
        "-n",
        "--notes",
        nargs=2,
        metavar=("<default or custom>", "<filename>"),
        required=False,
        help="Print the note. Provide either 'default' or 'custom' as the first argument and the file name as the second argument.",
    )
    parser.add_argument(
        "-u",
        "--update",
        required=False,
        action="store_true",
        help="Update the binaries and executables.",
    )
    parser.add_argument(
        "-s",
        "--shell",
        required=False,
        default="/bin/sh",
        metavar="<shell>",
        help="Specify shell, default is /bin/sh.",
        choices=shells,
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
    parser.add_argument(
        "-en",
        "--encode",
        required=False,
        default="",
        metavar="<encode>",
        help="Specify encoding for reverse shell.",
        choices=["base64", "url"],
    )
    parser.add_argument(
        "-l",
        "--listener",
        required=False,
        default="",
        metavar="<listener>",
        help="Specify listener for reverse shell.",
        choices=[command[0] for command in listenerCommands],
    )
    parser.add_argument(
        "-v",
        "--version",
        required=False,
        action="store_true",
        help="Show version.",
    )

    args = parser.parse_args()

    home_dir = check_init()

    if args.bins:
        name = fuzz_name(name=args.bins, type_str="gtfobins", home_dir=home_dir)
        gtfobins_info(name)

    if args.exe:
        name = fuzz_name(name=args.exe, type_str="lolbas", home_dir=home_dir)
        lolbas_info(name, home_dir)

    if args.list == "bins":
        list_bins(home_dir)
    elif args.list == "exe":
        list_exe(home_dir)
    elif args.list == "shell":
        print("Shell")
    elif args.list == "notes":
        list_notes(home_dir)

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
        generate_shell(
            shell_names=name_list,
            shell_type="reverse",
            ip_address=args.ip_address,
            port_number=args.port,
            operating_system=os,
            shell=args.shell,
            encode=args.encode,
            listener=args.listener,
        )

    if args.bind_shell:
        name_list = fuzz_name(name=args.bind_shell, type_str="bind")
        generate_shell(
            shell_names=name_list,
            shell_type="bind",
            ip_address=None,
            port_number=args.port,
            operating_system=None,
            shell=None,
            listener=args.listener,
        )

    if args.msfvenom:
        name_list = fuzz_name(name=args.msfvenom, type_str="msfvenom")
        generate_shell(
            shell_names=name_list,
            shell_type="msfvenom",
            ip_address=args.ip_address,
            port_number=args.port,
            operating_system=None,
            shell=None,
            listener=args.listener,
        )

    if args.hoax_shell:
        name_list = fuzz_name(name=args.hoax_shell, type_str="hoax")
        generate_shell(
            shell_names=name_list,
            shell_type="hoax",
            ip_address=args.ip_address,
            port_number=args.port,
            operating_system=None,
            shell=None,
            listener=args.listener,
        )

    if args.notes:
        name = fuzz_name(
            name=args.notes[1],
            type_str="notes",
            choice_path=args.notes[0],
            home_dir=home_dir,
        )
        print_note(home_dir=home_dir, note_name=name[0], note_mode=args.notes[0])


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    main()
