
from random import randint


snakes = {}

# This function will generate ladders position randomly
def generate_snakes():
    print()
    number_of_snakes = int(input("ENTER NUMBER OF SNAKES : "))

    i = 0
    while i < number_of_snakes:
        snake_head = randint(11, 99) 
        if snake_head not in snakes:
            if snake_head not in snakes.values():
                snakes[snake_head] = randint(2, snake_head-6)

            i += 1
    print("THE SNAKE HEAD AND TILE POSITIONS IS: ",snakes)

