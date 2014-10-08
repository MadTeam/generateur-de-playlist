#!/usr/bin/python3
# -*- coding: utf-8 -*-

import logging

class log:
	logger = logging.getLogger() #permet d'obtenir le logger 'root'
	formatter = None #formattage de l'affichage
	handler = None #sortie de l'affichage (stdout, fichier, etc...)

	def __init__(self):
		self.logger.setLevel(0)
		handler 

	def __init__(self, level=0, formatStr=None, mode=0, pathFile=None):
		self.logger.setLevel(level)

		if formatStr is not None:
			self.formatter = logging.Formatter(formatStr)

		if mode is not None:
			if mode == 0:
				#pas de fichier de log
				self.handler = logging.StreamHandler()
			elif mode == 1:
				self.handler = logging.FileHandler(pathFile)
				#fichier de log uniquement
			elif mode == 2:
				self.handler = list()
				self.handler.append(logging.StreamHandler())
				self.handler.append(logging.FileHandler(pathFile))
				#fichier de log + stdout
			self.handler.setLevel(level)

	

	def const(self): #construit le logger selon les paramètres d'initialisation
		if type(self.handler) is type(list()):
			self.handler[0].setFormatter(self.formatter)
			self.handler[1].setFormatter(self.formatter)
			self.logger.addHandler(self.handler[0])
			self.logger.addHandler(self.handler[1])
		else:
			self.handler.setFormatter(self.formatter)
			self.logger.addHandler(self.handler)
		return self.logger
'''
class functions:
	def diffType(value, typeOfValue): #compare le type d'une variable avec une autre
		if type(value) is type(typeOfValue):
			return True
		else:
			return False

	def convert(variable, typeOfVariable): #convertit une variable a un type choisi (returne une exception si la conversion echoue)
		try:
			if type(typeOfVariable) is type(666):
				variable = int(variable)
				return variable
		except ValueError:
			logging.error("converting of "+variable+" to integer failed")
			return False

	def chkValue(variable, minValue, maxValue): #verifie si la valeur absolue d'une variable est comprise strictement entre deux valeur
		try:
			variable = abs(variable)
			if minValue < variable < maxValue:
				logging.info("the argument value of "+variable+" is accepted")
				return True
			else:
				variable = None
				logging.warning("the argument value of "+variable+" is invalid")
				return False
		except ValueError:
			logging.error("converting of "+variable+" to absolute integer failed")
			return False


class parser:
	import argparse

	parser = argparse.ArgumentParser(prog="Personal playlist generator", add_help=False, description="WIP", epilog="note : le generateur accepte les expressions regulieres dans les arguments optionnels", prefix_chars='-')
	obli = parser.add_argument_group("Arguments obligatoires ", "Obligatoires pour genere la playlist")
	opt = parser.add_argument_group("Arguments optionnels ", "Ils permettent d'obtenir un pourcentage sur un critere specifique (ex: --genre rock 70 => 70% de la playlist sera composee de rock)")

	''''''arguments positionnels''''''
	obli.add_argument("name", help="output name of file")
	obli.add_argument("format", help="output format of file (xspf, m3u, pls available)", choices=["xspf", "m3u", "pls"])
	obli.add_argument("length", help="total length of the playlist ('h' to hour, 'm' to minute)")

	''''''arguments optionnels''''''
	opt.add_argument("-h", "--help", help="show help", action="help")
	opt.add_argument("-v", "--verbose", help="all informations will be visible like debug information", action="store_true")
	opt.add_argument("-G", "--genre", nargs=2, help="genre and percentage of genre")
	opt.add_argument("-g", "--subgenre", nargs=2, help="subgenre and percentage of subgenre")
	opt.add_argument("-a", "--artist", nargs=2, help="artist and percentage of artist")
	opt.add_argument("-A", "--album", nargs=2, help="album and percentage of album")
	opt.add_argument("-t", "--title", nargs=2, help="title ad percentage of title")

	scan = parser.parse_args() #la variable 'scan' conservera l'ensemble des arguments'''
