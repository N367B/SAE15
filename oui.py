import markdown

maList = ['Oui', 'Non', 'Peut-être']

def convertListHTML(list, fileName):
	content = ""
	content += "# La liste contient "+str(len(list))+" éléments\n\n"
	for i in range(len(list)):
		content += " - "+list[i]+"\n"
	html = markdown.markdown(content)
	with open(fileName+".html", 'w') as f:
		f.write(html)

convertListHTML(maList, "cool")

