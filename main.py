import random
import os
import pwinput

from itertools import islice
from CORE.link import set_joueur, Math, Anglais, ScNat, Francais, Deutsch
from CORE.funk import sauvegarder_auto, charger_sauvegarde, ajouter_joueur, Level_up, selectionner_joueur, controller_int
from CORE.langue import langue

v = "0.8.0"

def calcule_pourcentage(nombre, nombre_total):
    return (nombre / nombre_total) * 100 if nombre_total > 0 else 0

# ===============================
#       CLASSE BOUTTON
# ===============================

class Boutton:
    def __init__(self):
        self.state = {
            "ScNat_1": False,
            "ScNat_1_1": False,
            "ScNat_1_2": False,

            "Français_2": False,
            "Français_2_1": False,

            "Deutsch_3": False,
            "Deutsch_3_1": False,
            "Deutsch_3_2": True,

            "Anglais_4": False,
            "Anglais_4_1": False,
            "Anglais_4_2": False,

            "Math_5": False,
            "Math_5_1": False
        }

    def toggle(self, name):
        if name in self.state:
            self.state[name] = not self.state[name]
        else:
            print(f"[ERREUR] '{name}' n'existe pas.")

    def collect(self):
        menu = []
        i_ScNat = []
        i_Francais = []
        i_Deutsch = []
        i_Anglais = []
        i_Math = []
        # ---------------- SC NAT ----------------
        if self.state["ScNat_1"]:
            menu.append("ScNat")
            if self.state["ScNat_1_1"]:
                i_ScNat.append("element")
            if self.state["ScNat_1_2"]:
                i_ScNat.append("ordnungszahl")

        # ---------------- FRANÇAIS ----------------
        if self.state["Français_2"]:
            menu.append("Francais")
            if self.state["Français_2_1"]:
                i_Francais.append("voc dif")

        # ---------------- DEUTSCH ----------------
        if self.state["Deutsch_3"]:
            menu.append("Deutsch")
            if self.state["Deutsch_3_1"]:
                i_Deutsch.append("einfach")
            if self.state["Deutsch_3_2"]:
                i_Deutsch.append("schwer")

        # ---------------- ANGLAIS ----------------
        if self.state["Anglais_4"]:
            menu.append("Anglais")
            if self.state["Anglais_4_1"]:
                i_Anglais.append("easy")
            if self.state["Anglais_4_2"]:
                i_Anglais.append("impossible")

        # ---------------- MATH ----------------
        if self.state["Math_5"]:
            menu.append("Math")
            if self.state["Math_5_1"]:
                i_Math.append("base")
        
        return menu, i_ScNat, i_Francais, i_Deutsch, i_Anglais, i_Math


# ===============================
#       PROGRAMME PRINCIPAL
# ===============================

boutons = Boutton()
running = True
connection = False

while running:

    donnees = charger_sauvegarde()

    # =================================
    #  CONNEXION
    # =================================
    while not connection:
        print("=== ONE ===")
        mot_de_passe_entrer = False
        ndc = 3
        

        if ndc == 0 and mot_de_passe_entrer is False:
            print("Too many incorrect attempts. Exiting.")
            exit()

        nom = input("Enter your name.\n> ")
        mdp = pwinput.pwinput(prompt = "Enter your password.\n> ", mask = '#')
        joueur, mot_de_passe_entrer = selectionner_joueur(donnees, nom, mdp)

        if joueur is None:
            creer = input("Player not found. Create one? (o/n) ")

            if creer.lower() == "o":
                if ajouter_joueur(donnees, nom, mdp):
                    joueur = donnees["joueurs"][nom]
                    sauvegarder_auto(donnees)
                else:
                    print("ERROR")
                    continue
            else:
                exit()

        while mot_de_passe_entrer is False and ndc > 0:
            nom = input("Enter your name.\n> ")
            mdp = pwinput.pwinput(prompt = "Enter your password.\n> ", mask = '#')
            joueur, mot_de_passe_entrer = selectionner_joueur(donnees, nom, mdp)
            if mot_de_passe_entrer is True:
                break
            ndc -= 1
            print(f"Password: {mdp}\nAttempts remaining: {ndc}/3")
            if ndc == 0 and mot_de_passe_entrer is False:
                print("Too many incorrect attempts. Exiting.")
                exit()

        connection = True
        set_joueur(joueur)

    # ===============================
    #       LANGUE
    # ===============================
    L = langue(nom, joueur, v, boutons.state)

    # ===============================
    #       MENU PRINCIPAL
    # ===============================
    while True:

        print(L["main.1.p"])
        choix = input(L["main.2.i"]).strip()

        # =======================================
        #                PARAMÈTRES
        # =======================================
        if choix == "1":

            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("=========== PARAMÈTRES ===========")

                def show(btn, txt):
                    etat = "ON" if boutons.state[btn] else "OFF"
                    print(f"{txt} ({etat})")

                show("ScNat_1", "1. ScNat")
                show("ScNat_1_1", "  1.1 Element Namen")
                show("ScNat_1_2", "  1.2 Ordnungszahl")

                show("Français_2", "2. Français")
                show("Français_2_1", "  2.1 Voc. difficile")

                show("Deutsch_3", "3. Deutsch")
                show("Deutsch_3_1", "  3.1 Kurzgeschichten (einfach)")
                show("Deutsch_3_2", "  3.2 Kurzgeschichten (schwer)")

                show("Anglais_4", "4. Anglais")
                show("Anglais_4_1", "  4.1 Easy voc")
                show("Anglais_4_2", "  4.2 Impossible voc")

                show("Math_5", "5. Math")
                show("Math_5_1", "  5.1 Base")

                print("\nENTER to valider, ou choisir un bouton.")

                action = input("> ").strip()

                mapping = {
                    "1": "ScNat_1",
                    "1.1": "ScNat_1_1",
                    "1.2": "ScNat_1_2",

                    "2": "Français_2",
                    "2.1": "Français_2_1",

                    "3": "Deutsch_3",
                    "3.1": "Deutsch_3_1",
                    "3.2": "Deutsch_3_2",

                    "4": "Anglais_4",
                    "4.1": "Anglais_4_1",
                    "4.2": "Anglais_4_2",

                    "5": "Math_5",
                    "5.1": "Math_5_1"
                }

                if action in mapping:
                    boutons.toggle(mapping[action])
                elif action == "":
                    break
                else:
                    print("Choix invalide.")
                    input("ENTER pour continuer...")
            
            # =======================================
            #           LANCER LES JEUX
            # =======================================
            menu, i_ScNat, i_Francais, i_Deutsch, i_Anglais, i_Math = boutons.collect()
            if not menu:
                print("Aucun jeu sélectionné dans les paramètres.")
                input("ENTER pour continuer...")
                continue
            else:
                choix_mode = input("Choisir le mode\n1: Infini\n2: Normal\n> ").strip().lower()
                if choix_mode in ["1", "infini"]:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    Streak = True
                    ndq = 0
                    while Streak:
                        ndq += 1
                        jeu_choisi = random.choice(menu)
                        if jeu_choisi == "ScNat":
                            ScNat(i_ScNat, ndq, L)
                        elif jeu_choisi == "Francais":
                            Francais(i_Francais, ndq, L)
                        elif jeu_choisi == "Deutsch":
                            Deutsch(i_Deutsch, ndq, L)
                        elif jeu_choisi == "Anglais":
                            Anglais(i_Anglais, ndq, L)
                        elif jeu_choisi == "Math":
                            Math(i_Math, ndq, L)
                        else:
                            print("Erreur de sélection du jeu.")
                            Streak = False
                        Level_up(joueur)
                        sauvegarder_auto(donnees)
                elif choix_mode in ["2", "normal"]:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    Streak = True
                    ndc = 5
                    ndc_max = ndc
                    ndq = 0
                    ndq = controller_int(ndc, ndc_max, ndq, "Combien de questions voulez-vous?")
                    ndqr = ndq
                    for i in range(ndq):
                        ndqr += 1
                        jeu_choisi = random.choice(menu)
                        if jeu_choisi == "ScNat":
                            ScNat(i_ScNat, ndqr, L)
                        elif jeu_choisi == "Francais":
                            Francais(i_Francais, ndqr, L)
                        elif jeu_choisi == "Deutsch":
                            Deutsch(i_Deutsch, ndqr, L)
                        elif jeu_choisi == "Anglais":
                            Anglais(i_Anglais, ndqr, L)
                        elif jeu_choisi == "Math":
                            Math(i_Math, ndqr, L)
                        else:
                            print("Erreur de sélection du jeu.")
                            Streak = False
                        Level_up(joueur)
                        sauvegarder_auto(donnees)


        # =======================================
        #             QUITTER LE JEU
        # =======================================
        elif choix.lower() == "q":
            print("Au revoir !")
            running = False
            break

        else:
            print("Choix invalide.")
            input("ENTER pour continuer...")