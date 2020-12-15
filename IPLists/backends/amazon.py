import typing

try:
	import ujson as json
except ImportError:
	import json

from ..core import Format
from ..utils import IPNetwork
from .cidr import _parseCidrLinesList


def _parseAmazonAddresses(amazonIps: dict) -> typing.Iterable[IPNetwork]:
	return _parseCidrLinesList(p["ip_prefix"] for p in amazonIps["prefixes"])


class AmazonJSON(Format):
	__slots__ = ()

	@classmethod
	def parse(cls, amazonIps: dict) -> typing.Collection[IPNetwork]:
		if isinstance(amazonIps, (str, bytes)):
			amazonIps = json.loads(amazonIps)
		return tuple(_parseAmazonAddresses(amazonIps))
