import markdown
import pokepy

def getPokemon(n):
	pokemon = pokepy.V2Client().get_pokemon(n)
	return pokemon

def statsGeneral(pokemon):
	stats = {'type1' : [], 'type2' : [], 'generation' : [], 'pokedex': [], 'version':[], ... is there any function to do that ? --> "https://pokeapi.co/docs/v2#stats"}
	pokemon.types[0].type.name
def mardownStatsGeneral(stats):
	print('ok')

def downloadPokemonSprite(n):
	pokemon = pokepy.V2Client().get_pokemon(n)
	imagr = pokemon.Sprite
def mardownToHTML(file):
	print('ok')

print(statsGeneral(getPokemon(56)))
