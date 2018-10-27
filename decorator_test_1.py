
userlogged = True

def decorateur(func):
	def wrapper():
		if userlogged:
			print("vous etes connectes")
			return func()
		print("utilisateur inconnu")
	return wrapper

@decorateur
def articles():
	print("voici la liste des articles accessibles")


articles()
