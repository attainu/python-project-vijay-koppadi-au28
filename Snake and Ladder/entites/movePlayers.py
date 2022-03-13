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
        print(player, "ROLLED A ", roll_dice, " AND MOVED FROM", value, " TO ",num, '\n')

        # TO CHECK IF PLAYER STOPPED ON SNAKE HEAD
        if num in snakesPositions.snakes:
            print(
                player, " GOT BITTEN BY A SNAKE AND IS NOW ON",
                snakesPositions.snakes[num], '\n'
                )
            num = snakesPositions.snakes[num]
            '''to check if even after bitten by snake is there any other snakes
            or ladder at that position'''
            if num in snakesPositions.snakes:
                print(
                    player, " GOT BITTEN BY A SNAKE AGAIN! AND IS NOW ON",
                    snakesPositions.snakes[num], '\n'
                    )
                num = snakesPositions.snakes[num]
            if num in laddersPositions.ladders:
                print(
                    player,
                    " YOUR LUCKY AFTER BITTEN BY SNAKE YOU GOT A LADDER " +
                    " YOUR NOW ON ", laddersPositions.ladders[num], '\n'
                    )
                num = laddersPositions.ladders[num]

        # IF PLAYER IS ON LADDER BOTTOM IT WILL CLIMB THE LADDER
        if num in laddersPositions.ladders:
            print(
                player, "CLIMBED THE LADDER AND IS NOW ON",
                laddersPositions.ladders[num], '\n'
                )
            num = laddersPositions.ladders[num]
            # extra functionality
            if num in snakesPositions.snakes:
                print(
                    player, " BAD LUCK BRO! JUST CLIMBED AND AGAIN " +
                    "BITTEN BY SNAKES AND YOUR NOW ON ",
                    snakesPositions.snakes[num], '\n'
                    )
                num = snakesPositions.snakes[num]
            if num in laddersPositions.ladders:
                print(
                    player, " YOUR LUCKY YOU CLIMBED LADDER AGAIN! AND YOUR NOW ON ",
                    laddersPositions.ladders[num], '\n'
                    )
                num = laddersPositions.ladders[num]

        return num


