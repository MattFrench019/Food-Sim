

class BoardLog:
	def __init__(self):
		self._log = []

	def reset(self):
		self._log = []

	def store_remove(self, company):
		msg = f"The {company.type.name} restaurant \"{company.name}\" has closed a store due to losses"
		self._log.append(msg)

	def close(self, company):
		msg = f"The {company.type.name} restaurant \"{company.name}\" has closed"
		self._log.append(msg)

	def output(self):
		for msg in self._log:
			print(msg)