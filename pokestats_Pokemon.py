import markdown
import pokepy

def getPokemon(n):
	pokemon = pokepy.V2Client().get_pokemon(n)
	return pokemon

def statsGeneral(pokemon):
	#son identifiant, son nom, sa hauteur, son poids, et une liste de ses attaques possibles
	identifiant = pokemon.id
	nom = pokemon.name
	hauteur = pokemon.height
	poids = pokemon.weight
	attaques = pokemon.moves
	for i in range(len(attaques)):
		attaques[i] = attaques[i].move.__dict__['name']
	return [identifiant, nom, hauteur, poids, attaques]

def mardownStatsGeneral(stats):
	print('ok')

#def downloadPokemonSprite(n):
	pokemon = pokepy.V2Client().get_pokemon(n)
	imagr = pokemon.Sprites
def mardownToHTML(file):
	print('ok')

stats = (statsGeneral(getPokemon(56)))
#print(downloadPokemonSprite(56))
print(stats)
