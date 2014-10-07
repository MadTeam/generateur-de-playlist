#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''importation des bibliotheques nescessaires'''
import argparse
import logging

'''definition des fonctions'''
def diffType(value, typeOfValue): #compare la valeur d'une variable avec celui decide
	if type(value) == type(typeOfValue):
		return True
	else:
		return False

def convert(variable, typeOfVariable): #convertit une variable a un type choisi (returne une exception si la conversion echoue)
	try:
		if type(typeOfVariable) == type(666):
			variable = int(variable)
			return variable
	except ValueError:
		logging.error(variable+"'s convert to int failed")
		return False
    
def chkValue(variable, minValue, maxValue): #verifie si la valeur d'une variable est comprise entre deux valeur
	try:
		variable = abs(variable)
		if minValue < variable < maxValue:
			logging.info("argument "+variable+" accepted")
			return True
		else:
			variable = None
			logging.warning("argument value of "+variable+" is invalid")
			return False
	except ValueError:
		logging.error()
		return False

'''configuration du fichier de log'''
logging.basicConfig(filename="journal.log", level=logging.DEBUG);

'''configuration du parser'''
parser = argparse.ArgumentParser(prog="Generateur de playlist personnalisee | Personal playlist generator", description="WIP", epilog="note : le generateur accepte les expressions regulieres dans les arguments optionnels", prefix_chars='-+')
obli = parser.add_argument_group("Arguments obligatoires ", "Obligatoires pour genere la playlist")
opt = parser.add_argument_group("Arguments optionnels ", "Ils permettent d'obtenir un pourcentage sur un critere specifique (ex: --genre rock 70 => 70% de la playlist sera composee de rock)")

'''arguments positionnels'''
obli.add_argument("nom", help="le nom de sortie du fichier")
obli.add_argument("format", help="le format de sortie du fichier (xspf, m3u, pls disponible)", choices=["xspf", "m3u", "pls"])
obli.add_argument("duree", help="la duree totale de la playlist ('h' pour heure, 'm' pour minute)")

'''arguments optionnels'''
'''opt.add_argument("-h", "-H", "--help", "--aide", action="help")'''
opt.add_argument("-G", "--genre", nargs=2, help="le genre et le pourcentage")
opt.add_argument("-g", "--sousgenre", nargs=2, help="le sous-genre et le pourcentage")
opt.add_argument("+a", "++artiste", nargs=2, help="l'artiste et le pourcentage")
opt.add_argument("+A", "++album", nargs=2, help="l'album et le pourcentage")
opt.add_argument("+t", "++titre", nargs=2, help="le titre et le pourcentage")


scan = parser.parse_args() #la variable 'scan' conservera l'ensemble des arguments
logging.debug("list of arguments : ") #logging de la liste des arguments

for ARG in ['nom', 'format', 'duree']:
	elem = getattr(scan, ARG)
	if elem is not None:
		logging.debug(ARG+" : "+elem[0])

validOptArgs[5]
i = 0

for ARG in ['genre', 'sousgenre', 'artiste', 'album', 'titre']:
	elem = getattr(scan, ARG)
	if elem is not None:
		logging.debug(ARG+" : \n-1 : "+elem[0]+"\n-2 : "+elem[1]) #affiche la valeur envoyee pour chaque argument
		convert(elem[1], 666) #convertit l'argument 2 (pourcentage) en un entier
		validOptArgs[i] = chkValue(elem[1], 0, 101) #verifie si la valeur absolue de l'argument 2 est compris entre 1 et 100
		i++


'''
if(scan.genre):
    #le genre est donc renseigne
    if(diffType(scan.genre[0], "str")):'''
        


'''scan.genre[1] = convert(scan.genre[1], 666)
scan.sgenre[1] = convert(scan.sgenre[1], 666)
scan.artiste[1] = convert(scan.artiste[1], 666)
scan.album[1] = convert(scan.album[1], 666)
scan.titre[1] = convert(scan.titre[1], 666)'''
