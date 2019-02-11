from markdown import *
import argparse
import os

parser = argparse.ArgumentParser(description = "Utilitaire de conversion de fichiers Markdown en fichiers Html")
parser.add_argument("-i", "--input_file", type = str, metavar = " ", required = True, help = "Entrez le chemin de votre dossier qui contient vos fichiers en markdown qui seront convertis en HTML ")
parser.add_argument( "-o", "--output_file", type = str, metavar = " ", required = True, help = "Entrez le chemin où vous souhaitez sauvegarder vos pages HTML fraichement converties.")
args = parser.parse_args()
							
def convertir():
	dossiermd = os.listdir(args.input_file)
	fichierHtml = open('converti.html','w')
	fichierHtml.write("<meta charset='UTF-8'>")
	for fichiers in dossiermd:
		with open(f'{args.input_file}/{fichiers}') as fichiermd:
			html = markdown(fichiermd.read())
			fichierHtml.write(html)
	

convertir()