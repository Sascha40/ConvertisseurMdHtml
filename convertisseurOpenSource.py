listeHtml = ['<h1>','<h2>','<h3>','<em>','</em>','<ul>','<li>','<a>','</a>','<br>','<a','>','<u>','</u>','<strong>','</strong>']
listeMd = ['# ','## ','### ','**','**','* ','	*','[',']','\n','[',']','__','__','**','**']
listeNonDésirés = ['<!DOCTYPE', 'html>','<html>','<head>','</head>','</h1>','</h2>','</h3>','</li>','<p>','</p>''</img>','href=','</ul>','</body>','</html>','<body>','<title>','</title>','</ol>']
with open(input("Veuillez entrez le chemin de votre fichier .html à convertir en markdown: ")) as fichierHtml:
	fichier = open('Fichier_Converti_vers_Markdown.md','w')
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
	
    '''
    Copyright (C) <2019>  <Sallès Sascha>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
    
    '''
