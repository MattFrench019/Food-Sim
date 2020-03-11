import random

from .person import *
from .func import *
from .constants import *


class House:
	def __init__(self, closest_stores, pos):
		self.stores = closest_stores
		self.pos = pos

		self._num_people = rand_range_int(HouseProps.people)
		self.people = [Person() for _ in range(0, self._num_people)]

	def sim(self):
		sales = [x.sim() for x in self.people]
		for sale in sales:
			if sale:
				store = random.choice(self.stores)
				store.sale()

	def change_closest(self, closest):
		self.stores = closest
