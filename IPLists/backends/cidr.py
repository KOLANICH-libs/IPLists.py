import typing
from ipaddress import ip_network

from ..core import Format
from ..utils import IPNetwork


def _parseCidrLinesList(ls: typing.Iterable[str]) -> typing.Iterable[IPNetwork]:
	for el in ls:
		if not el or el.startswith("#"):
			continue

		yield ip_network(el)


class CIDR(Format):
	__slots__ = ()
	EXTS = ("ipset", "cidr")

	@classmethod
	def parse(cls, ls: typing.Union[str, typing.Iterable[str]]) -> typing.Collection[IPNetwork]:
		if isinstance(ls, str):
			ls = ls.splitlines()
		return tuple(_parseCidrLinesList(ls))

	@classmethod
	def serialize(cls, ls):
		return "\n".join(str(el) for el in ls)
