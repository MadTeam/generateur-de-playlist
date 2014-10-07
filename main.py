#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''importation des bibliotheques nescessaires'''
import argparse
import logging

'''definition des fonctions'''
def diffType(value, typeOfValue): #compare le type d'une variable avec une autre
	if type(value) == type(typeOfValue):
		return True
	else:
		return False

def convert(variable, typeOfVariable, verbose=False): #convertit une variable a un type choisi (returne une exception si la conversion echoue)
	try:
		if type(typeOfVariable) == type(666):
			variable = int(variable)
			return variable
	except ValueError:
		logging.error("converting of "+variable+" to integer failed")
		if verbose:
			print("ERROR : converting of "+variable+" to integer failed")
		return False
    
def chkValue(variable, minValue, maxValue, verbose=False): #verifie si la valeur absolue d'une variable est comprise strictement entre deux valeur
	try:
		variable = abs(variable)
		if minValue < variable < maxValue:
			logging.info("the argument value of "+variable+" is accepted")
			if verbose:
				print("INFO : the argument value of "+variable+" is accepted")
			return True
		else:
			variable = None
			logging.warning("the argument value of "+variable+" is invalid")
			if verbose:
				print("WARNING : the argument value of "+variable+" is invalid")
			return False
	except ValueError:
		logging.error("converting of "+variable+" to absolute integer failed")
		if verbose:
			print("ERROR : converting of "+variable+" to absolute integer failed")
		return False

'''configuration du fichier de log'''
logging.basicConfig(filename="journal.log", level=logging.DEBUG)

'''configuration du parser'''
parser = argparse.ArgumentParser(prog="Personal playlist generator", add_help=False, description="WIP", epilog="note : le generateur accepte les expressions regulieres dans les arguments optionnels", prefix_chars='-')
obli = parser.add_argument_group("Arguments obligatoires ", "Obligatoires pour genere la playlist")
opt = parser.add_argument_group("Arguments optionnels ", "Ils permettent d'obtenir un pourcentage sur un critere specifique (ex: --genre rock 70 => 70% de la playlist sera composee de rock)")

'''arguments positionnels'''
obli.add_argument("name", help="output name of file")
obli.add_argument("format", help="output format of file (xspf, m3u, pls available)", choices=["xspf", "m3u", "pls"])
obli.add_argument("length", help="total length of the playlist ('h' to hour, 'm' to minute)")

'''arguments optionnels'''
opt.add_argument("-h", "--help", help="show help", action="help")
opt.add_argument("-v", "--verbose", help="all informations will be visible like debug information", action="store_true")
opt.add_argument("-G", "--genre", nargs=2, help="genre and percentage of genre")
opt.add_argument("-g", "--subgenre", nargs=2, help="subgenre and percentage of subgenre")
opt.add_argument("-a", "--artist", nargs=2, help="artist and percentage of artist")
opt.add_argument("-A", "--album", nargs=2, help="album and percentage of album")
opt.add_argument("-t", "--title", nargs=2, help="title ad percentage of title")

scan = parser.parse_args() #la variable 'scan' conservera l'ensemble des arguments	

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
		
	if len(elem): #idee: partir avec un len() pour l'addition de deux valeurs (au minimum)    
		validOptArgs[i] = len(elem[1])
		if len(elem[1]) > 100:
			logging.warning(elem[1]+" is higher than 100")
			logging.info("Please, retry the process")




'''if(scan.genre):
    #le genre est donc renseigne
    if(diffType(scan.genre[0], "str")):'''
        


'''scan.genre[1] = convert(scan.genre[1], 666)
scan.sgenre[1] = convert(scan.sgenre[1], 666)
scan.artiste[1] = convert(scan.artiste[1], 666)
scan.album[1] = convert(scan.album[1], 666)
scan.titre[1] = convert(scan.titre[1], 666)'''
