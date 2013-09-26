import sqlite3
from CreationDB import GestionBD
from PlayList import PlayList
from Morceau import Morceau

def main():
    ''' connection a la base sqlite RadioLibre '''
    connection = sqlite3.connect('RadioLibre.sqlite3')
    connection.row_factory = sqlite3.Row
    curseur = connection.cursor()
    
    ''' creation de la base (table musique) '''
    base = GestionBD()
    base.CreationBase(curseur)
    
    ''' validation '''
    connection.commit()
    
    # creaton d'une liste de criteres de selection pour recherche dans la table 
    #listeAV = [['genre','Dubstep'],['artiste','Pink Floyd'],['album','Ummagumma']]
    listeAV = [['album','Ummagumma']]
    '''
    appel au module qui permet de faire la recherche dans la table musique en fonction de la liste de criteres 
    et recuperation du curseur resultat 
    '''
    curseur = base.RequeteSelectionMultiple(listeAV, connection)
    
    #for liste in curseur:
    #   print(liste)
    # creation de la playlist avec le resultat de la requete
    
    #variables ici juste pour verification
    ''' temps souhaite de la playlist '''
    temps=1200
    ''' temps cumule '''
    tempsCumule=0
    ''' marge de duree ... '''
    marge = 5/100
    
    ''' la playlist '''
    
    ''' creation de la playlist '''
    unePlayList = PlayList(nom='ma playlist de test')
    
    
    ''' 
    
    >>>>>>
    ICI : les enregistrements resultats de la requete sont ajoutes a la playlist
    <<<<<<
     
    '''
    for ligne in curseur:
        # si la duree de l\'enregistrement en cours ne fait pas depasser le temps souhaite de la playlist, on "prend" le morceau
        if ((ligne["duree"]+tempsCumule)<=(temps*(1+marge))):
            unMorceau=Morceau(ligne["id"],ligne["titre"], ligne["album"], ligne["artiste"], ligne["genre"], ligne["sousgenre"],\
                          ligne["duree"], ligne["format"], ligne["polyphonie"], ligne["chemin"])
            unePlayList.AjoutPlayList(unMorceau)
            tempsCumule+=ligne["duree"]
        # si le temps des morceaux deja enregistres est suffisant on arrete
        if (tempsCumule >= temps):
            break
    
    
    # fin de la connection
    curseur.close()
    connection.close()

    # juste pour verifier:
    for morc in unePlayList.ListMorceaux():
        print(morc.titre,morc.artiste,morc.genre, morc.format, morc.duree, morc.chemin, morc.polyphonie, morc.sousgenre, morc.album)
    

if __name__ == '__main__':
    main()
    