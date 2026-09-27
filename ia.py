def choisir_coup(plateau):
    """
    Entrée : liste de 9 cases.
        ""  = case vide
        "X" = joueur humain
        "O" = IA

    Sortie : indice entier d'une case vide, entre 0 et 8.

    L'IA joue toujours O.
    """

    # Comportement provisoire pour tester l'interface :
    # joue dans la première case vide.
    # Remplace cette partie par ton algorithme Minimax.
    for index in range(9):
        if plateau[index] == "":
            return index