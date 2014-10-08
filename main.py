#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''importation des bibliotheques nescessaires'''
#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''importation des bibliotheques nescessaires'''
from config import log

'''logging'''
one = log(10, "%(levelname)s %(asctime)s : %(message)s", 0)
logger = one.const();

logger.debug("test")

'''logging.basicConfig(filename="journal.log", level=logging.DEBUG, format="%(levelname)s %(asctime)s : %(message)s", datefmt="%d/%M/%Y - %I:%M")
logger = logging.getLogger()
handler = logging.StreamHandler()
handler.setLevel(10)'''
