from FoodSim.person import Person
import unittest


class TestHouse(unittest.TestCase):
	def test_init_basic(self):
		person = Person(prob=0.5)
		self.assertIsInstance(person, Person)

	def test_init_auto_value(self):
		person = Person()
		self.assertIsInstance(person, Person)

	def test_init_value_upper_limit(self):
		person = Person(prob=1.0)
		self.assertIsInstance(person, Person)

	def test_init_value_lower_limit(self):
		person = Person(prob=0.0)
		self.assertIsInstance(person, Person)

	def test_init_value_over(self):
		with self.assertRaises(ValueError):
			person = Person(prob=1.1)

	def test_init_value_under(self):
		with self.assertRaises(ValueError):
			person = Person(prob=-0.1)

	############################################

	def test_sim_false(self):
		person = Person(prob=0.0)
		result = person.sim()

		self.assertEqual(result, False)

	def test_sim_true(self):
		person = Person(prob=1.0)
		result = person.sim()

		self.assertEqual(result, True)

	def test_sim_output(self):
		person = Person(prob=0.5)
		trues = 0
		falses = 0

		for x in range(0, 1_000):
			result = person.sim()
			if result:
				trues += 1
			else:
				falses += 1

		# Check there are the correct number of trues and falses
		self.assertEqual(trues + falses, 1_000)

	def test_sim_probability(self):
		""" Checks that the probability of true/false is correct """
		person = Person(prob=0.5)
		trues = 0
		falses = 0

		for x in range(0, 1_000):
			result = person.sim()
			if result:
				trues += 1
			else:
				falses += 1

		# Check that the probabilities are correct
		# There is a %0.00001 chance that this will fail correctly
		ok = 430 < trues < 570

		self.assertTrue(ok)


if __name__ == '__main__':
	unittest.main()
