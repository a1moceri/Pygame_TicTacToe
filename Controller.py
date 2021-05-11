import random as ran
from TicTacToePlayer import *
from TicTacToeDrawingBasics import *

class Controller:
    def __init__(self):
        """
        private variable __first_move = random int [0,1]
        private variable __draw = False
        """
        self.__first_move = ran.randint(0, 1)
        self.__draw = False

    def starting_inputs(self):
        """
        print greeting for players
        take player1_name and player2_name strings
        if length of player1_name or player2_name > 12: slice string to 12 char and add '...' to string

        print coin toss message

        if __first_move = 0, player1 moves first, label1 = 0, vice versa

        player1 = TicTacToePlayer object with (player1_name, label) inputs
        player2 = TicTacToePlayer object with (player2_name, label) inputs
        :return player1, player2:
        """
        print('Greetings players! Welcome to tic tac toe!', '\n',
              'Instructions:', '\n',
              'Press the arrow keys to move the cursor.', '\n',
              'Press the space bar to mark your space.', '\n',
              "Let's play!", '\n')
        player1_name = input('Enter the name of Player 1: ')
        if len(player1_name) > 12:
            player1_name = player1_name[0:12] + '...'
        player2_name = input('Enter the name of Player 2: ')
        if len(player2_name) > 12:
            player2_name = player2_name[0:12] + '...'

        print('Now to determine who plays first! ---> If "Heads": ', player1_name, 'if "Tails":', player2_name,
              '\n', 'Toss: ')

        if self.__first_move == 0:
            print("Heads!")
            print(player1_name + " is 'X', " + player2_name + " is 'O'")
            label1 = 0
            label2 = 1
        else:
            print("Tails!")
            print(player2_name + " is 'X', " + player1_name + " is 'O'")
            label2 = 0
            label1 = 1

        player1 = TicTacToePlayer(player1_name, label1)
        player2 = TicTacToePlayer(player2_name, label2)

        return player1, player2

    def calc_winner(self, player1, player2, game_map):
        '''
        check every possible tictactoe line that could win the game if equal and check that those spots are not -1
            check if player1.get_label == that game_map spot
                :returns player1
            else:
                :returns plater2
        :param player1:
        :param player2:
        :param game_map:
        :return:
        '''
        if game_map[0][0] == game_map[0][1] == game_map[0][2] and game_map[0][0] != -1:
            if player1.get_label() == game_map[0][0]:
                return player1
            else:
                return player2

        elif game_map[1][0] == game_map[1][1] == game_map[1][2] and game_map[1][0] != -1:
            if player1.get_label() == game_map[1][0]:
                return player1
            else:
                return player2

        elif game_map[2][0] == game_map[2][1] == game_map[2][2] and game_map[2][0] != -1:
            if player1.get_label() == game_map[2][0]:
                return player1
            else:
                return player2

        elif game_map[0][0] == game_map[1][0] == game_map[2][0] and game_map[0][0] != -1:
            if player1.get_label() == game_map[0][0]:
                return player1
            else:
                return player2

        elif game_map[0][1] == game_map[1][1] == game_map[2][1] and game_map[0][1] != -1:
            if player1.get_label() == game_map[0][1]:
                return player1
            else:
                return player2

        elif game_map[0][2] == game_map[1][2] == game_map[2][2] and game_map[0][2] != -1:
            if player1.get_label() == game_map[0][2]:
                return player1
            else:
                return player2

        elif game_map[0][0] == game_map[1][1] == game_map[2][2] and game_map[0][0] != -1:
            if player1.get_label() == game_map[0][0]:
                return player1
            else:
                return player2

        elif game_map[0][2] == game_map[1][1] == game_map[2][0] and game_map[0][2] != -1:
            if player1.get_label() == game_map[0][2]:
                return player1
            else:
                return player2

        else:
            return False

    def run_game(self, player1, player2):
        '''
        creates board object from BoardBasics() class
        player1_name = player1.get_name()
        player2_name = player2.get_name()

        run = True
        while run is True:
            pygame.time.delay(80)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            winner = call calc_winner with (player1, player2, board.get_map()) args
            if winner = False:
                pass
            else:
                print winner.get_name() and winner.get_tic_tac_toe_label(),
                break loop
            if board.get_counter == 9 and winner == False
                print "DRAW"
                break loop

            board.draw_board()
            board.display_player_names(player1_name, player2_name, player1.get_tic_tac_toe_label(), player2.get_tic_tac_toe_label())
            board.display_player_move(player1, player2)
            board.mark_map()
            board.draw_char()
            pygame.display.update()

        pygame.quit()

        :param player1:
        :param player2:
        :return:
        '''
        board = BoardBasic()
        player1_name = player1.get_name()
        player2_name = player2.get_name()

        run = True
        while run:
            pygame.time.delay(80)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            winner = self.calc_winner(player1, player2, board.get_map())
            if not winner:
                pass
            else:
                break
            if board.get_counter() == 9 and not winner:
                self.__draw = True
                break

            board.draw_board()
            board.display_player_names(player1_name, player2_name, player1.get_tic_tac_toe_label(),
                                       player2.get_tic_tac_toe_label())
            board.display_player_move(player1, player2)
            board.mark_map()
            board.draw_cursor()
            pygame.display.update()

        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            if not self.__draw:
                quit = board.game_over_screen(winner.get_name(), winner.get_tic_tac_toe_label())
            else:
                quit = board.game_over_screen(None, None)
            if quit:
                break
            pygame.display.update()

        pygame.quit()
