from util.numberOfPlayers import CountPlayer
from util.playersNames import PlayerNames
from display.welcomePlayers import Welcome
import random
from entites import snakesPositions
from entites import laddersPositions
from game.playeGame import PlayGame


# This function is responsible for executing all the features of the game
def main_function():
    # programatically generated snakes positions
    snakesPositions.generate_snakes()

    # programatically generated ladders positions
    laddersPositions.generate_ladders()

    # number of players playing the game
    num_of_players = CountPlayer.players_count()

    # Getting the player names
    global players_names
    players_names = PlayerNames.name_of_players(num_of_players)

    # Welcome the players to the game
    Welcome.welcome_players(players_names)

    # This code will execute in case there is only one player
    if num_of_players < 2:
        PlayGame.play_single_player_game(num_of_players, players_names)

    # This code will execute when players are more then one
    else:
        PlayGame.play_multi_player_game(num_of_players, players_names)


if __name__ == '__main__':
    main_function()
