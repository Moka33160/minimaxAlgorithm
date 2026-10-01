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


def utility(plateau : list[Any]) -> int:
    """ final numeric value for the terminal state"""
    _ , vainqueur = is_terminal(plateau)
    if vainqueur == "nul" :
        return 0
    elif vainqueur == "X":
        return -1
    elif vainqueur == "O":
        return 1
    else:
        raise ValueError("le plateau n'est pas terminal")



def is_future_action_terminal(plateau):
    """check if the future action can be terminal or not  """


    for a, b, c in combinaisons:
        cases = [plateau[a], plateau[b], plateau[c]]

        if cases.count("") == 1:
            if cases.count("X") == 2 or cases.count("O") == 2:
                return True

    return False


def MiniMax(plateau, current_Player):
    """Retourne le score du plateau si les deux joueurs jouent parfaitement."""
    if current_Player == "O":
        v = float("-inf")
    else:
        v = float("inf")

    terminate , _ = is_terminal(plateau)
    if terminate == True :
        return utility(plateau)


    for i in range(len(plateau)):
        if plateau[i] == "":
            new_palteau = future_state(plateau, i, current_Player)
            other_player = "O" if current_Player == "X" else "X"
            score = MiniMax(new_palteau, other_player)
            if current_Player == "O":
                if v < score:
                    v = score
            else :
                if v > score:
                    v = score
    return v


def choisir_coup(plateau):
    meilleur_score = float("-inf")
    meilleur_coup = None

    for action in mouvement_possible(plateau):
        # Simuler le coup de l'IA
        nouveau_plateau = future_state(plateau, action, "O")

        # Après O, c'est à X de jouer
        score = MiniMax(nouveau_plateau, "X")

        if score > meilleur_score:
            meilleur_score = score
            meilleur_coup = action

    return meilleur_coup








