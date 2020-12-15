import typing
from ipaddress import summarize_address_range

from ..core import Format
from ..utils import IPNetwork, parseIpv4AddrWithLeadingZeros


def _parseIpFilteDat(ls: typing.Iterable[str]) -> typing.Iterable[IPNetwork]:
	for el in ls:
		spl1 = el.split(",", 2)
		if len(spl1) == 3:
			spl1 = tuple(el.strip() for el in spl1)
			rnge, lvl, comment_ = spl1
			# lvl = parseIntWithLeadingZeros(lvl)
			lvl = int(lvl)
			if lvl < 127:
				spl2 = rnge.split("-")
				spl2 = tuple(el.strip() for el in spl2)
				if len(spl2) == 2:
					rnge = tuple(parseIpv4AddrWithLeadingZeros(el) for el in spl2)
					nets = tuple(summarize_address_range(*rnge))
					yield from nets
				else:
					raise Exception(spl2)
		else:
			raise Exception(spl1)


def _net2record(n: IPNetwork) -> str:
	return " - ".join(str(a) for a in net2range(n)) + "," + "000" + ","


class IPFilter(Format):
	__slots__ = ()
	EXTS = ("dat",)

	@classmethod
	def parse(cls, ls: typing.Iterable[str]) -> typing.Collection[IPNetwork]:
		if isinstance(ls, str):
			ls = ls.splitlines()
		return tuple(_parseIpFilteDat(ls))

	@classmethod
	def serialize(cls, ls):
		return "\n".join(_net2record(el) for el in ls)
