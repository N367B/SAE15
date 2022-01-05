import markdown
import pokepy

def getPokemonList(first, last) :
	pokemons = []
	for i in range(first, last+1):
		pokemons.append(pokepy.V2Client().get_pokemon(i))
	return pokemons

def statsHeight(pokemonList) :
	taille = [None] * len(pokemonList)
	vie = [None] * len(pokemonList)
	nom = [None] * len(pokemonList)
	for i in range(len(pokemonList)) :
		nom[i] = pokemonList[i].name
		taille[i] = pokemonList[i].height
		vie[i] = pokemonList[i].stats[0].base_stat
	return [nom, taille, vie]


def markdownStatsHeightHP(stats) :
	markdown = "#Les pokémon grands sont-ils les plus tanky ? \n"
	markdown += "| Nom | Taille | HP | \n"
	for i in range(len(stats[0])) :
		markdown += "| | | | \n"
		markdown += "| " + str(stats[0][i])+ " | " + str(stats[1][i])+ " | " + str(stats[2][i])+ " |" + "\n"
	with open ("./markdown/StatsHeightHP/statsHeightHP.md", 'w') as handler:
		handler.write(markdown)


markdownStatsHeightHP(statsHeight(getPokemonList(1, 5)))
