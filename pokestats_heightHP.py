import markdown 
import pokepy

def getPokemonList(first, last) :
	pokemons = []
	for i in range(first, last+1):
		pokemons.append(pokepy.V2Client().get_pokemon(i))
	return pokemons
print(getPokemonList(1, 5))
