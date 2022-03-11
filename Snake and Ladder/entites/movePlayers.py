'''
this function rolls the dice and increase the positions, check for overflow
depending on pos check for snakes and ladders and
update the positions
'''

import random
from entites import snakesPositions
from entites import laddersPositions


class MovePlayer:

    def move(player, value):
        roll_dice = random.randint(1, 6)
        num = value + roll_dice
        if num > 100:
            print(f"BAD LUCK, YOU CANT MOVE, YOU NEED {100 - value} TO WIN\n")
            return value

        if num == 100:
            return num

        # IF PLAYER IS NOT REACHED HOME
        print(player, "Rolled a ", roll_dice, " and moved from", value, " to ",num, '\n')

        # TO CHECK IF PLAYER STOPPED ON SNAKE HEAD
        if num in snakesPositions.snakes:
            print(
                player, " got bitten by a snake and is now on",
                snakesPositions.snakes[num], '\n'
                )
            num = snakesPositions.snakes[num]
            '''to check if even after bitten by snake is there any other snakes
            or ladder at that position'''
            if num in snakesPositions.snakes:
                print(
                    player, " got bitten by a snake again! and is now on",
                    snakesPositions.snakes[num], '\n'
                    )
                num = snakesPositions.snakes[num]
            if num in laddersPositions.ladders:
                print(
                    player,
                    " Your Lucky after bitten by snake you got a ladder" +
                    " your now on ", laddersPositions.ladders[num], '\n'
                    )
                num = laddersPositions.ladders[num]

        # IF PLAYER IS ON LADDER BOTTOM IT WILL CLIMB THE LADDER
        if num in laddersPositions.ladders:
            print(
                player, "Climbed the ladder and is now on ",
                laddersPositions.ladders[num], '\n'
                )
            num = laddersPositions.ladders[num]
            # extra functionality
            if num in snakesPositions.snakes:
                print(
                    player, " bad luck bro! just climbed and again " +
                    "bitten by snakes and your now on ",
                    snakesPositions.snakes[num], '\n'
                    )
                num = snakesPositions.snakes[num]
            if num in laddersPositions.ladders:
                print(
                    player, " Your lucky You climbed again! and your now on ",
                    laddersPositions.ladders[num], '\n'
                    )
                num = laddersPositions.ladders[num]

        return num
