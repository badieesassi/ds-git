taches = []
def ajouter_tache():
    titre = input("Entrez le titre de la tache : ")

    if titre == "":
        print("Erreur: le titre est obligatoire.")
    else:
        numero = len(taches) + 1
        tache = {
            "numero": numero,
            "titre": titre
        }

        taches.append(tache)
        print("Tache ajoutée avec succès")

def afficher_taches():
    if len(taches) == 0:
        print("La liste est vide.")
    else:
        print("\n Liste des taches:")

        for tache in taches:
            print(tache["numero"], "-", tache["titre"])


def rechercher_tache():
    numero = input("Entrez le numéro de la tache : ")

    if numero.isdigit():
        numero = int(numero)
        trouve = False

        for tache in taches:
            if tache["numero"] == numero:
                print("Tache trouvée :", tache["titre"])
                trouve = True

        if trouve == False:
            print("Tache introuvable.")
    else:
        print("Veuillez entrer un numéro valide.")

while True:

    print("Gestion des taches ")
    print("1) Ajouter une tache")
    print("2) Afficher les taches")
    print("3)  Rechercher une tache")
    print("0)  Quitter")

    choix = input("Votre choix: ")

    if choix == "1":
        ajouter_tache()

    elif choix == "2":
        afficher_taches()

    elif choix == "3":
        rechercher_tache()

    elif choix == "0":
        print("Merci")
        break
    else:
        print("Choix incorrect")
