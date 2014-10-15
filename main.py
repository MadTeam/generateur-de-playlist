#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''importation des bibliotheques nescessaires'''
from config import *

'''argparse'''
parser = argparse()
scan = parser.parse_args() #la variable 'scan' conservera l'ensemble des arguments

'''logging'''
fmt = "%(levelname)s %(asctime)s : %(message)s"
datefmt="%d/%m/%Y - %H:%M:%S"
log = logging('playlist.log', scan.verbose, fmt, datefmt)

for ARG in ['name', 'format', 'length']:
	elem = getattr(scan, ARG)
	if elem is not None:
		log.debug(ARG+" -> "+elem)

functions.init(log)

for ARG in ['genre', 'subgenre', 'artist', 'album', 'title']:
	i = 0
	if getattr(scan, ARG) is not None:
		elem = getattr(scan, ARG)
		
#############################""""
		while i < len(elem):
			log.debug(ARG+" : \n\t-1 : "+str(elem[0])+"\n\t-2 : "+str(elem[1])) #affiche la valeur envoyee pour chaque argument
			elem[1] = functions.convert(elem[1], 666) #convertit l'argument 2 (pourcentage) en un entier
			functions.chkValue(elem[1], 0, 101) #verifie si la valeur absolue de l'argument 2 est compris entre 1 et 100
		




'''if(scan.genre):
    #le genre est donc renseigne
    if(diffType(scan.genre[0], "str")):'''
        


'''scan.genre[1] = convert(scan.genre[1], 666)
scan.sgenre[1] = convert(scan.sgenre[1], 666)
scan.artiste[1] = convert(scan.artiste[1], 666)
scan.album[1] = convert(scan.album[1], 666)
scan.titre[1] = convert(scan.titre[1], 666)'''
