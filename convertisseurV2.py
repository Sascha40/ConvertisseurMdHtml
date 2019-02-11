from markdown import *
fichiermd = open(input("Entrez le chemin de votre fichier markdown à convertir en HTML")) 
fichierHTML = open('fichier_converti_en_html.html','w') 
for ligne in fichiermd:    
	html = markdown(ligne)  
	fichierHTML.write(html) 