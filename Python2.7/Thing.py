class Things:
	pass

class Inanimate(Things):
	pass

class Sidewalks(Inanimate):
	pass

class Animate(Things):
	pass

class Animals(Animate):
	def Breathe(self):
		print ("Breathe")

	def Move(self):
		print("Move")

	def Eat_Food(self):
		print("Eating Food")

class Mammals(Animals):
	def Feed(self):
		print("Feed young with milk")


class Giraffes(Mammals):
	def Eat_Leaves(self):
		print("Eat leaves from trees")
	def Find_Food(self):
		self.Move()
		self.Eat_Leaves()


def main():
	reginald = Giraffes()
	reginald.Eat_Leaves()
	reginald.Feed()
	reginald.Find_Food()


main()



