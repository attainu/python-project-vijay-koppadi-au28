from entites.movePlayers import MovePlayer


class TurnPlayers:
    def turn(player, pos):
        play_message = "Press Enter to continue or press 'stop' to stop : "
        win_message = "WINS THE GAME! CONGRATULATIONS"
        player_turn_message = str(
            "Hey " + player + " ! It's your turn now " + play_message
            )
        player_input = input(player_turn_message)

        # IF THE USER CHOSE TO QUIT GAME, THE GAME MUST STOP
        if player_input.lower() == 'stop':
            return True, pos, ''

        pos = MovePlayer.move(player, pos)

        # IF THE PLAYER WINS, HE WILL BE IN WINNER LIST AND AVOIDED THE NEXT
        # TIME
        if pos == 100:
            print(player, win_message)
            print(f"AT WINNING {player} was at {pos}\n")
            return False, pos, 'winner'

        # IF PLAYER HAS NOT QUIT THE GAME AND ALSO HE HAS NOT REACHED HOME
        # THE GAME SHOULD CONTINUE
        return False, pos, player
