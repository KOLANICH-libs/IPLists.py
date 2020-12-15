import typing
from os import pathsep
from pathlib import Path

from plumbum import cli

from .backends import byExts, byNames
from .core import Format


def parseCliItem(f: str) -> typing.Tuple[Path, typing.Type[Format]]:
	s = f.split(pathsep, 1)
	if len(s) == 1:
		f = Path(s[0])
		importer = byExts[f.suffix[1:]]
	elif len(s) == 2:
		f = Path(s[1])
		importer = byNames[s[0]]
	else:
		raise ValueError("each item must be either just path, or a path prepended with platform-specific path separator and importer type", s)
	return f, importer


class CLI(cli.Application):
	outputFormat = cli.SwitchAttr("--format", cli.Set(*byNames, case_sensitive=True), default="CIDR")

	def main(self, *items):
		data = []
		for el in items:
			f, importer = parseCliItem(el)
			d = f.read_text()
			data.extend(importer.parse(d))
		print(byNames[self.outputFormat].serialize(data))


if __name__ == "__main__":
	CLI.run()
