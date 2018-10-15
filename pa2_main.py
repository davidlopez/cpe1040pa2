if __name__ == '__main__':

	names = ["calvin", "and", "hobbes", "are", "the", "first", "spacemen", "on", "mars"]

	def cap_join(names):

		names2 = " ".join(names).title()
		return names2

	print(cap_join(names))
	