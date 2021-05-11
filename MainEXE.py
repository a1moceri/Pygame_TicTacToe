from Controller import *

def main():
    cont = Controller()
    player1, player2 = cont.starting_inputs()
    cont.run_game(player1, player2)


main()
