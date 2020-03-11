import random

from .constants import *


class Person:
	def __init__(self):
		self._chance = PersonProps.probability

	def sim(self):
		# See if they will eat at a store
		return self._chance > random.random()

