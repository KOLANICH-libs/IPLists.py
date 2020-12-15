import typing
from ipaddress import IPv4Network


class Format:
	__slots__ = ()
	EXTS = None

	@classmethod
	def parse(cls, *args) -> typing.Collection[IPv4Network]:
		raise NotImplementedError

	@classmethod
	def serialize(cls, *args):
		raise NotImplementedError
