#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Jeux  de Nim (variante simple et de Marienbad)
"""
from itertools import cycle
import random
def ask_yes_no(prompt):
    """Demande oui/non, accepte variantes (o/oui/y/yes/n/non)."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"o", "oui", "y", "yes"}:
            return True
        if answer in {"n", "non", "no"}:
            return False
        print("Réponse invalide. Tapez oui ou non.")

def ask_int_in_range(prompt,min_val,max_val):
    """Demande un entier entre un et deux"""
    while True:
        txt = input(prompt).strip()
        if txt.isdigit():
            val = int(txt)
            if min_val <= val <= max_val:
                return val
        print(f"Valeur invalide. Entrez un entier entre {min_val} et {max_val}.")

def ask_game_type(prompt):
    """Demande le type de jeu (Simple ou Marienbad)."""
    while True:
        answer = input(prompt).strip().lower()
        if answer in {"1", "2"}:
            return answer
        print("Réponse invalide. Tapez 1 ou 2.")

def display_matches_stacks(matches_stacks):
    """
    Affiche les allumettes
    :param matches_stacks:
    :return:
    """
    for key,stack in enumerate(matches_stacks):
        print (f"tas n°{key + 1}  ",end=" :")
        for i in range(0, stack):
            print(" | ", end=" ")
        print ("")


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

    return ask_int_in_range(" ",1,num_players + 1)


def cpu_first_move(num_matches,min_matches,max_matches):
    r = list(range(min_matches,max_matches))
    random.shuffle(r)
    matches_removed = 0
    for i in r:
        remaining_matches = num_matches - i
        if remaining_matches % 5 == 0:
            matches_removed = i
    return matches_removed


def compute_turn(current_player_id, players, matches_stacks,prev_move):
    """
    Debut du tour le joueur enlève 1 a 4 allumettes
    :param prev_move:
    :param current_player_id:
    :param players:
    :param matches_stacks:
    :return:
    """
    display_matches_stacks(matches_stacks)
    current_player_name = get_player_name_by_id(current_player_id, players)
    print(f"c'est a {current_player_name} de jouer")
    if current_player_name == "cpu":
        if prev_move:
            num_matches_removed = 5 - int(prev_move)
        else:
            num_matches_removed = cpu_first_move(matches_stacks[0],1,4)
        print ("le cpu a retiré " + str(num_matches_removed) + " allumettes")
    else:
        num_matches_removed = ask_int_in_range(f"{current_player_name}, Combien d'allumettes souhaitez-vous retirez ? :",1,4)

    current_move = num_matches_removed

    return current_move



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
    prev_move = False
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


def init_game(num_players,cpu_player,game_type):
    """
    Fonction principale qui initialise le jeu: récupère le nom des joueurs, affiche les allumettes et commence la partie
    :param cpu_player:
    :param game_type:
    :param num_players:
    :return:
    """
    players = init_players_names(num_players,cpu_player)

    starting_player_id = choose_starting_player(num_players)
    if int(game_type) == 1:
        matches_stacks = [0]
        matches_stacks[0] = 21
    else:
        matches_stacks = (1,3,5,7)

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
    g_type = ask_game_type("Choisissez le type de partie (1:Simple,2:Marienbad) : ")
    init_game(2, cpu,g_type)