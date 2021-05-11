class TicTacToePlayer:
    # Accepts a player’s name and label and initializes those attributes.
    def __init__(self, player, label):
        self.__player = player
        self.__label = label

    # This returns 0 (for X) or 1 (for O)
    def get_label(self):
        return self.__label

    # This returns X if label is zero, and O if label is 1
    def get_tic_tac_toe_label(self):
        if self.__label == 0:
            return 'X'
        else:
            return 'O'

    # Returns the name of the player
    def get_name(self):
        return self.__player
