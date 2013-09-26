import sys
import argparse
from PlayList import PlayList

VERSION=(0, 0, 1)

def main():
    parser = argparse.ArgumentParser(description='Gestion des arguments de la ligne de commande pour la création d\'une playlist', epilog='(c) 2013 GPLv3, Grégory DAVID et Géraldine TAYSSE', prefix_chars='-+')
    parser.add_argument('--version', action='version', version='%(prog)s '+str(VERSION[0])+'.'+str(VERSION[1])+'.'+str(VERSION[2]))
    parser.add_argument('-m', '--m3u', action='store_true')
    parser.add_argument('-x', '--xspf', action='store_true')
    parser.add_argument('-p', '--pls', action='store_true')
    parser.add_argument('-g', '--genre', action='append', nargs=2)
    parser.add_argument('-s', '--sousgenre', action='append', nargs=2)
    parser.add_argument('-a', '--artiste', action='append', nargs=2)
    parser.add_argument('-A', '--album', action='append', nargs=2)
    parser.add_argument('-t', '--titre', action='append', nargs=2)
    parser.add_argument('-T', '--temps', action='store')
    parser.add_argument('-M', '--marge', action='store')
    parser.parse_args()

    unePlayList = PlayList(nom='une playlist')
    print(unePlayList.getNom())
    
    
if __name__ == '__main__':
    min_version = (3,2)
    if sys.version_info < min_version :
        print("Python %i.%i est requis pour " % (min_version[0],min_version[1]))
        sys.exit(1)
    main()
