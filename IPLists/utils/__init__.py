import typing
from ipaddress import IPv4Address, IPv4Network, IPv6Address, IPv6Network
from struct import Struct

IPAddress = typing.Union[IPv4Address, IPv6Address]
IPNetwork = typing.Union[IPv4Network, IPv6Network]

fourByteStruct = Struct("=BBBB")
oneIntStruct = Struct(">I")


def parseIpv4AddrWithLeadingZeros(s: str) -> IPv4Address:
	intTuple = tuple(int(el) for el in s.split("."))
	return IPv4Address(oneIntStruct.unpack(fourByteStruct.pack(*intTuple))[0])


def net2range(n: IPv4Network) -> typing.Tuple[IPv4Address, IPv4Address]:
	return n.network_address, n.broadcast_address
