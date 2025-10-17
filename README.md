# Jeux de Nim

Ce programme permet de jouer au jeu de nim où deux joueurs s'affrontent en retirant des allumettes
chacun leur tour d'un tas d'allumettes.

- [Installation](#installation)
- [Utilisation](#utilisation)
- [Règles du jeu](#règles-du-jeu)
- [Fonctionnalités](#fonctionnalités)
- [Structure du code](#structure-du-code)

## Installation

1. Assurez-vous d’avoir **Python 3** installé sur votre machine.
2. Téléchargez le fichier `nim_games.py` dans un répertoire de votre choix.
3. Ouvrez un terminal et exécutez le script : `python nim_games.py`

## Règles du jeu

**Variante simple:**

Chaque joueur à son tour enlève entre une et quatre allumettes du tas. Celui qui enlève la dernière 
allumette a perdu.

**Variante Marienbad:**

il y a au départ quatre tas, avec respectivement 1, 3, 5 et 7 allumettes. À chaque tour, 
le joueur prend le nombre d'allumettes qu'il veut, au moins 
une et dans un même tas. Celui qui prend la dernière allumette perd.

## Fonctionnalités

Avant qu'une partie démarre, deux possibilités s'offrent au joueur :
- De jouer contre l'ordinateur
- De jouer contre un autre joueur

On demande alors au joueur de choisir un type de partie : simple ou Marienbad

Ensuite, est demandé le nom de chaque joueur et quel joueur doit commencer.

Enfin, la partie commence et les règles mentionnées ci-dessus s'appliquent.

## Structure du code

### `ask_yes_no(prompt)`
**Paramètres :** `prompt`  
**Description :** Demande oui/non, accepte variantes (o/oui/y/yes/n/non).

---

### `ask_int_in_range(prompt, min_val, max_val)`
**Paramètres :** `prompt`, `min_val`, `max_val`  
**Description :** Demande un entier entre un et deux.

---

### `ask_game_type(prompt)`
**Paramètres :** `prompt`  
**Description :** Demande le type de jeu (Simple ou Marienbad).

---

### `get_player_name_by_id(player_id, players)`
**Paramètres :** `player_id`, `players`  
**Description :** Récupère le nom de joueur selon son id.

---

### `start_game(starting_player_id, players, matches_stacks)`
**Paramètres :** `starting_player_id`, `players`, `matches_stacks`  
**Description :** Commence la partie.

---

### `next_turn(current_player_id, players, matches_stacks, id_cycle, prev_move)`
**Paramètres :** `current_player_id`, `players`, `matches_stacks`, `id_cycle`, `prev_move`  
**Description :** On avance d'un tour.

---

### `next_player(id_cycle)`
**Paramètres :** `id_cycle`  
**Description :** On passe au joueur suivant.

---

### `compute_turn(current_player_id, players, matches_stacks, prev_move)`
**Paramètres :** `current_player_id`, `players`, `matches_stacks`, `prev_move`  
**Description :** Début du tour : le joueur enlève 1 à 4 allumettes.

---

### `cpu_move_marienbad(matches_stacks)`
**Paramètres :** `matches_stacks`  
**Description :** Joue un coup pour l'ordinateur dans la version Marienbad.

---

### `cpu_move_simple(num_matches, min_matches, max_matches)`
**Paramètres :** `num_matches`, `min_matches`, `max_matches`  
**Description :** Joue un coup pour l'ordinateur dans la version simple du jeu.

---

### `remove_matches(matches_stacks, chosen_stack, num_matches)`
**Paramètres :** `matches_stacks`, `chosen_stack`, `num_matches`  
**Description :** Retire un nombre d'allumettes (num_matches) dans un tas d'allumettes.

---

### `choose_stack(matches_stacks, current_player_name)`
**Paramètres :** `matches_stacks`, `current_player_name`  
**Description :** Demande au joueur de choisir un tas d'allumettes.

---

### `display_matches_stacks(matches_stacks)`
**Paramètres :** `matches_stacks`  
**Description :** Affiche les allumettes.

---

### `choose_starting_player(num_players)`
**Paramètres :** `num_players`  
**Description :** On affiche l'invite pour choisir entre le joueur 1 et n.

---

### `init_cycle(players, starting_player_id)`
**Paramètres :** `players`, `starting_player_id`  
**Description :** Initialise l'objet `cycle` et place le pointeur sur le joueur qui commence.

---

### `init_players_names(num_players, cpu_player)`
**Paramètres :** `num_players`, `cpu_player`  
**Description :** On demande le nom de chaque joueur.

---

### `init_game(num_players, cpu_player, game_type)`
**Paramètres :** `num_players`, `cpu_player`, `game_type`  
**Description :** Fonction principale qui initialise le jeu : récupère le nom des joueurs, affiche les allumettes et commence la partie.
