class PlayerNames:
    def name_of_players(N):
        names = [""for i in range(N)]
        print(names)
        for i in range(N):
            names[i] = input("Enter name of Player " + str(i+1) + " : ").strip()
        return names
        
