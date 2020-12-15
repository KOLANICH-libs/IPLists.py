import typing
from ipaddress import ip_address, summarize_address_range

from ..core import Format
from ..utils import IPNetwork, net2range


def _parsePeerGuardian(ls: typing.Iterable[str]) -> typing.Iterable[IPNetwork]:
	for el in ls:
		spl1 = el.rsplit(":")
		if len(spl1) == 2:
			comment_, rnge = spl1
			spl2 = rnge.split("-")
			if len(spl2) == 2:
				rnge = tuple(ip_address(el) for el in spl2)
				nets = tuple(summarize_address_range(*rnge))
				yield from nets
			else:
				raise Exception(spl2)
		else:
			raise Exception(spl1)


def _net2record(n: IPNetwork) -> str:
	return ":" + "-".join(str(a) for a in net2range(n))


class PeerGuardianP2P(Format):
	__slots__ = ()
	EXTS = ("p2p",)

	@classmethod
	def parse(cls, ls: typing.Union[str, typing.Iterable[str]]) -> typing.Collection[IPNetwork]:
		if isinstance(ls, str):
			ls = ls.splitlines()
		return tuple(_parsePeerGuardian(ls))

	@classmethod
	def serialize(cls, ls):
		return "\n".join(_net2record(el) for el in ls)
