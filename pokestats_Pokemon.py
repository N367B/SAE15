import markdown
import pokepy
import requests

def getPokemon(n):
	pokemon = pokepy.V2Client().get_pokemon(n)
	return pokemon

def statsGeneral(pokemon):
	identifiant = pokemon.id
	nom = pokemon.name
	hauteur = pokemon.height
	poids = pokemon.weight
	attaques = pokemon.moves
	for i in range(len(attaques)):
		attaques[i] = attaques[i].move.__dict__['name']
	return [identifiant, nom, hauteur, poids, attaques]

def downloadPokemonSprite(n):
	pokemon = pokepy.V2Client().get_pokemon(n)
	imagrURL = pokemon.sprites.__dict__['front_default']
	imagr = requests.get(imagrURL).content
	with open('./sprites/'+pokemon.name+'.png', 'wb') as handler:
		handler.write(imagr)

def markdownStatsGeneral(stats):
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
def mardownToHTML(file):
	print('ok')

stats = (statsGeneral(getPokemon(151)))
markdownStatsGeneral(stats)
