import pygame
import numpy as np
import time

pygame.init()


class BoardBasic:
    def __init__(self):
        self.__x = 200
        self.__y = 200
        self.__dis = 166
        self.__map = np.full((3, 3), -1)
        self.__win = pygame.display.set_mode((500, 625))
        self.__i = 1
        self.__j = 1
        self.__move = 0
        self.__counter = 0

    def draw_board(self):
        '''
        call self.__win.fill() to create black background
        call pygame.display.set_caption("Tic Tac Toe")

        call pygame.draw.lines() draw white lines in a TicTacToe formation
        :return:
        '''
        # draw board
        bg = pygame.image.load('bg.jpg')  # background image
        self.__win.blit(bg, (0, 0))
        pygame.display.set_caption("Tic Tac Toe")  # window caption

        # draw game lines
        pygame.draw.lines(self.__win, (255, 255, 255), True, [(0, 166), (500, 166)], 10)
        pygame.draw.lines(self.__win, (255, 255, 255), True, [(0, 332), (500, 332)], 10)
        pygame.draw.lines(self.__win, (255, 255, 255), True, [(166, 0), (166, 500)], 10)
        pygame.draw.lines(self.__win, (255, 255, 255), True, [(332, 0), (332, 500)], 10)

        # draw info box
        pygame.draw.lines(self.__win, (255, 255, 255), True, [(0, 500), (500, 500)], 3)
        pygame.draw.rect(self.__win, (0, 0, 0), (0, 500, 500, 500))

    def display_player_names(self, p1, p2, p1label, p2label):
        '''
        p1 = 'Player 1: ' + p1 + '(' + p1label + ')'
        p2 = 'Player 2: ' + p2 + '(' + p2label + ')'

        font = comic sans font, size 40
        player1_name = font.render(p1, True, (255, 255, 255)) create white text
        player2_name = font.render(p2, True, (255, 255, 255)) create white text

        draw player1_name at (5, 510)
        draw player2_name at (5, 540)
        :param p1:
        :param p2:
        :param p1label:
        :param p2label:
        :return:
        '''
        # display player names and label (X/O)
        p1 = 'Player 1: ' + p1 + '(' + p1label + ')'
        p2 = 'Player 2: ' + p2 + '(' + p2label + ')'

        font = pygame.font.SysFont('comicsans', 40)
        player1_name = font.render(p1, True, (255, 255, 255))
        player2_name = font.render(p2, True, (255, 255, 255))
        self.__win.blit(player1_name, (5, 510))
        self.__win.blit(player2_name, (5, 540))

    def display_player_move(self, p1, p2):
        # display who's turn it is to move
        if self.__move == p1.get_label():
            message = p1.get_name() + "'s turn! " + '(' + p1.get_tic_tac_toe_label() + ')'
        else:
            message = p2.get_name() + "'s turn! " + '(' + p2.get_tic_tac_toe_label() + ')'

        font = pygame.font.SysFont('comicsans', 55)
        move_message = font.render(message, True, (255, 0, 0))
        self.__win.blit(move_message, (22, 575))

    def draw_cursor(self):
        # draw cursor for player to mark spots with
        pygame.draw.rect(self.__win, (0, 255, 0), (self.__x, self.__y, 100, 100))
        keys = pygame.key.get_pressed()

        # move character
        if keys[pygame.K_LEFT] and self.__x > self.__dis:
            self.__x -= self.__dis
            self.__j -= 1
        if keys[pygame.K_RIGHT] and self.__x < 300:
            self.__x += self.__dis
            self.__j += 1
        if keys[pygame.K_UP] and self.__y > self.__dis:
            self.__y -= self.__dis
            self.__i -= 1
        if keys[pygame.K_DOWN] and self.__y < 300:
            self.__y += self.__dis
            self.__i += 1

        # draw cursor
        if keys[pygame.K_SPACE]:
            if self.__map[self.__i][self.__j] != -1:
                pygame.draw.rect(self.__win, (255, 0, 0), (self.__x, self.__y, 100, 100))
            else:
                self.__map[self.__i][self.__j] = self.__move   #mark self.__game_map with spot marked
                self.__counter += 1
                self.switch_move()
                time.sleep(0.2)  # gives moment to allow players to switch

    def switch_move(self):
        # allows program to switch between player moves
        if self.__move == 0:
            self.__move = 1
        else:
            self.__move = 0

    def draw_circle(self, x_cord, y_cord):
        # draws circle
        x_cord += 50
        y_cord += 50
        pygame.draw.circle(self.__win, (255, 255, 255), (x_cord, y_cord), 75, width=10)

    def draw_X(self, x_cord, y_cord):
        # draws X
        x_corner1 = x_cord - 14
        x_corner2 = x_cord + 116

        y_corner1 = y_cord - 14
        y_corner2 = y_cord + 116

        pygame.draw.lines(self.__win, (255, 255, 255), True, [(x_corner1, y_corner1), (x_corner2, y_corner2)], 5)
        pygame.draw.lines(self.__win, (255, 255, 255), True, [(x_corner1, y_corner2), (x_corner2, y_corner1)], 5)

    def mark_map(self):
        '''
        if self.__map[0][0] == 0:
            self.drawX() in appropriate coordinates
        elif self.__map =[0][0] == 1:
            self.draw_circle in appropriate coordinates
        else:
            pass
        repeat for every spot in self.__map array
        :return:
        '''
        # row 1
        if self.__map[0][0] == 0:
            self.draw_X(34, 34)
        elif self.__map[0][0] == 1:
            self.draw_circle(34, 34)
        else:
            pass
        if self.__map[1][0] == 0:
            self.draw_X(34, 200)
        elif self.__map[1][0] == 1:
            self.draw_circle(34, 200)
        if self.__map[2][0] == 0:
            self.draw_X(34, 366)
        elif self.__map[2][0] == 1:
            self.draw_circle(34, 366)
        # row 2
        if self.__map[0][1] == 0:
            self.draw_X(200, 34)
        elif self.__map[0][1] == 1:
            self.draw_circle(200, 34)
        if self.__map[1][1] == 0:
            self.draw_X(200, 200)
        elif self.__map[1][1] == 1:
            self.draw_circle(200, 200)
        if self.__map[2][1] == 0:
            self.draw_X(200, 366)
        elif self.__map[2][1] == 1:
            self.draw_circle(200, 366)
        # row 3
        if self.__map[0][2] == 0:
            self.draw_X(366, 34)
        elif self.__map[0][2] == 1:
            self.draw_circle(366, 34)
        if self.__map[1][2] == 0:
            self.draw_X(366, 200)
        elif self.__map[1][2] == 1:
            self.draw_circle(366, 200)
        if self.__map[2][2] == 0:
            self.draw_X(366, 366)
        elif self.__map[2][2] == 1:
            self.draw_circle(366, 366)

    def game_over_screen(self, winner, label):
        # draw message box
        pygame.draw.rect(self.__win, (0, 0, 0), (50, 120, 400, 250))
        pygame.draw.rect(self.__win, (255, 255, 255), (50, 120, 400, 250), width=5)

        # game over text
        font = pygame.font.SysFont('comicsans', 40)
        g_o = 'GAME OVER'
        g_o_m = font.render(g_o, True, (255, 0, 0))

        if not label:
            win_message = 'DRAW'
            draw = pygame.font.SysFont('comicsans', 75)
            w_m = draw.render(win_message, True, (0, 255, 0))
            self.__win.blit(w_m, (170, 200))
        else:
            win_message = 'THE WINNER IS:'
            winner_name = winner + '(' + label + ')'
            s_p = 250 - (len(winner_name) * 8)

            w_m = font.render(win_message, True, (0, 255, 0))
            w_n = font.render(winner_name, True, (0, 255, 0))
            self.__win.blit(w_m, (133, 200))
            self.__win.blit(w_n, (s_p, 240))

        # print game over
        self.__win.blit(g_o_m, (165, 150))

        # Quit message
        quit_message = "PRESS 'SPACE' TO QUIT"
        qm = font.render(quit_message, True, (0, 0, 255))
        self.__win.blit(qm, (90, 300))
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            pygame.quit()
            return True

    def get_map(self):
        '''
        :return self.__map:
        '''
        return self.__map

    def get_counter(self):
        '''
        :return self.__counter:
        '''
        return self.__counter

    def print_board(self):
        '''
        :return self.__map:
        '''
        return self.__map
