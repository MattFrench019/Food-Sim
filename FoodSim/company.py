import random
from typing import *

from .func import *
from .store import *


class Company:
	def __init__(self, _type, board):
		self.type = _type
		self.parent = board

		# TODO Change
		self.name = "Bob"

		# Set up random variables based on company type
		self.sale_price = round_pence(rand_range_float(_type.sale_price))
		self.cost_per_sale = round_pence(self.sale_price * rand_range_float(_type.cost_per_meal_percent))
		self.store_cost_avg = round_pence(rand_range_float(_type.store_costs))

		self.stores = []
		self.stores_inactive = []
		self.active = True


	def add_store(self, store):
		self.stores.append(store)

	def remove_store(self, store):
		self.parent.log.store_remove(self)

		self.stores.remove(store)
		self.stores_inactive.append(store)

		self.parent.need_to_adjust_closest = True

	def sim(self):
		if self.active:
			for store in self.stores:
				store.sim()

			if len(self.stores) == 0:
				self.active = False
				self.parent.log.close(self)

	@property
	def sales(self):
		sales = 0.0
		stores = self.stores.copy()
		stores += self.stores_inactive.copy()

		for store in stores:
			sales += store.sales
		return round_pence(sales)

	@property
	def costs(self):
		costs = 0.0
		stores = self.stores.copy()
		stores += self.stores_inactive.copy()

		for store in stores:
			costs += store.costs
		return round_pence(costs)

	@property
	def total(self):
		return round_pence(self.sales - self.costs)

