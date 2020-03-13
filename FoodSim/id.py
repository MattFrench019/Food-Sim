import string
import random

from .constants import Prefix

_ids = {}


def rand_id(_type):
	while True:
		prefix = Prefix.get(_type) if Prefix.get(_type) else Prefix.get('None')
		rand_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=7))

		if not _ids.get(rand_str):
			_ids[rand_str] = True
			return prefix + rand_str
