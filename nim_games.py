#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Jeux  de Nim (variante simple et de Marienbad)
"""


def display_matches_stacks(matches_stacks):
    """
    Affiche les allumettes
    :param matches_stacks:
    :return:
    """
    for stack in matches_stacks:
        for i in range(0, stack):
            print(" | ", end=" ")


def choose_starting_player(players):
    pass


def start_game():
    pass


def init_game(num_players):
    """
    Fonction principale qui initialise le jeu: recupere le nom des joeurs, affiche les allumettes et commence la partie
    :param num_players:
    :return:
    """
    players = init_players_names(num_players)
    choose_starting_player(players)
    matches_stacks = [0]
    matches_stacks[0] = 21
    display_matches_stacks(matches_stacks)
    start_game()


def init_players_names(num_players):
    players = []
    for i in range(1, num_players + 1):
        name = input(f"Entrez le nom du joueur {i} : ")
        players.append({"id": i, "name": name})
    return players


if __name__ == '__main__':
    init_game(2)
