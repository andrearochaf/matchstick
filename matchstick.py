"""Match Stick Game"""
__authors__ = "gueye_d, rocha_a, taffor_l"


from sys import argv


def Matchstick(nb_line, nb_alu):
    """Lancement du jeu"""
    allumettes = game_start(nb_line)
    player1 = {
        'win': True
    }
    player2 = {
        'win': True
    }

    while(True):
        print("Player 1 turn: ")
        line = input("Line: ")
        match = input("Matches: ")
        print("Player 1 removed", match, "match(es) from line", line, ".")
        allumettes = game_on(int(nb_line), int(line), int(match))
        if allumettes == 0:
            player1["win"] = False
            break
        
        print("Player 2 turn: ")
        line = input("Line: ")
        match = input("Matches: ")
        print("Player 2 removed", match, "match(es) from line", line, ".")
        allumettes = game_on(int(nb_line), int(line), int(match))
        if allumettes == 0:
            player2["win"] = False
            break

    winner = "player1" if player1["win"] else "player2"


    print("The winner is", winner)


def game_start(nb_lines: int) -> int:
    """fonction affichage de la pyramide de base"""
    allumettes = 0
    for i in range(nb_lines):
        for j in range(2*i + 1):
            allumettes += 1
            print("|", end="")
        print("\n", end="")
    return allumettes;


def game_on(nb_line: int, line_sup: int, allum_sup: int) -> int:
    """affiche les allumettes qui reste dans la pyramide"""
    allumettes = 0
    line_sup -= 1
    for i in range(nb_line):
        supp = 0
        if i == line_sup:
            supp = allum_sup
        for j in range(2*i + 1 - supp):
            allumettes += 1
            print("|", end="")
        print("\n", end="")
    return allumettes


Matchstick(int(argv[1]), int(argv[2]))
