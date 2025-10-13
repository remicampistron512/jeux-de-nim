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
            print (i, end=" ) ? ")

    starting_player = int(input(":  "))


    return starting_player


def start_game(starting_player,players):
    current_player_name  = get_player_name_by_id(starting_player, players)
    print(f"c'est a {current_player_name} de jouer")


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
    starting_player = choose_starting_player(num_players)

    matches_stacks = [0]
    matches_stacks[0] = 21
    display_matches_stacks(matches_stacks)

    start_game(starting_player,players)


    while matches_stacks[0] > 1:

        id_cycle = cycle(p["id"] for p in players)
        current_player_id = next(id_cycle)

        print ("current id" + str(current_player_id))
        display_matches_stacks(matches_stacks)
        print(f"c'est a {get_player_name_by_id(current_player_id,players)} de jouer")
        matches_stacks[0] -= 1

def init_players_names(num_players):
    players = []
    for i in range(1, num_players + 1):
        name = input(f"Entrez le nom du joueur {i} : ")
        players.append({"id": i, "name": name})
    return players


if __name__ == '__main__':
    init_game(2)
