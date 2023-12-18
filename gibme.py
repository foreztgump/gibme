#!/usr/bin/env python3

import argparse
import signal
import sys

from modules.utils import initialize_settings, update_gibme, check_init, fuzz_name
from modules.colors import colors
from modules.gtfobins import list_bins, gtfobins_info
from modules.lolbas import list_exe


def signal_handler(signal, frame):
    print(colors('\n\nYou pressed Ctrl+C!', 'red'))
    sys.exit(0)

def main():
    parser = argparse.ArgumentParser(description='gibme - Your CLI tool')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-b", "--bins", help="Search binaries on GTFOBins")
    group.add_argument("-e", "--exe", help="Search Windows exe on LOLBAS")
    group.add_argument("-s", "--shell", help="Generate reverse shell", choices=['bash', 'perl', 'python', 'php', 'ruby', 'netcat', 'java', 'xterm', 'powershell', 'awk', 'lua', 'telnet', 'socat', 'gdb', 'nmap', 'openssl', 'msfvenom', 'node', 'ncat', 'java', 'ruby', 'python', 'bash', 'php', 'awk', 'xterm', 'socat', 'gdb', 'nmap', 'openssl', 'msfvenom', 'node', 'ncat', 'java', 'ruby', 'python', 'bash', 'php', 'awk', 'xterm', 'socat', 'gdb', 'nmap', 'openssl', 'msfvenom', 'node', 'ncat', 'java', 'ruby', 'python', 'bash', 'php', 'awk', 'xterm', 'socat', 'gdb', 'nmap', 'openssl', 'msfvenom', 'node', 'ncat', 'java', 'ruby', 'python', 'bash', 'php', 'awk', 'xterm', 'socat', 'gdb', 'nmap', 'openssl', 'msfvenom', 'node', 'ncat', 'java', 'ruby', 'python', 'bash', 'php', 'awk', 'xterm', 'socat', 'gdb', 'nmap', 'openssl', 'msfvenom', 'node', 'ncat', 'java', 'ruby', 'python', 'bash', 'php', 'awk', 'xterm', 'socat', 'gdb', 'nmap', 'openssl', 'msfvenom', 'node', 'ncat'])
    group.add_argument("-ls", "--list", help="list all the available binaries or shell", choices=["bins", "exe", "shell"])
    group.add_argument("-u", "--update", help="Update Gibme")

    args = parser.parse_args()

    home_dir = check_init()

    if args.bins:
        name = fuzz_name(name=args.bins, type_str='gtfobins', choice_path=home_dir)
        gtfobins_info(name)

    if args.exe:
        name = fuzz_name(name=args.exe, type_str='lolbas', choice_path=home_dir)
        lolbas_info(name)

    if args.list == 'bins':
        list_bins(home_dir)
    elif args.list == 'exe':
        list_exe(home_dir)
    elif args.list == 'shell':
        print('Shell')


    if args.update:
        update_gibme()
    

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal_handler)
    main()     