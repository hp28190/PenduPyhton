#!/usr/bin/python3.7
# -*-coding:Utf8 -*


#Fichier du jeu du pendu fait par LOUIS Maxime
#
#Dans le cadre du cours sur python d'openclassroom

#Déclaration nécessaires
import random
import pickle
import os
import donnees
from fonctions import mot_masque

print("Bienvenu dans le jeu du pendu. \n")
print('Chargement des fichiers\n')

#Vérification de la présence des fichiers
if not os.path.exists('scores'):	#créé le fichier seulement si il n'existe pas
	fichier = open("scores",'w')
	fichier.close()
	scores = {}
else:
#Chargement des scores
	with open('scores', 'rb') as fichier_score:
		depickler = pickle.Unpickler(fichier_score)
		scores = depickler.load()
	
#Chargement du dictionnaire et du nombre de coups
#with open('donnees.py', 'rb') as fichier_donnees:
#	depickler = pickle.Unpickler(fichier_donnees)
#	chances = depickler.load()	
#	mots = depickler.load()
	

print('Fin du chargement des fichiers\n')

joueur = input('Saisir votre nom de joueur\n')
	
if joueur not in scores.keys():
	scores[joueur] = 0
else:
	print("Rebonjour {0}, votre score actuel est de {1} points\n".format(joueur, scores[joueur]))

#Choix du mot et début du jeu
fin_partie = 'n'

while fin_partie != 'o' :
	tentatives = 0
	lettres =[]
	#mot = mots[random.randrange(mots.len())]
	mot = random.choice(donnees.mots)
	mot_trouve = ""
	
	while tentatives < donnees.chances and mot_trouve != mot :
		lettre = input('Quelle lettre voulez vous essayer?\n')
		
		if lettre in lettres:
			print('Vous avez déja saisi cette lettre')
		else:
			lettres.append(lettre)
			if lettre in mot: 
				print('Bravo la lettre ',lettre,' est dans le mot que l\'on cherche.\n')
				tentatives += 1
				#######affichage mot actuel
				#affichage_mot_masque(mot, lettres)
				mot_trouve = mot_masque(mot, lettres)
				print('Le mot que l\'on cherche est: {0}'.format(mot_trouve))
				print('il vous reste',donnees.chances-tentatives,'chances de le trouver')
			else:
				print('Dommage cette lettre ne fait pas partie de notre mot\n')
				tentatives +=1
				######Affichage mot actuel
				#affichage_mot_masque(mot, lettres)
				mot_trouve = mot_masque(mot, lettres)
				print('Le mot que l\'on cherche est: {0}'.format(mot_trouve))
				print('il vous reste',donnees.chances-tentatives,'chances de le trouver')			

	if mot_trouve == mot :
		print('Bravo vous avez trouver le bon mot\n')
	else:
		print('Dommage vous n\'avez pas trouver le mot, qui était: {0}\n'.format(mot))
	
	scores[joueur] += donnees.chances-tentatives
	fin_partie = input('Voulez vous arreter? (o/n)')
############## Sauvegarde des scores, peut être faire une fonction
with open ('scores', 'wb') as fichier_score:
	pickle = pickle.Pickler(fichier_score)
	pickle.dump(scores)
	

os.system("pause")