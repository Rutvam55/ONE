import json
import os
from pathlib import Path

# Emplacement par défaut du fichier de sauvegarde
ROOT = Path(__file__).parent.parent
DEFAULT_SAVE_FILE = ROOT / "DATA" / "sauvegarde.json"

def controller_int(ndc, ndc_max, nombre, raison):
    """Demande un entier à l'utilisateur avec plusieurs tentatives.
    Retourne 0 si toutes les tentatives échouent.
    """
    attempts = ndc
    while attempts > 0:
        try:
            val = int(input(raison + "\n> "))
            return val
        except ValueError:
            attempts -= 1
            print(f"Entrée invalide. Retour au menu principal. ({attempts}/{ndc_max})")
            input("ENTER pour continuer...")
    return 0


def charger_sauvegarde(chemin_json: str | Path | None = None):
    """Charge la sauvegarde si elle existe, sinon renvoie une structure vide.
    Accepte un chemin ou utilise le chemin par défaut.
    """
    if chemin_json is None:
        chemin = DEFAULT_SAVE_FILE
    else:
        chemin = Path(chemin_json)

    if chemin.exists():
        try:
            with open(chemin, "r", encoding="utf-8") as fichier:
                donnees = json.load(fichier)
        except json.JSONDecodeError:
            print("Erreur : fichier de sauvegarde corrompu. Réinitialisation.")
            return {"joueurs": {}}

        # Migration: supporter l'ancien format plat vers le format imbriqué
        for nom, joueur in list(donnees.get("joueurs", {}).items()):
            if isinstance(joueur, dict) and "mot_de_passe" in joueur and "Francais" not in joueur:
                nouveau = {
                    "mot_de_passe": joueur.get("mot_de_passe"),
                    "best_score": joueur.get("best_score", 0),
                    "Francais": {
                        "parties_jouees_Francais": joueur.get("parties_jouees_Francais", 0),
                        "Level_Francais": joueur.get("Level_Francais", 0),
                        "xp_Francais": joueur.get("xp_Francais", 0),
                        "Max_xp_Francais": joueur.get("Max_xp_Francais", 1000),
                    },
                    "Deutsch": {
                        "parties_jouees_Deutsch": joueur.get("parties_jouees_Deutsch", 0),
                        "Level_Deutsch": joueur.get("Level_Deutsch", 0),
                        "xp_Deutsch": joueur.get("xp_Deutsch", 0),
                        "Max_xp_Deutsch": joueur.get("Max_xp_Deutsch", 1000),
                    },
                    "ScNat": {
                        "parties_jouees_ScNat": joueur.get("parties_jouees_ScNat", 0),
                        "Level_ScNat": joueur.get("Level_ScNat", 0),
                        "xp_ScNat": joueur.get("xp_ScNat", 0),
                        "Max_xp_ScNat": joueur.get("Max_xp_ScNat", 1000),
                    },
                    "Anglais": {
                        "parties_jouees_Anglais": joueur.get("parties_jouees_Anglais", 0),
                        "Level_Anglais": joueur.get("Level_Anglais", 0),
                        "xp_Anglais": joueur.get("xp_Anglais", 0),
                        "Max_xp_Anglais": joueur.get("Max_xp_Anglais", 1000),
                    },
                    "Math": {
                        "parties_jouees_Math": joueur.get("parties_jouees_Math", 0),
                        "Level_Math": joueur.get("Level_Math", 0),
                        "xp_Math": joueur.get("xp_Math", 0),
                        "Max_xp_Math": joueur.get("Max_xp_Math", 1000),
                    },
                    "P": {
                        "langue": joueur.get("langue", "FR")
                    }
                }
                donnees["joueurs"][nom] = nouveau
        return donnees

    # fichier introuvable
    return {"joueurs": {}}


def sauvegarder_auto(donnees, chemin_json: str | Path | None = None):
    """Écrit automatiquement les données actuelles dans le fichier JSON."""
    if chemin_json is None:
        chemin = DEFAULT_SAVE_FILE
    else:
        chemin = Path(chemin_json)

    # S'assurer que le dossier existe
    chemin.parent.mkdir(parents=True, exist_ok=True)

    with open(chemin, "w", encoding="utf-8") as fichier:
        json.dump(donnees, fichier, indent=4, ensure_ascii=False)


def ajouter_joueur(donnees, nom, mot_de_passe):
    """Ajoute un nouveau joueur avec des données par défaut."""
    if nom in donnees.get("joueurs", {}):
        print("Ce joueur existe déjà.")
        return False

    donnees.setdefault("joueurs", {})
    donnees["joueurs"][nom] = {
        "mot_de_passe": mot_de_passe,
        "best_score": 0,
        "Francais": {
            "parties_jouees_Francais": 0,
            "Level_Francais": 0,
            "xp_Francais": 0,
            "Max_xp_Francais": 1000,
        },
        "Deutsch": {
            "parties_jouees_Deutsch": 0,
            "Level_Deutsch": 0,
            "xp_Deutsch": 0,
            "Max_xp_Deutsch": 1000,
        },
        "ScNat": {
            "parties_jouees_ScNat": 0,
            "Level_ScNat": 0,
            "xp_ScNat": 0,
            "Max_xp_ScNat": 1000,
        },
        "Anglais": {
            "parties_jouees_Anglais": 0,
            "Level_Anglais": 0,
            "xp_Anglais": 0,
            "Max_xp_Anglais": 1000
        },
        "Math": {
            "parties_jouees_Math": 0,
            "Level_Math": 0,
            "xp_Math": 0,
            "Max_xp_Math": 1000
        },
        "P": {
            "langue": "FR"
        }
    }
    return True


def Level_up(joueur):
    # ScNat
    if joueur.get("ScNat", {}).get("xp_ScNat", 0) >= joueur.get("ScNat", {}).get("Max_xp_ScNat", 1000):
        joueur["ScNat"]["Level_ScNat"] += 1
        joueur["ScNat"]["xp_ScNat"] = 0
        joueur["ScNat"]["Max_xp_ScNat"] += 500
        print(f"🎉 Level up ScNat -> {joueur['ScNat']['Level_ScNat']}")
    # Francais
    if joueur.get("Francais", {}).get("xp_Francais", 0) >= joueur.get("Francais", {}).get("Max_xp_Francais", 1000):
        joueur["Francais"]["Level_Francais"] += 1
        joueur["Francais"]["xp_Francais"] = 0
        joueur["Francais"]["Max_xp_Francais"] += 500
        print(f"🎉 Level up Francais -> {joueur['Francais']['Level_Francais']}")
    # Deutsch
    if joueur.get("Deutsch", {}).get("xp_Deutsch", 0) >= joueur.get("Deutsch", {}).get("Max_xp_Deutsch", 1000):
        joueur["Deutsch"]["Level_Deutsch"] += 1
        joueur["Deutsch"]["xp_Deutsch"] = 0
        joueur["Deutsch"]["Max_xp_Deutsch"] += 500
        print(f"🎉 Level up Deutsch -> {joueur['Deutsch']['Level_Deutsch']}")
    # Anglais
    if joueur.get("Anglais", {}).get("xp_Anglais", 0) >= joueur.get("Anglais", {}).get("Max_xp_Anglais", 1000):
        joueur["Anglais"]["Level_Anglais"] += 1
        joueur["Anglais"]["xp_Anglais"] = 0
        joueur["Anglais"]["Max_xp_Anglais"] += 500
        print(f"🎉 Level up Anglais -> {joueur['Anglais']['Level_Anglais']}")
    # Math
    if joueur.get("Math", {}).get("xp_Math", 0) >= joueur.get("Math", {}).get("Max_xp_Math", 1000):
        joueur["Math"]["Level_Math"] += 1
        joueur["Math"]["xp_Math"] = 0
        joueur["Math"]["Max_xp_Math"] += 500
        print(f"🎉 Level up Math -> {joueur['Math']['Level_Math']}")


def selectionner_joueur(donnees, nom, mot_de_passe):
    """
    Vérifie si le joueur existe et si le mot de passe est correct.
    Retourne toujours (joueur, mot_correct)
    joueur = dict ou None
    mot_correct = True / False
    """
    if "joueurs" not in donnees:
        print("Aucune sauvegarde chargée.")
        return None, False

    # Joueur n'existe pas
    if nom not in donnees["joueurs"]:
        print("Joueur introuvable.")
        return None, False

    joueur = donnees["joueurs"][nom]

    # Problème de données
    if "mot_de_passe" not in joueur:
        print("Données du joueur corrompues.")
        return None, False

    # Mot de passe incorrect
    if joueur["mot_de_passe"] != mot_de_passe:
        print("Mot de passe incorrect.")
        return None, False

    # Succès
    return joueur, True