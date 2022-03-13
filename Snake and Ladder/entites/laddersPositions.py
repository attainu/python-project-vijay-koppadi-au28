from random import randint
from entites import snakesPositions


ladders = {}


# This function will generate ladders position randomly
def generate_ladders():
    print()
    number_of_ladders = int(input("ENTER NUMBER OF LADDERS : "))
    i = 0
    while i < number_of_ladders:
        ladder_top = randint(11, 99)
        if ladder_top not in ladders:
            if ladder_top not in ladders.values():
                if ladder_top not in snakesPositions.snakes:
                    if ladder_top not in snakesPositions.snakes.values():
                        ladders[randint(2, ladder_top-6)] = ladder_top
                    i += 1
    print("THE LADDER STATING AND ENDING POSITIONS IS: ",ladders)

