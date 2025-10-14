#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Jeux  de Nim (variante simple et de Marienbad)
"""
from itertools import cycle


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

    starting_player_id = input(":  ")

    if starting_player_id.isdigit():
        if int(starting_player_id) not in range(1, num_players + 1):
            print(f"Joueur invalide (entrez un chiffre entre 1 et {num_players} )")
            return choose_starting_player(num_players)
        else:
            return int(starting_player_id)
    else:
        print("Joueur invalide (pas un chiffre)")
        return choose_starting_player(num_players)


def compute_turn(current_player_id, players, matches_stacks):
    """
    Debut du tour le joueur enlève 1 a 4 allumettes
    :param current_player_id:
    :param players:
    :param matches_stacks:
    :return:
    """
    display_matches_stacks(matches_stacks)
    print(f"c'est a {get_player_name_by_id(current_player_id, players)} de jouer")
    num_matches_removed = input("Combien d'allumettes souhaitez vous retirez : ")

    if num_matches_removed.isdigit() and 4 >= int(num_matches_removed) >= 1:
        matches_stacks[0] -= int(num_matches_removed)
        return None
    else:
        print ("merci de rentrer un chiffre valide entre 1 et 4")
        return compute_turn(current_player_id, players, matches_stacks)


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


def next_turn(current_player_id, players, matches_stacks, id_cycle):
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
        compute_turn(current_player_id, players, matches_stacks)
        next_turn(current_player_id, players, matches_stacks, id_cycle)
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
    compute_turn(starting_player_id, players, matches_stacks)
    id_cycle = init_cycle(players, starting_player_id)
    next_turn(starting_player_id, players, matches_stacks, id_cycle)


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


def init_game(num_players):
    """
    Fonction principale qui initialise le jeu: récupère le nom des joueurs, affiche les allumettes et commence la partie
    :param num_players:
    :return:
    """
    players = init_players_names(num_players)

    starting_player_id = choose_starting_player(num_players)

    matches_stacks = [0]
    matches_stacks[0] = 21

    start_game(starting_player_id, players, matches_stacks)

    print("finish")


def init_players_names(num_players):
    """
    On demande le nom de chaque joueur
    :param num_players:
    :return:
    """
    players = []
    for i in range(1, num_players + 1):
        name = input(f"Entrez le nom du joueur {i} : ")
        players.append({"id": i, "name": name})
    return players


if __name__ == '__main__':
    init_game(2)
