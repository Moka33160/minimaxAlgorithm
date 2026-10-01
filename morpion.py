import tkinter as tk
from tkinter import messagebox
from ia import choisir_coup


HUMAIN = "X"
IA = "O"

plateau = [""] * 9
partie_terminee = False
tour_ia = False
appel_ia = None


def gagnant():
    combinaisons = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Lignes
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Colonnes
        (0, 4, 8), (2, 4, 6),             # Diagonales
    ]

    for a, b, c in combinaisons:
        if plateau[a] != "" and plateau[a] == plateau[b] == plateau[c]:
            return plateau[a]

    return None


def verifier_fin():

    global partie_terminee

    vainqueur = gagnant()

    if vainqueur is not None:
        partie_terminee = True
        if vainqueur == HUMAIN:
            message.config(text="Tu as gagné !")

        else:
            message.config(text="L'IA a gagné !")


    elif "" not in plateau:
        partie_terminee = True
        message.config(text="Match nul !")


    return partie_terminee


def poser_symbole(index, symbole):
    plateau[index] = symbole
    boutons[index].config(text=symbole)


def jouer_humain(index):
    global tour_ia, appel_ia

    if partie_terminee or tour_ia or plateau[index] != "":
        return

    poser_symbole(index, HUMAIN)

    if verifier_fin():
        return

    tour_ia = True
    message.config(text="L'IA réfléchit…")

    # Laisse le temps à l'interface d'afficher ton coup
    appel_ia = fenetre.after(200, jouer_ia)


def jouer_ia():
    global tour_ia, appel_ia, partie_terminee

    appel_ia = None

    try:
        # Une copie permet à ton algo de simuler des coups
        # sans modifier directement le plateau de l'interface.
        index = choisir_coup(plateau.copy())

        if type(index) is not int:
            raise ValueError("choisir_coup doit retourner un entier.")

        if not 0 <= index < 9:
            raise ValueError("L'indice doit être compris entre 0 et 8.")

        if plateau[index] != "":
            raise ValueError("L'IA a choisi une case déjà occupée.")

    except Exception as erreur:
        partie_terminee = True
        tour_ia = False
        message.config(text="Erreur IA : recommence après correction.")
        messagebox.showerror("Erreur dans l'IA", str(erreur))
        return

    poser_symbole(index, IA)
    tour_ia = False

    if not verifier_fin():
        message.config(text="À toi de jouer : X")


def recommencer():
    global partie_terminee, tour_ia, appel_ia

    # Annule le coup prévu si on recommence pendant le délai
    if appel_ia is not None:
        fenetre.after_cancel(appel_ia)
        appel_ia = None

    plateau[:] = [""] * 9
    partie_terminee = False
    tour_ia = False

    for bouton in boutons:
        bouton.config(text="")

    message.config(text="À toi de jouer : X")


fenetre = tk.Tk()
fenetre.title("Morpion — Joueur contre IA")
fenetre.resizable(False, False)

message = tk.Label(
    fenetre,
    text="À toi de jouer : X",
    font=("Arial", 16),
)
message.pack(pady=15)

grille = tk.Frame(fenetre)
grille.pack(padx=15, pady=5)

boutons = []

for index in range(9):
    bouton = tk.Button(
        grille,
        text="",
        font=("Arial", 28, "bold"),
        width=4,
        height=2,
        command=lambda i=index: jouer_humain(i),
    )
    bouton.grid(
        row=index // 3,
        column=index % 3,
        padx=3,
        pady=3,
    )
    boutons.append(bouton)

tk.Button(
    fenetre,
    text="Recommencer",
    command=recommencer,
).pack(pady=15)

fenetre.mainloop()