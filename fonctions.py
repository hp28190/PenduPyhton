#!/usr/bin/python3.7
# -*-coding:Utf8 -*

##########################################################
##Fichier contenant les fonction du jeu du pendu
##
##Fait partie du projet PenduPyhton 
##########################################################

def mot_masque (mot, lettres_trouves):
	"""Cette fonction vérifie et créé un mot avec les lettres trouvé et 
	des étoiles pour celles qui ne le sont pas

	prend en paramètre: - un str contenant le mot 
						- une list contenant les lettres trouvées
						
	"""
	aff_mot = ""
	
	for lettre in mot:
		if lettre in lettres_trouves:
			aff_mot += lettre
		else:
			aff_mot += '*'
	
	#print('Le mot que l\'on cherche est: {0}'.format(aff_mot))
	return aff_mot	

