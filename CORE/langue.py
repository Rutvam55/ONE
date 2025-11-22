def langue(nom, joueur, v, boutton_state):

    scnat = boutton_state["ScNat_1"]
    scnat_1 = boutton_state["ScNat_1_1"]

    FR = {
        "main.1.p": "Bienvenue, {name} !\nTu veux faire quoi?",
        "main.2.i": "1. Entrainemant\nP. Parametre",
        "main.3.i": "__PARAMETRE__\n1. Langue: {langue}\n2. v: {v}",
        "main.4.p": "Appuie sur Entrée pour lancer le quiz avec les modes sélectionnés.",
        "main.5.i": "Entrer votre réponse (tape 1-5 pour basculer): ",
        "main.6.p": "Erreur : aucun mode sélectionné. Sélectionnez au moins un mode.",
        "main.7.p": "1. ScNat ({scnat})",
        "main.8.p": "    1.1. Nom des elemente ({scnat_11})"
    }

    EN = {
        "main.1.p": "Welcome, {name}!\nWhat would you like to do?",
        "main.2.i": "1. Training\nS. Setting",
        "main.3.i": "__SETTING__\n1. Language: {langue}\n2. v: {v}",
        "main.4.p": "Press of Enter to start the game.",
        "main.5.i": "Enter your answer (tape 1-5 or (1.2 5.1)): ",
        "main.6.p": "!!! ERROR !!!\n*restart",
        "main.7.p": "1. ScNat ({scnat})",
        "main.8.p": "    1.1. Name of the elemente ({scnat_11})"
    }

    DE = {
        "main.1.p": "Willkommen, {name}!\nWas wollen sie machen?",
        "main.2.i": "1. Aufgaben\nS. Einstellung",
        "main.3.i": "__EINSTELLUNG__\n1. Sprache: {langue}\n2. v: {v}",
        "main.4.p": "Um zu Starten, drucken sie auf Enter.",
        "main.5.i": "Geben sie ihre antwort (tape 1-5 or (1.2 5.1)): ",
        "main.6.p": "!!! FEHLER !!!\n*NEUSTART",
        "main.7.p": "1. ScNat ({scnat})",
        "main.8.p": "    1.1. Name der elemente ({scnat_11})"
    }

    langue_actuelle = joueur["P"]["langue"]
    if langue_actuelle == "EN":
        La = EN
    elif langue_actuelle == "FR":
        La = FR
    elif langue_actuelle == "DE":
        La = DE
    else:
        La = FR  # Par défaut: Français

    # Formatage final
    return {k: v.format(
        name = nom if nom else "Invité",
        langue = joueur["P"]["langue"],
        v = v,
        scnat = "ON" if scnat else "OFF",
        scnat_11 = "ON" if scnat_1 else "OFF"
    ) for k, v in La.items()}