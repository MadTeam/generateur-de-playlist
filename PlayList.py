#from Morceau import Morceau 

class PlayList():
    '''
    Description de la classe PlayList
    '''
    __duree = int()
    __nom = str()
    __marge = int()
    ''' __Liste d'objets Morceau '''
    __listMorceaux = list()
    
    def __init__(self, duree=0, nom='',marge=0):
        '''
        Constructeur avec initialisation de la duree, du titre et de la marge de la playlist
        '''
        self.__duree = duree
        self.__nom = nom
        self.__marge = marge
        
        
    def Marge(self):
        ''' la marge de la playlist '''
        return self.__marge
    
    def Nom(self):
        ''' le nom de la playlist'''
        return self.__nom
    
    def Duree(self):
        ''' la duree de la playlist'''
        return self.__duree
    
    def ListMorceaux(self):
        ''' la liste des morceaux composant la playlist'''
        return self.__listMorceaux
    
    
    # Methodes
    
    
    ''' Methode d\'ajout d'un morceau en fin de la playlist'''
    def AjoutPlayList(self, morceau):  #ajout en fin de liste
        self.__listMorceaux.append(morceau)
        
    '''Methode d'\ajout d'un morceau a un endroit precis dans la playlist '''
    def AjoutPlayListIndex(self, index, morceau):
        self.__listMorceaux.insert(index, morceau)
        
    ''' Methode de suppression d\'un morceau de la playlist'''
    def SuppressionList(self, morceau):
        if (morceau in self.__listMorceaux):
            self.__listMorceaux.remove(morceau)
            print('suppression effectuee')
        else:
            print ('erreur : suppression impossible => morceau non trouve !')
    
    ''' Renvoi le nombre de morceaux de la playlist '''
    def NombreMorceaux(self):
        return len(self.__listMorceaux)
