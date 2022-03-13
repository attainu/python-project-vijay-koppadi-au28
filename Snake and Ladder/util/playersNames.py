class PlayerNames:
    def name_of_players(N):
        names = ["player{number}".format(number = i+1) for i in range(N) ]
        print(names)
        print()
        for i in range(N):
            names[i] = input("Enter name of Player " + str(i+1) + " : ").strip()
        return names
        
