import markdown
import pokepy
import requests
import os

def getPokemon(n):
	"""
	Entrée : Un entier, pour un numéro de pokémon
	Retourne une variable avec les données correspondantes avec le numéro du pokémon
	Utilisation de pokepy
	"""
	pokemon = pokepy.V2Client().get_pokemon(n)
	return pokemon

def statsGeneral(pokemon):
	"""
	Entrée : variable pokémon obtenue par la fonction getPokemon(n)
	Retourne une liste comprenant certaines statisqtiques sur le pokémon sous la forme :
	[identifiant, nom, hauteur, poids, [attaques]]
	Attaques est une liste des 'moves'
	"""
	identifiant = pokemon.id
	nom = pokemon.name
	hauteur = pokemon.height
	poids = pokemon.weight
	attaques = pokemon.moves
	for i in range(len(attaques)):
		attaques[i] = attaques[i].move.__dict__['name']
	return [identifiant, nom, hauteur, poids, attaques]

def downloadPokemonSprite(n):
	"""
	Entrée : un entier, pour le numéro du pokémon
	La fonction télécharge le sprite (de devant, par défaut) correspondant un numéro du pokémon
	L'image est stockée dans le répertoire ./sprites avec le nom du pokémon en .png
	"""
	pokemon = pokepy.V2Client().get_pokemon(n)
	imagrURL = pokemon.sprites.__dict__['front_default']
	imagr = requests.get(imagrURL).content
	with open('./sprites/'+pokemon.name+'.png', 'wb') as handler:
		handler.write(imagr)

def markdownStatsGeneral(stats):
	"""
	Entrée : liste des statisqtiques sur un poékmon, obtenu par la fonction statsGeneral(pokemon)
	La fonction crée un fichier markdown, dans lequel les statisqtiques sont affichées, ainsi que le sprite correspondant
	"""
	downloadPokemonSprite(stats[0])
	content = '# Nom du pokémon : '+str(stats[1])+'\n\n'
	content += '![image de '+str(stats[1])+'](../../sprites/'+stats[1]+'.png)\n\n'
	content += '## Taille : '+ str(stats[2])+'\n\n'
	content += '## Poids : '+ str(stats[3])+'\n\n'
	content += '#Liste des attaques :\n'
	for i in range(len(stats[4])):
		content += '- '+stats[4][i] + '\n'
	with open('./markdown/StatsGeneral/'+stats[1]+'_stats.md', 'w') as handler:
		handler.write(content)

def markdownToHTML(file):
	"""
	Entrée : le nom du fichier (seulement le nom+extension, sans le répertoire)
	La fonction transforme le fichier au format markdown en fichier HTML, qui est stocké dans le répertoire ./html/StatsGeneral au avec le nom 'fichier'.html
	"""
	with open('./markdown/StatsGeneral/'+file, "r") as input_file:
		text = input_file.read()
	html = markdown.markdown(text)
	base = os.path.splitext(file)[0]
	file += '.html'
	with open('./html/StatsGeneral/'+file, 'w', encoding='utf-8') as output_file:
	    output_file.write(html)


def marche(n):
	"""
	Permet de faire fonctionner
	"""
	stats = (statsGeneral(getPokemon(n)))
	markdownStatsGeneral(stats)
	markdownToHTML(stats[1]+'_stats.md')
