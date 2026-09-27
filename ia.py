from typing import Any

combinaisons = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6),
    ]


def mouvement_possible(plateau : list[Any]) -> list[Any]:
    state = []
    for i in range(9):
        if plateau[i] == "":
            state.append(i)
    return state


def future_state(plateau  : list[Any], action : int , joeur : str) -> list[Any]:
    state = plateau[:]

    if joeur == "X":
        state[action] = "X"
        return state
    else :
        state[action] = "O"
        return state

def is_terminal(plateau ):


    for a, b, c in combinaisons:
        if plateau[a] != "" and plateau[a] == plateau[b] == plateau[c]:
            return True, plateau[a]

    if "" not in plateau:
        return True, "nul"

    return False, None



def is_future_action_terminal(plateau):
    """check if the future action can be terminal or not  """


    for a, b, c in combinaisons:
        cases = [plateau[a], plateau[b], plateau[c]]

        if cases.count("") == 1:
            if cases.count("X") == 2 or cases.count("O") == 2:
                return True

    return False


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
    pass