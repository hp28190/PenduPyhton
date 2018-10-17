#!/usr/bin/python3.7
# -*-coding:Utf8 -*

############################################
##Fichier du jeu du pendu fait par LOUIS Maxime
##
##Dans le cadre du cours sur python d'openclassroom
#############################################

import random

print("Bienvenu dans le jeu du pendu. \n")

print('Chargement des fichiers\n')

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
	
if joueur not in scores.keys()
	score[joueur] = 0
	







############## Sauvegarde des scores, peut être faire une fonction
with open ('score', 'wb') as fichier_score:
	pickle = pickle.pickler(fichier_score)
	pickle.dump(scores)
	

os.system("pause")