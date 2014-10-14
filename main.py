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


functions.init(log) #ajout du fichier de log dans les functions pour le mode verbose
functions.convert("35d", 666)
