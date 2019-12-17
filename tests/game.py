from enum import Enum

#pour le choix du mot mystere
from random import randrange

#pour gérer le mode deflexion de nos programmes
class Reflexion(Enum):
    STANDARD = 1
    HUMAN = 2

def play_game(reflexion, *programmes):
    """
    Cette fonction effectue une partie  de plus ou moins
    en utilisant des programmes coder pour faire des propositions
        - reflexion permet de decider si les programmes doivent se comporter
          comme des humains ou non.
          Le programme se comporte comme un humain s'il tient compte
          des propositions des autres programmes
    """
    n = len(programmes)  #nombre de programmes jouant
    pasfinir = 1   #pour arrêter la partie en cas de victoire d'un des programmes
    CSTE = 1e6    #constante sup global
    infs = [0]*n   # ensemble des valeurs inf pour chaque programme
    sups = [CSTE]*n   # ensemble des valeurs sup pour chaque programme
   
    propositions = [50]*n   #ensemble des propositions  de chaque programme
    reponses = [' ']*n    #ensemble des reponses obtenu par chaque programme
    i = 0    #pour donner la parole à chaque programme tour à tour
    motMystere = randrange(CSTE + 1)    #initialisation du mot à chercher
    while pasfinir:
        #le programme en cours faire sa propositions
        if reflexion == Reflexion.HUMAN:   #quand on reflexion comme un humain, on fais nos propositions en fonction de la dernière personne à jouer
            propositions[i] = programmes[i](reponses[(i-1)%n], CSTE, sups[i], infs[i], propositions[(i-1)%n])
        else:
            propositions[i] = programmes[i](reponses[i], CSTE, sups[i], infs[i], propositions[i])
        
        #en fonction de la proposition on repond
        if propositions[i] == motMystere:
            break
        elif propositions[i] < motMystere:
            reponses[i] = '+'
        else:
            reponses[i] = '-'
        
        #en fonction du mode de reflexion on fait la/les mise(s) à jour
        if reflexion == Reflexion.STANDARD:
            infs[i], sups[i] = programmes[i](reponses[i], CSTE, sups[i], infs[i], propositions[i], True)
        else:
            for j in range(n):
                infs[j], sups[j] = programmes[j](reponses[i], CSTE, sups[j], infs[j],propositions[i], True)
        i += 1   #on passe au programme suivant
        if i == n:    #on revient au premier programme si tous ont fait une proposition fausse
            i = 0
    
    return i
if __name__ == "__main__":
    import dichotomy, randoms

    #on recupere les programmes qui joueront
    programmes = [dichotomy.pmdichotomie, randoms.pmrandom]
    print(play_game(Reflexion.HUMAN, *programmes))