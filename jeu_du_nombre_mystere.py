"""
Jeux du nombre mystère
Créé le Samedi 7 novembre 2020
auteur: LEMOINE Maxime - première
jeu_du_nombre_mystere.py
"""

# -*- coding: utf-8 -*-
from random import randint
nombre_essai=0


#choix du type de partie
choixpartie=""
while choixpartie!="1" and choixpartie!="2":
    print("---- Type de partie ----")
    print("Trouver le nombre de l'ordinateur : 1\nL'ordinateur doit trouver votre nombre : 2")
    choixpartie=input("> ")


#si on choisit "Trouver le nombre de l'ordinateur"
if choixpartie=="1" :
    #initialisation
    nombre_bot=randint(0,1000)
    nombre_player=""
    print("\n\n\nTrouvez le nombre entre 0 et 1000 :")

    #boucle de la partie
    while nombre_player!=nombre_bot:
        try:#permet d'éviter une erreur si le joueur ne met pas un nombre
            nombre_player=int(input("> "))
            if nombre_player < nombre_bot:
                nombre_essai+=1
                print("plus grand")
            elif nombre_player > nombre_bot:
                nombre_essai+=1
                print("plus petit")
        except:
            continue

    print("Tu as trouvé le nombre ({}) en {} essais.".format(nombre_bot,nombre_essai+1))


#si on choisit "L'ordinateur doit trouver votre nombre"
elif choixpartie=="2" :
    #initialisation
    nombre_moins=0
    nombre_plus=1001 #si la limite n'est pas 1001, l'ordinateur ne pourra jamais trouver le nombre 1000
    nombre_bot=500
    choix_player=""
    print("\n\n\nPensez à un nombre entre 0 et 1000.")
    print('"+" : votre nombre est plus grand\n"-" : votre nombre est plus petit\n"=" : l\'ordinateur a trouvé votre nombre')
    input("[Appuyez sur Entré pour continuer]\n")

    #boucle de la partie
    while choix_player!="=":
        print(nombre_bot)
        choix_player=input("> ")
        if choix_player=="+":
            nombre_essai+=1
            #calcul permettant au bot de trouver forcement le nombre
            nombre_moins=nombre_bot
            nombre_bot=int(((nombre_plus-nombre_moins)/2)+nombre_bot)
        elif choix_player=="-":
            nombre_essai+=1
            #calcul permettant au bot de trouver forcement le nombre
            nombre_plus=nombre_bot
            nombre_bot=int((nombre_bot-(nombre_plus-nombre_moins)/2))

    print("L'ordinateur a trouvé ton nombre ({}) en {} essais.".format(nombre_bot,nombre_essai+1))

input("[Appuyez sur Entré pour arrêter.]") #pour empêcher la fermeture instantanée du programme
