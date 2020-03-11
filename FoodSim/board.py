import random
from typing import *

from .constants import *
from .company import *
from .house import *
from .board_log import *


class Board:
	"""

	"""
	def __init__(self,
	             length=BoardProps.length,
	             houses=BoardProps.houses,
	             companies=BoardProps.companies,
	             shop_range=BoardProps.shop_range,
	             company_types=types
	             ):

		self._len = length
		self._houses = houses
		self._num_companies = companies
		self._company_types = company_types
		self._shop_range = shop_range

		self.need_to_adjust_closest = False
		self.log = BoardLog()

		self._gen_board()

	def _gen_board(self):

		# Set up board
		self._board = []

		# Init with nulls
		for x in range(0, self._len):
			to_append = []
			for y in range(0, self._len):
				to_append.append(None)
			self._board.append(to_append)

		# Set up companies
		self.companies = []
		for _ in range(0, self._num_companies):
			_type = random.choice(self._company_types)
			company = Company(_type, self)
			self.companies.append(company)

			# Set up stores
			num_stores = round(random.randint(self._shop_range[0], self._shop_range[1]) * _type.stores_multiplier)

			if num_stores == 0:
				num_stores += 1

			for __ in range(0, num_stores):
				pos = self.get_place()
				store = Store(company, pos)
				self.place(store)
				company.add_store(store)

		# Set up houses
		self.houses = []
		self.build_houses(self._houses)

	def build_houses(self, houses):
		for _ in range(0, houses):
			pos = self.get_place()

			closest_stores = self.calc_closest(pos)

			house = House(closest_stores, pos)
			self.place(house, pos)
			self.houses.append(house)

	def place(self, obj, pos=None):
		if not pos:
			pos = self.get_place()

		self._board[pos[0]][pos[1]] = obj

		return pos

	def get_place(self):
		while True:
			x = random.randint(0, self._len - 1)
			y = random.randint(0, self._len - 1)

			if not self._board[x][y]:
				return x, y

	def calc_closest(self, pos):
		closest_stores = []

		for company in self.companies:
			closest = None
			closest_dist = float("inf")

			for store in company.stores:
				dist_sqrd = (pos[0] - store.pos[0]) ** 2 + (pos[1] - store.pos[1]) ** 2

				if dist_sqrd < closest_dist:
					closest = store
					closest_dist = dist_sqrd

			closest_stores.append(closest)

		return closest_stores

	def sim(self):
		self.log.reset()

		for house in self.houses:
			house.sim()

		for company in self.companies:
			company.sim()

		if self.need_to_adjust_closest:
			for house in self.houses:
				pos = house.pos
				closest = self.calc_closest(pos)
				house.change_closest(closest)

		self.do_events()

		self.need_to_adjust_closest = False
		self.log.output()

	def do_events(self):
		pass

