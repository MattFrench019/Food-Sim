from typing import *


class CompanyType:
	def __init__(self,
		name: str,
		store_costs: Tuple[float, float],
		sale_price: Tuple[float, float],
		cost_per_meal: Tuple[float, float],
		stores_multiplier: float,
		sales_multiplier: float,
		store_close_limit: float,
		store_open_limit: float,
	):

		self.name = name
		self.store_costs = store_costs
		self.sale_price = sale_price
		self.cost_per_meal_percent = cost_per_meal
		self.stores_multiplier = stores_multiplier
		self.sales_multiplier = sales_multiplier
		self.store_close_limit = store_close_limit
		self.store_open_limit = store_open_limit
