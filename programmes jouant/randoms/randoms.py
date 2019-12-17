#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      HP
#
# Created:     16/12/2019
# Copyright:   (c) HP 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from random import randrange
def pmrandomsolve():
    """
        Cette fonction joue au jeu du plus ou moins
        au lieu de faire devenir un nombre à l'utilisateur
        c'est elle qui devine le nombre de l'utilisateur
        pour se faire elle determine une borne sup et une borne inf
        puis faire  des propositions aleatoire entre ces bornes
    """

    CSTE = 1e6 #constante qui doit être superieure au nombre choisir
                #pour que le programme fonctionne correctement
                #dans le cas sans intervalle
    #dialogue introductif
    print("Bonjour je m'appelle Searchbot")
    print("Mon but est de trouver un nombre entier positif que vous aurez choisir")
    print("Si mon nombre est inférieur  au votre, taper '+' ")
    print("s'il est plus grand taper '-' ")
    print("et '=' si j'ai trouver")
    print("Voulez-vous me donner un intervalle ou chercher le nombre")
    print("Tapeze 'O' ou 'o' pour oui...")
    reponse = input()   #choix du mode de jeu, avec intervalle ou sans intervalle
    incorrect = True
    if reponse.upper() == 'O':  #parametrage pour un jeu avec intervalle
        while incorrect:
            print("Donner la borne inferieure") #saisie de la bonne inf
            try:    #on s'assure que la valeur entree est correcte
                inf = int(input())
                assert(inf >= 0)
                incorrect = False
            except  AssertionError:
                print("un entier positif s'il vous plait")
            except:
                print("un nombre s'il vous plait")
        incorrect = True
        while incorrect:
            print("Donner la borne superieure") #saisie de la borne sup
            try:    #on s'assure que la valeur entree est correcte
                sup = int(input())
                assert(sup > inf)
                incorrect = False
            except  AssertionError:
                print("un entier plus grand que la borne inferieure s'il vous plait")
            except:
                print("un nombre s'il vous plait")
        proposition = randrange(inf, sup + 1)    #initialisation de la 1ere proposition

    else:   #parametrage pour un jeu sans intervalle
        inf = 0 #initialisation de la borne inf
        proposition = 50    #initialisation de la 1ere proposition
        sup = CSTE  #initialisation de la borne sup
    trouve = '-'

    print(" c'est partir, voici ma première proposition")   #debut du jeu

    while trouve != '=':
        print(int(proposition)) #affichage de la proposition
        trouve = input()    #recuperation de la reponse de l'utilisateur
        if trouve not in '-+=': #on s'assure que l'utilisateur a faire unensaisie correcte
            print("Ah ah tu te moque de moi")
            print('j\'arrete')
            break
        if trouve == '-':
            sup = proposition - 1
        elif trouve == '+':
            if sup != CSTE:
                inf = proposition + 1
        else:
            print("Hourra j'ai trouver")
        proposition = randrange(inf, sup + 1)

if __name__ == "__main__":
    pmrandomsolve()
