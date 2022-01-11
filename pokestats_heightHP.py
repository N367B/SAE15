import markdown
import pokepy


def getPokemonList(first, last) :
	"""
	Entrée : deux entier qui correspondent aux numéros des pokmon (premier strictement supérieur au deuxième)
	Retourne une liste avec les données de chaque pokemon entre les deux entrées
	"""
	pokemons = []
	for i in range(first, last):
		pokemons.append(pokepy.V2Client().get_pokemon(i))
	return pokemons


def statsHeightHP(pokemonList) :
	"""
	Entrée : la liste des avec les données de chaque pokemon obtenu par la fonction getPokemonList(first, last)
	Retourne une liste des données comportant le nom, la taille, la vie de chaque pokemon
	"""
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
	"""
	Entrée : la liste obtenue par la fonction markdownStatsHeightHP(stats)
	Créer un fichier au format markdown avec les pokemon rangée dans un tableau en fonction de la taille
	Ce fichier s'appele statsHeightHP.mp stocké dans le répertoire ./markdown/StatsHeightHP/statsHeightHP.md
	"""
	markdown = "#Les pokémon grands sont-ils les plus tanky ? \n"
	markdown += "| Nom | Taille | HP | \n"
	for i in range(len(stats)) :
		markdown += "| | | | \n"
		markdown += "| " + str(stats[i][0])+ " | " + str(stats[i][1])+ " | " + str(stats[i][2])+ " |" + "\n"
	with open ("./markdown/StatsHeightHP/statsHeightHP.md", 'w') as handler:
		handler.write(markdown)


def markdownToHTML(file):
	"""
	Entrée : le fichier statsHeightHP.mp
	Transforme/convertit ce fichier en page HTML et l'enregistre dans ./html/StatsHeightHP
	"""
	with open('./markdown/StatsHeightHP/'+file, "r") as input_file:
		text = input_file.read()
	html = markdown.markdown(text, extensions=['tables'])
	file = file[:-3]
	file += '.html'
	with open('./html/StatsHeightHP/'+file, 'w', encoding='utf-8') as output_file:
	    output_file.write(html)


def pokestats_heightHP(first, last):
	"""
	Permet de faire fonctionner heigthHP
	"""
	markdownStatsHeightHP(statsHeightHP(getPokemonList(first, last)))
	markdownToHTML('statsHeightHP.md')
	print('Les fichiers sont créés')


pokestats_heightHP(int(input('ID du premier pokémon ? ')), int(input('ID du second pokémon ? ')))
