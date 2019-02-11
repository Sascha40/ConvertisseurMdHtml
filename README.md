# Convertisseur(s) 🙃

Il s'agit d'un convertisseur de Markdown vers HTML réalisé sous Python3, en tant que devoir maison pour mon école d'ingénierie informatique.

## Quelles versions ? 

Comme vous avez pu le constater, je dispose de **trois versions** de convertisseur. 

* Une réalisée en `CLI`
* Une assez simpliste ne pouvant gérer qu'une seul fichier à la fois à exécuter en tant que script python simple.
* La troisième version diffère, en effet ce n'est pas une version à proprement parlé, étant donné que nous souhaitons ici faire une conversion de markdown vers html, je me suis lancé le défit de faire l'inverse et de crée mon propre module. Qui une fois finalisé sera open-source et disponible à toute la communautée informatique. Je compte poursuivre ce projet et élaborer ensuite une interface graphique. Pour l'instant seul le module convertisseur est diponible.


## Utilisation de la v1 en `CLI` :
Tout d'abord veuillez installer les librairies suivantes:

* Argparse : `pip3 install argparse` dans un terminal.
* Markdown : `pip3 install markdown`dans un terminal également.

Pour la suite
Ouvrez un terminal avec le fichier `convertisseurV1.py` puis saisissez les commandes suivantes:

- `-i` suivi du nom du fichier Markdown que vous souhaitez convertir 
- `-o` suivi du nom du fichier HTML de destination
- `-h` affiche l'aide de l'application.

Sur mac et linux un `sudo` ou `su` peut se révéler nécessaire, sinon vous n'allez pas avoir l'accès aux fichiers. 
Ce fut mon cas.
Attention la syntaxe est importante lors des `-i`et `-o`pour que cela fonctionne. 
 
## Utilisation de la v2:

* Lancez `convertisseurV2.py` dans votre éditeur/runner préféré ou dans le terminal. 
* Il vous demande le chemin de votre fichier Markdown d'entrée.
* Copiez-collez vos chemins si votre éditeur le permet, sinon vous êtes partis pour une session d'écriture.
* Faites entrer
* Hop, votre fichier source en markdown est converti dans le dossier ou se trouve votre `convertisseurV2.py`.

## Utilisation du futur module-opensource :

* Lancez `convertisseurOpenSource.py` dans votre éditeur/runner préféré ou dans le terminal. 
* Il vous demande le chemin de votre fichier HTML d'entrée, puis le chemin de sauvegarde du fichier Markdown généré.
* Copiez-collez vos chemins si votre éditeur le permet, sinon vous êtes partis pour une session d'écriture.
* Faites entrer
* Votre fichier en markdown est généré. Certaines balises, et traitement ne sont pas parfait. *Beaucoup de travail reste à effectuer.*



