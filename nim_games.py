#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Jeux  de Nim (variante simple et de Marienbad)
"""
from itertools import cycle

def ask_yes_no(prompt):
    """Demande oui/non, accepte variantes (o/oui/y/yes/n/non)."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"o", "oui", "y", "yes"}:
            return True
        if answer in {"n", "non", "no"}:
            return False
        print("Réponse invalide. Tapez oui ou non.")

def ask_int_in_range(prompt):
    """Demande un entier entre un et deux"""
    while True:
        txt = input(prompt).strip()
        if txt.isdigit():
            val = int(txt)
            if 1 <= val <= 2:
                return val
        print(f"Valeur invalide. Entrez un entier entre 1 et 2.")

def display_matches_stacks(matches_stacks):
    """
    Affiche les allumettes
    :param matches_stacks:
    :return:
    """
    for stack in matches_stacks:
        for i in range(0, stack):
            print(" | ", end=" ")


def choose_starting_player(num_players):
    """
    On affiche l'invite pour choisir entre le joueur 1 et n
    :param num_players:
    :return:
    """
    print("Quel joueur doit commencer ? (Tapez ", end=" ")
    for i in range(1, num_players + 1):
        if i != num_players:
            print(i, end=" ou ")
        else:
            print(i, end=" )  ? ")

    return ask_int_in_range(" ")



def compute_turn(current_player_id, players, matches_stacks,prev_move):
    """
    Debut du tour le joueur enlève 1 a 4 allumettes
    :param current_player_id:
    :param players:
    :param matches_stacks:
    :return:
    """
    display_matches_stacks(matches_stacks)
    current_player_name = get_player_name_by_id(current_player_id, players)
    print(f"c'est a {current_player_name} de jouer")
    if current_player_name == "cpu":
        num_matches_removed = 5 - int(prev_move)
        print ("le cpu a retiré " + str(num_matches_removed) + " allumettes")
    else:
        num_matches_removed = input("{}, Combien d'allumettes souhaitez-vous retirez? : " .format(current_player_name))

    current_move = num_matches_removed

    if str(num_matches_removed).isdigit() and 4 >= int(num_matches_removed) >= 1:
        matches_stacks[0] -= int(num_matches_removed)
        return current_move
    else:
        print ("merci de rentrer un chiffre valide entre 1 et 4")
        return compute_turn(current_player_id, players, matches_stacks,current_move)


def init_cycle(players, starting_player_id):
    """
    Initialise l'objet cycle de cycler et place le pointeur sur le joueur qui commence
    :param players:
    :param starting_player_id:
    :return:
    """
    id_cycle = cycle(p["id"] for p in players)
    # avancer jusqu'au joueur de départ
    cur = next(id_cycle)
    while cur != starting_player_id:
        cur = next(id_cycle)
    return id_cycle


def next_player(id_cycle):
    """
    On passe au joueur suivant
    :param id_cycle:
    :return:
    """
    current_player_id = next(id_cycle)
    return current_player_id


def next_turn(current_player_id, players, matches_stacks, id_cycle,prev_move):
    """
    On avance d'un tour
    :param current_player_id:
    :param players:
    :param matches_stacks:
    :param id_cycle:
    :return:
    """
    if matches_stacks[0] > 1:
        current_player_id = next_player(id_cycle)
        current_move = compute_turn(current_player_id, players, matches_stacks,prev_move)
        next_turn(current_player_id, players, matches_stacks, id_cycle,current_move)
    else:
        print(f"{get_player_name_by_id(current_player_id, players)} a gagné !!")


def start_game(starting_player_id, players, matches_stacks):
    """
    Commence la partie
    :param starting_player_id:
    :param players:
    :param matches_stacks:
    :return:
    """
    prev_move = 0
    current_move = compute_turn(starting_player_id, players, matches_stacks,prev_move)
    id_cycle = init_cycle(players, starting_player_id)
    next_turn(starting_player_id, players, matches_stacks, id_cycle,current_move)


def get_player_name_by_id(player_id, players):
    """
    Récupère le nom de joueur selon son id
    :param player_id:
    :param players:
    :return:
    """
    player_name = ""
    for player in players:
        if player_id == player["id"]:
            player_name = player["name"]

    return player_name


def init_game(num_players,cpu_player):
    """
    Fonction principale qui initialise le jeu: récupère le nom des joueurs, affiche les allumettes et commence la partie
    :param num_players:
    :return:
    """
    players = init_players_names(num_players,cpu_player)

    starting_player_id = choose_starting_player(num_players)

    matches_stacks = [0]
    matches_stacks[0] = 21

    start_game(starting_player_id, players, matches_stacks)

    print("finish")


def init_players_names(num_players,cpu_player):
    """
    On demande le nom de chaque joueur
    :param num_players:
    :return:
    """
    players = []
    for i in range(1, num_players + 1):
        if cpu_player and i == 2:
            players.append({"id": i, "name": "cpu"})
        else:
            name = input(f"Entrez le nom du joueur {i} : ")
            players.append({"id": i, "name": name})
    return players


if __name__ == '__main__':
    cpu = ask_yes_no("Voulez-vous jouer contre l'ordinateur ? (oui/non) : ")
    init_game(2, cpu)