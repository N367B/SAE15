import markdown
import pokepy

def getPokemon(n):
	pokemon = pokepy.V2Client().get_pokemon(n)
	return pokemon

def statsGeneral(pokemon):
	#stats = Taille, poid, liste des attaques, nom du pokémon, sprite--> "https://pokeapi.co/docs/v2#stats"}
	pokemon.types[0].type.name
def mardownStatsGeneral(stats):
	print('ok')

def downloadPokemonSprite(n):
	pokemon = pokepy.V2Client().get_pokemon(n)
	imagr = pokemon.PokemonSprites
def mardownToHTML(file):
	print('ok')

print(statsGeneral(getPokemon(56)))
print(downloadPokemonSprite(56))
