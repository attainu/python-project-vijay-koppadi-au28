from game.turnPlayers import TurnPlayers


class PlayGame:
    def play_single_player_game(num_of_players, players_names):
        player_turn = 0
        player_positions = [0 for i in range(num_of_players)]

        # THIS CODE WILL EXECUTE IF ONLY ONE PLAYER WANT TO PLAYE THE GAME
        game_over = False
        while not game_over:
            while player_turn < num_of_players:
                player_turn += 1
                player = ''

                if player_positions[player_turn-1] < 100 and players_names[player_turn-1] != 'winner':
                    game_over, player_positions[player_turn-1], player = TurnPlayers.turn(players_names[player_turn-1], 
                    player_positions[player_turn-1])

                if player == 'winner':
                    players_names[player_turn-1] = player

                count = players_names.count("winner")
                if len(players_names) - count == 0:
                    game_over = True

                if game_over:
                    return

            player_turn = 0

    # THIS CODE WILL EXECUTE IN CASE IF NUMBER OF PLAYERS ARE MORE THEN ONE
    def play_multi_player_game(num_of_players, players_names):
        player_turn = 0
        player_positions = [0 for i in range(num_of_players)]
        game_over = False
        while not game_over:
            while player_turn < num_of_players:
                player_turn += 1
                player = ''

                if player_positions[player_turn-1] < 100 and players_names[player_turn-1] != 'winner':
                    game_over, player_positions[player_turn-1], player = TurnPlayers.turn(players_names[player_turn-1],
                     player_positions[player_turn-1])

                if player == 'winner':
                    players_names[player_turn-1] = player

                count = players_names.count("winner")
                if len(players_names) - count == 1:
                    game_over = True

                if game_over:
                    return

            player_turn = 0
