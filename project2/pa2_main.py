if __name__ == '__main__':

	names = []

	def cap_join(names):

		names2 = " ".join(names).title()
		return names2

	names = ["calvin", "and", "hobbes", "are", "the", "first", "spacemen", "on", "mars"]

	print(cap_join(names))