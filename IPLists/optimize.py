from pathlib import Path

import sh

from .backends.cidr import CIDR

cm = sh.Command("./cidr-merger").bake("--cidr")


def optimize(inputList):
	if not isinstance(inputList, Path):
		from MempipedPath import MempipedPathRead

		if not isinstance(inputList, (str, bytes)):
			inputList = CIDR.serialize(inputList)
		if isinstance(inputList, str):
			inputList = inputList.encode("utf-8")
		with MempipedPathRead(inputList) as p:
			res = cm(p)
	else:
		res = cm(inputList)
	return CIDR.parse(res)
