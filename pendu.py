#!/usr/bin/python3.7
# -*-coding:Utf8 -*

############################################
##Fichier du jeu du pendu fait par LOUIS Maxime
##
##Dans le cadre du cours sur python d'openclassroom
#############################################
#############Déclaration nécessaires
import random
import os



print("Bienvenu dans le jeu du pendu. \n")
print('Chargement des fichiers\n')

#####Vérification de la présence des fichiers
if not os.path.exists('scores'):	##créé le fichier seulement si il n'existe pas
	fichier = open("scores",'w')
	close(fichier)


#####Chargement des scores
with open('score', 'rb') as fichier_score:
	depickler = pickle.Unpickler(fichier_score)
	scores = depickler.load()
	
#####Chargement du dictionnaire et du nombre de coups
with open('donnees.py', 'rb') as fichier_donnees:
	depickler = pickle.Unpickler(fichier_donnees)
	chances = depickler.load()	
	mots = depickler.load()
	

print('Fin du chargement des fichiers\n')

joueur = input('Saisir votre nom de joueur')
	
if joueur not in scores.keys():
	score[joueur] = 0
else:
	print('Rebonjour {0}, votre score actuel est de {1} points',.format(joueur , score[joueur]

#########################Choix du mot et début du jeu
while arret != 'o'
tentatives = 0

while tentative < chances and mot_trouve 
	







############## Sauvegarde des scores, peut être faire une fonction
with open ('score', 'wb') as fichier_score:
	pickle = pickle.pickler(fichier_score)
	pickle.dump(scores)
	

os.system("pause")