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
    print("Quel joueur doit commencer ? (Tapez ", end=" ")
    for i in range(1,num_players+1):
        if i != num_players:
            print (i, end=" ou ")
        else:
            print (i, end=" )  ? ")

    starting_player_id = int(input(":  "))


    return starting_player_id

def compute_turn(current_player_id, players, matches_stacks):
    display_matches_stacks(matches_stacks)
    print(f"c'est a {get_player_name_by_id(current_player_id,players)} de jouer")
    num_matches_removed = int(input("Combien d'allumettes souhaitez retirez"))
    matches_stacks[0] -= num_matches_removed

def init_cycle(players,starting_player_id):
    id_cycle = cycle(p["id"] for p in players)
    # avancer jusqu'au joueur de départ
    cur = next(id_cycle)
    while cur != starting_player_id:
        cur = next(id_cycle)
    return id_cycle

def next_player(id_cycle):
    current_player_id = next(id_cycle)
    print ("next player :" + str(current_player_id))
    return current_player_id

def next_turn(current_player_id, players, matches_stacks,id_cycle):
    print ("next turn")
    if matches_stacks[0] > 1:

        current_player_id = next_player(id_cycle)
        compute_turn(current_player_id, players, matches_stacks)
        next_turn(current_player_id, players, matches_stacks, id_cycle)
    else:
        print (f"{get_player_name_by_id(current_player_id,players)} a gagné !!")



def start_game(starting_player_id,players,matches_stacks):
    compute_turn(starting_player_id, players, matches_stacks)
    id_cycle = init_cycle(players,starting_player_id)
    print ("starting player" + str(starting_player_id))
    next_turn(starting_player_id, players, matches_stacks,id_cycle)


def get_player_name_by_id(player_id, players):

    player_name = ""
    for player in players:
        if player_id == player["id"]:
            player_name = player["name"]

    return player_name




def init_game(num_players):
    """
    Fonction principale qui initialise le jeu: recupere le nom des joeurs, affiche les allumettes et commence la partie
    :param num_players:
    :return:
    """
    players = init_players_names(num_players)

    starting_player_id = choose_starting_player(num_players)

    matches_stacks = [0]
    matches_stacks[0] = 21


    start_game(starting_player_id,players,matches_stacks)

    print("finish")



def init_players_names(num_players):
    players = []
    for i in range(1, num_players + 1):
        name = input(f"Entrez le nom du joueur {i} : ")
        players.append({"id": i, "name": name})
    return players


if __name__ == '__main__':
    init_game(2)
