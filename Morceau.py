'''
Proposition d'une classe pour définir la notion de morceau.

    Morceau.py, exemple d'utilisation
    Copyright (C) 2012-2014  Grégory DAVID, Géraldine TAYSSE

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

class Morceau(object):
    __titre = str()
    __album = str()
    __artiste = str()
    __genre = str()
    __sousgenre = str()
    __duree = int()
    __polyphonie = int()
    __format = str()
    __chemin = str()

    def __init__(self, titre, album, artiste, genre, sousgenre, duree, polyphonie, file_format, chemin):
        self.__titre = titre
        self.__album = album
        self.__artiste = artiste
        self.__genre = genre
        self.__sousgenre = sousgenre
        self.__duree = duree
        self.__polyphonie = polyphonie
        self.__format = file_format
        self.__chemin = chemin

    @property
    def titre(self):
        '''Le titre du morceau'''
        return self.__titre

    @property
    def album(self):
        '''L\'album duquel le morceau fait partie'''
        return self.__album

    @property
    def artiste(self):
        '''Nom de l\'artiste principal ou du groupe du morceau'''
        return self.__artiste

    @property
    def genre(self):
        '''Genre du morceau'''
        return self.__genre

    @property
    def sousgenre(self):
        '''Sous-genre du morceau'''
        return self.__sousgenre

    @property
    def duree(self):
        '''Duree du morceau en secondes'''
        return self.__duree

    @property
    def polyphonie(self):
        '''Polyphonie du morceau (1=mono, 2=stereo, 6=5.1, etc.)'''
        return self.__polyphonie

    @property
    def format(self):
        '''Format d\'encodage des donnees (MP3, OGG Vorbis, FLAC, etc.)'''
        return self.__format

    @property
    def chemin(self):
        '''Chemin d\'acces au fichier'''
        return self.__chemin

    
