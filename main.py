import random
import os
from itertools import islice
from link import set_joueur, Math, Anglais, ScNat, Francais, Deutsch
from def_sauv import sauvegarder_auto, charger_sauvegarde, ajouter_joueur, Level_up, selectionner_joueur

def calcule_pourcentage(nombre, nombre_total):
    return (nombre / nombre_total) * 100

# bouton
boutton_ScNat = False
boutton_ScNat_i_elementen_namen = False
boutton_ScNat_i_elementen_ordnungszahl = False

boutton_Français = False
boutton_Français_i_diffi = False

boutton_Deutsch = False
boutton_Deutsch_i_merkmale_von_Kurzgeschichten = False
boutton_Deutsch_i_merkmale_von_Kurzgeschichten_alle = True

boutton_Anglais = False
boutton_Anglais_i_voc_easy = False
boutton_Anglais_i_voc_impossible = False

boutton_Math = False
boutton_Math_i_base = False

# Menu principal
menu = []
running = True
connection = False
while running:
    donnees = charger_sauvegarde()
    while not connection:
        print("=== ONE ===")
        nom = input("Entrez votre nom : ")
        mot_de_passe = input("Entrez votre mot de passe : ")
        joueur = selectionner_joueur(donnees, nom, mot_de_passe)
        if joueur is None:
            creer = input("Joueur introuvable. Voulez-vous créer un nouveau joueur ? (o/n) ")
            if creer.lower() == "o":
                if ajouter_joueur(donnees, nom, mot_de_passe):
                    print("Joueur créé avec succès.")
                    joueur = donnees["joueurs"][nom]
                    sauvegarder_auto(donnees)
                else:
                    print("Erreur lors de la création du joueur.")
                    continue
            else:
                exit()
        connection = True
        set_joueur(joueur)

    # configuration des boutons
    choix = None
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Bienvenue, {nom} !")
        print("Tu veux faire quoi ?")
        print("-" * 40)
        if boutton_ScNat == True:
            print(f"1. ScNat (ON)")
            if boutton_ScNat_i_elementen_namen == True:
                print("    1.1. Name der elemente (ON)")
            else:
                print("    1.1. Name der elemente (OFF)")
            if boutton_ScNat_i_elementen_ordnungszahl == True:
                print("    1.2. Ordnungszahl der elemente (ON)")
            else:
                print("    1.2. Ordnungszahl der elemente (OFF)")
        elif boutton_ScNat == False:
            print(f"1. ScNat (OFF)")

        if boutton_Français == True:
            print(f"2. Francais (ON)")
            if boutton_Français_i_diffi == True:
                print("    2.1. vocabulair (niv: diffi) (ON)")
            else:
                print("    2.1. vocabulair (niv: diffi) (OFF)")
        else:
            print(f"2. Francais (OFF)")

        if boutton_Deutsch == True:
            print(f"3. Deutsch (ON)")
            if boutton_Deutsch_i_merkmale_von_Kurzgeschichten == True:
                print("    3.1. Merkmale von Kurzgeschichten (einfach) (ON)")
            else:
                print("    3.1. Merkmale von Kurzgeschichten (einfach) (OFF)")
            if boutton_Deutsch_i_merkmale_von_Kurzgeschichten_alle == True:
                print("    3.2. Merkmale von Kurzgeschichten (Schwer) (ON)")
            else:
                print("    3.2. Merkmale von Kurzgeschichten (Schwer) (OFF)")
        elif boutton_Deutsch == False:
            print(f"3. Deutsch (OFF)")

        if boutton_Anglais == True:
            print(f"4. Anglais (ON)")
            if boutton_Anglais_i_voc_easy == True:
                print("    4.1. Easy voc (ON)")
            else:
                print("    4.1. Easy voc (OFF)")
            if boutton_Anglais_i_voc_impossible == True:
                print("    4.2. Impossible voc (ON)")
            else:
                print("    4.2. Impossible voc (OFF)")
        elif boutton_Anglais == False:
            print(f"4. Anglais (OFF)")
        
        if boutton_Math == True:
            print(f"5. Math (ON)")
            if boutton_Math_i_base == True:
                print("    5.1. Base math (ON)")
            else:
                print("    5.1. Base math (OFF)")
        else:
            print(f"5. Math (OFF)\n")
        print("-" * 40)
        print("Appuie sur Entrée pour lancer le quiz avec les modes sélectionnés.")
        choix = input("Entrer votre réponse (tape 1-5 pour basculer): ").strip()
        if choix == "1":
            boutton_ScNat = not boutton_ScNat
        elif choix == "1.1":
            boutton_ScNat_i_elementen_namen = not boutton_ScNat_i_elementen_namen
        elif choix == "1.2":
            boutton_ScNat_i_elementen_ordnungszahl = not boutton_ScNat_i_elementen_ordnungszahl
        elif choix == "2":
            boutton_Français = not boutton_Français
        elif choix == "2.1":
            boutton_Français_i_diffi = not boutton_Français_i_diffi
        elif choix == "3":
            boutton_Deutsch = not boutton_Deutsch
        elif choix == "3.1":
            boutton_Deutsch_i_merkmale_von_Kurzgeschichten = not boutton_Deutsch_i_merkmale_von_Kurzgeschichten
        elif choix == "3.2":
            boutton_Deutsch_i_merkmale_von_Kurzgeschichten_alle = not boutton_Deutsch_i_merkmale_von_Kurzgeschichten_alle
        elif choix == "4":
            boutton_Anglais = not boutton_Anglais
        elif choix == "4.1":
            boutton_Anglais_i_voc_easy = not boutton_Anglais_i_voc_easy
        elif choix == "4.2":
            boutton_Anglais_i_voc_impossible = not boutton_Anglais_i_voc_impossible
        elif choix == "5":
            boutton_Math = not boutton_Math
        elif choix == "5.1":
            boutton_Math_i_base = not boutton_Math_i_base
        elif choix == "":
            menu = []
            i_Francais = []
            i_Math = []
            i_Deutsch = []
            i_Anglais = []
            i_ScNat = []
            if boutton_ScNat:
                menu.append(ScNat)
                if boutton_ScNat_i_elementen_namen:
                    i_ScNat.append("element")
                if boutton_ScNat_i_elementen_ordnungszahl:
                    i_ScNat.append("ordnungszahl")
            if boutton_Français:
                menu.append(Francais)
                if boutton_Français_i_diffi:
                    i_Francais.append("voc dif")
            if boutton_Deutsch:
                menu.append(Deutsch)
                if boutton_Deutsch_i_merkmale_von_Kurzgeschichten:
                    i_Deutsch.append("Merkmale von Kurzgeschichten (Einfach)")
                if boutton_Deutsch_i_merkmale_von_Kurzgeschichten_alle:
                    i_Deutsch.append("Merkmale von Kurzgeschichten (Schwer)")
            if boutton_Anglais:
                menu.append(Anglais)
                if boutton_Anglais_i_voc_easy:
                    i_Anglais.append("voc easy")
                if boutton_Anglais_i_voc_impossible:
                    i_Anglais.append("voc difficile")
            if boutton_Math:
                menu.append(Math)
                if boutton_Math_i_base:
                    i_Math.append("base")
            if not menu:
                print("Erreur : aucun mode sélectionné. Sélectionnez au moins un mode.")
                input("Appuyez sur Entrée pour continuer...")
                continue
            break
        else:
            print("Choix invalide.")
            input("Appuyez sur Entrée pour continuer...")

    os.system('cls' if os.name == 'nt' else 'clear')
    choix = input("Tu veux faire un quiz avec quel mode ?\n1. infinie\n2. normal\nQ. Exit\nEntrer votre réponse: ").strip().lower()
    if choix == "1":
        streak = True
        ndq = 1
        while streak:
            os.system('cls' if os.name == 'nt' else 'clear')
            if not menu:
                print("Erreur : aucun mode disponible.")
                break
            fonction = random.choice(menu)
            if fonction is ScNat:
                score, xp_gagne, streak = fonction(i_ScNat, ndq)
                joueur["ScNat"]["parties_jouees_ScNat"] += 1
                joueur["ScNat"]["xp_ScNat"] += xp_gagne
                print("\nScNat\nXP ScNat: ", joueur["ScNat"]["xp_ScNat"], "; Level ScNat: ", joueur["ScNat"]["Level_ScNat"], "; Exercise ScNat: ", joueur["ScNat"]["parties_jouees_ScNat"])
            elif fonction is Deutsch:
                score, xp_gagne, streak = fonction(i_Deutsch, ndq)
                joueur["Deutsch"]["parties_jouees_Deutsch"] += 1
                joueur["Deutsch"]["xp_Deutsch"] += xp_gagne
                print("\nDeutsch\nXP Deutsch: ", joueur["Deutsch"]["xp_Deutsch"], "; Level Deutsch: ", joueur["Deutsch"]["Level_Deutsch"], "; Exercise Deutsch: ", joueur["Deutsch"]["parties_jouees_Deutsch"])
            elif fonction is Francais:
                score, xp_gagne, streak = fonction(i_Francais, ndq)
                joueur["Francais"]["parties_jouees_Francais"] += 1
                joueur["Francais"]["xp_Francais"] += xp_gagne
                print("\nFrancais\nXP Francais: ", joueur["Francais"]["xp_Francais"], "; Level Francais: ", joueur["Francais"]["Level_Francais"], "; Exercise Francais: ", joueur["Francais"]["parties_jouees_Francais"])
            elif fonction is Anglais:
                score, xp_gagne, streak = fonction(i_Anglais, ndq)
                joueur["Anglais"]["parties_jouees_Anglais"] += 1
                joueur["Anglais"]["xp_Anglais"] += xp_gagne
                print("\nAnglais\nXP Anglais: ", joueur["Anglais"]["xp_Anglais"], "; Level Anglais: ", joueur["Anglais"]["Level_Anglais"], "; Exercise Anglais: ", joueur["Anglais"]["parties_jouees_Anglais"])
            elif fonction is Math:
                score, xp_gagne, streak = fonction(i_Math, ndq)
                joueur["Math"]["parties_jouees_Math"] += 1
                joueur["Math"]["xp_Math"] += xp_gagne
                print("\nMath\nXP Math: ", joueur["Math"]["xp_Math"], "; Level Math: ", joueur["Math"]["Level_Math"], "; Exercise Math: ", joueur["Math"]["parties_jouees_Math"])
            Level_up(joueur)
            sauvegarder_auto(donnees)
            input("Appuyez sur Entrée pour continuer...")
            ndq += 1


    elif choix == "2":
        if not menu:
            print("Erreur : aucun mode sélectionné.")
            input("Appuyez sur Entrée pour continuer...")
        else:
            try:
                n = int(input("Combien de questions ? "))
            except ValueError:
                print("Nombre invalide.")
                continue
            ndq = n
            for _ in range(n):
                os.system('cls' if os.name == 'nt' else 'clear')
                fonction = random.choice(menu)
                if fonction is ScNat:
                    score, xp_gagne, streak = fonction(i_ScNat, ndq)
                    joueur["ScNat"]["parties_jouees_ScNat"] += 1
                    joueur["ScNat"]["xp_ScNat"] += xp_gagne
                elif fonction is Deutsch:
                    score, xp_gagne, streak = fonction(i_Deutsch, ndq)
                    joueur["Deutsch"]["parties_jouees_Deutsch"] += 1
                    joueur["Deutsch"]["xp_Deutsch"] += xp_gagne
                elif fonction is Francais:
                    score, xp_gagne, streak = fonction(i_Francais, ndq)
                    joueur["Francais"]["parties_jouees_Francais"] += 1
                    joueur["Francais"]["xp_Francais"] += xp_gagne
                elif fonction is Anglais:
                    score, xp_gagne, streak = fonction(i_Anglais, ndq)
                    joueur["Anglais"]["parties_jouees_Anglais"] += 1
                    joueur["Anglais"]["xp_Anglais"] += xp_gagne
                elif fonction is Math:
                    score, xp_gagne, streak = fonction(i_Math, ndq)
                    joueur["Math"]["parties_jouees_Math"] += 1
                    joueur["Math"]["xp_Math"] += xp_gagne
                Level_up(joueur)
                sauvegarder_auto(donnees)
                input("Appuyez sur Entrée pour continuer...")
                ndq -= 1
            print(f"Score: {score}\nPourcentage: {calcule_pourcentage(score, n)}")
            input("Appuyez sur Entrée pour continuer...")

    elif choix == "q":
        print("Au revoir !")
        break
    else:
        print("Choix invalide.")
        input("Appuyez sur Entrée pour continuer...")