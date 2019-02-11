listeHtml = ['<h1>','<h2>','<h3>','<em>','</em>','<ul>','<li>','<a>','</a>','<br>','<a','>','<u>','</u>','<strong>','</strong>']
listeMd = ['# ','## ','### ','**','**','* ','	*','[',']','\n','[',']','__','__','**','**']
listeNonDésirés = ['<!DOCTYPE', 'html>','<html>','<head>','</head>','</h1>','</h2>','</h3>','</li>','<p>','</p>''</img>','href=','</ul>','</body>','</html>','<body>','<title>','</title>','</ol>']
with open(input("Veuillez entrez le chemin de votre fichier .html à convertir en markdown: ")) as fichierHtml:
	fichier = open('Fichier Converti vers Markdo.md','w')
	for lignes in fichierHtml:
		lignes = lignes.replace(">", "> ")
		lignes = lignes.replace("><", "> <")
		lignes = lignes.replace("<", " <")
		lignes = lignes.replace("=", " = ")
		liste = lignes.split()
		compteur = 0
		compteur2 = 0				
		while compteur < len(listeHtml):
			liste = [listeMd[compteur] if x == listeHtml[compteur] else x for x in liste]
			compteur += 1
		while compteur2 < len(listeNonDésirés):
			liste = ["" if x == listeNonDésirés[compteur2] else x for x in liste]
			compteur2 += 1
		chaine = " ".join(liste)
		fichier.write(chaine)
#		print(chaine)
	
