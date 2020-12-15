from .amazon import AmazonJSON
from .cidr import CIDR
from .ipfilter import IPFilter
from .p2p import PeerGuardianP2P

backends = [AmazonJSON, CIDR, IPFilter, PeerGuardianP2P]


def _genExtsMapping(backends):
	res = {}
	for el in backends:
		exts = el.EXTS
		if exts:
			for ext in exts:
				res[ext] = el
	return res


byExts = _genExtsMapping(backends)
byNames = {el.__name__: el for el in backends}
