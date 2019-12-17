from random import randrange
def pmrandom(reponse, CSTE, sup, inf, proposition, update = False):
    """
        Cette fonction joue au jeu du plus ou moins
        au lieu de faire devenir un nombre à l'utilisateur
        c'est elle qui devine le nombre de l'utilisateur
        pour se faire elle determine une borne sup et une borne inf
        puis faire  des propositions aleatoire entre ces bornes
        puisque le programme sera appélé de l'exterieur, on doit à chaque fois
        lui rappeler les anciennes valeurs de inf et sup
            - CSTE définir la bonne sup globale
            - update d'indiquer si on fait une simple mise à jour de sup et inf
            - proposition sert à faire les tests en cas de mise à jour
    """
    
    if reponse == '-':
        sup = proposition
    else:
        if sup != CSTE:
            inf = proposition
    if update:   #besoin que des bornes pour la mise à jour
        return inf, sup
    
    proposition = randrange(inf, sup + 1)
    return proposition

if __name__ == "__main__":
    pmrandom(' ', 1e6)
