#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''importation des bibliotheques nescessaires'''
from config import *

'''argparse'''
'''parser = argparse()
scan = parser.parse_args() #la variable 'scan' conservera l'ensemble des arguments'''

'''logging'''
fmt = "%(levelname)s %(asctime)s : %(message)s"
datefmt="%d/%M/%Y - %I:%M"
log = logging('playlist.log', True, fmt, datefmt)

###############################################

for ARG in ['name', 'format', 'length']:
	elem = getattr(scan, ARG)
	if elem is not None:
		logging.debug(ARG+" : "+elem)
		if(scan.verbose):
			print("DEBUG : "+ARG+" : "+elem)

validOptArgs[5]
i = 0

for ARG in ['genre', 'susgenre', 'artist', 'album', 'title']:
	elem = getattr(scan, ARG)
	if elem is not None:
		logging.debug(ARG+" : \n-1 : "+elem[0]+"\n-2 : "+elem[1]) #affiche la valeur envoyee pour chaque argument
		convert(elem[1], 666) #convertit l'argument 2 (pourcentage) en un entier
		validOptArgs[i] = chkValue(elem[1], 0, 101) #verifie si la valeur absolue de l'argument 2 est compris entre 1 et 100
	
		#idee: partir avec un len() pour l'addition de deux valeurs (au minimum)
		#correction: regrouper toutes les saisies dans un match, puis ensuite totaliser les entiers
		
	#if match.group(elem[i]):
		validOptArgs[i] = len(elem[1])
		if len(elem[1]) > 100:
			logging.warning(elem[1]+" is higher than 100")
			logging.info("Please, retry the process") #
		#else:
			#transformer les saisies en données pour la transformation en playlist




'''if(scan.genre):
    #le genre est donc renseigne
    if(diffType(scan.genre[0], "str")):'''
        


'''scan.genre[1] = convert(scan.genre[1], 666)
scan.sgenre[1] = convert(scan.sgenre[1], 666)
scan.artiste[1] = convert(scan.artiste[1], 666)
scan.album[1] = convert(scan.album[1], 666)
scan.titre[1] = convert(scan.titre[1], 666)'''
