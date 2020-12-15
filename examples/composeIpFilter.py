#!/usr/bin/env python3

import typing
from ipaddress import IPv4Address, IPv4Network
from pathlib import Path

from IPLists.backends.amazon import AmazonJSON
from IPLists.backends.cidr import CIDR
from IPLists.backends.ipfilter import IPFilter
from IPLists.backends.p2p import PeerGuardianP2P
from IPLists.optimize import optimize

try:
	import httpx
except ImportError:
	import requests as httpx


def get(uri):
	return httpx.get(uri).content.decode("utf-8")


sources = [
	(AmazonJSON, "https://ip-ranges.amazonaws.com/ip-ranges.json"),
	(CIDR, "https://raw.githubusercontent.com/jhassine/server-ip-addresses/master/data/datacenters.txt"),
	(CIDR, "https://raw.githubusercontent.com/bongochong/CombinedPrivacyBlockLists/master/combined-final.cidr"),
	(PeerGuardianP2P, "https://raw.githubusercontent.com/bongochong/CombinedPrivacyBlockLists/master/combined-final.p2p"),
	(IPFilter, "https://raw.githubusercontent.com/bongochong/CombinedPrivacyBlockLists/master/combined-final-win.dat"),
]


def main():
	allRanges = sum((backend.parse(get(uri)) for backend, uri in sources), start=())
	optimized = optimize(allRanges)
	Path("./ipfilter.p2p").write_text(PeerGuardianP2P.serialize(optimized))


if __name__ == "__main__":
	main()
