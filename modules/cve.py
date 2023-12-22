import httpx
import asyncio
import json

from bs4 import BeautifulSoup


class CVE:
    def __init__(self, cve_name: str = None, search_keyword: str = None):
        self.cve_name = cve_name
        self.search_keyword = search_keyword
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/113.0"
        }

    def get_cve_poc(self):
        url = "https://raw.githubusercontent.com/trickest/cve/main/references.txt"

    def search_cve(self):
        url = "https://cve.mitre.org/cgi-bin/cvekey.cgi?keyword={}"

    def get_cve(self):
        url = "https://cve.mitre.org/cgi-bin/cvename.cgi?name={}"
