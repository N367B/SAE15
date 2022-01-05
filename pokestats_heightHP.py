import markdown
import pokepy

def getPokemonList(first, last) :
	pokemons = []
	for i in range(first, last+1):
		pokemons.append(pokepy.V2Client().get_pokemon(i))
	return pokemons

def statsHeight(pokemonList) :
	nom = [None] * len(pokemonList)
	taille = [None] * len(pokemonList)
	vie = [None] * len(pokemonList)
	infos = [None] * len(pokemonList)
	for i in range(len(pokemonList)) :
		nom[i] = pokemonList[i].name
		taille[i] = pokemonList[i].height
		vie[i] = pokemonList[i].stats[0].base_stat
		infos[i] = [nom[i], taille[i], vie[i]]
	infos.sort(key = lambda x: x[1])
	return infos


def markdownStatsHeightHP(stats) :
	markdown = "#Les pokémon grands sont-ils les plus tanky ? \n"
	markdown += "| Nom | Taille | HP | \n"
	for i in range(len(stats)) :
		markdown += "| | | | \n"
		markdown += "| " + str(stats[i][0])+ " | " + str(stats[i][1])+ " | " + str(stats[i][2])+ " |" + "\n"
	with open ("./markdown/StatsHeightHP/statsHeightHP.md", 'w') as handler:
		handler.write(markdown)


markdownStatsHeightHP(statsHeight(getPokemonList(1, 10)))
