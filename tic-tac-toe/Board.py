import math, copy

class Board(object):

    def __init__(self, board):
        self._board = board
        self._size  = int(math.sqrt(len(board)))

    """
        Returns:
            -100 - winner is X player
             100 - winner is O player
               0 - it is tie
            None - game is still active
    """
    def winner(self):
        board_str = ''.join(self._board)
        board_rvr = copy.deepcopy(self._board)

        # Columns
        for i in xrange(self._size):
            if board_str[i::self._size].count('O') == self._size:
                return 100
            if board_str[i::self._size].count('X') == self._size:
                return -100

        # Rows
        for i in xrange(0, self._size**2, self._size):
            board_rvr[i:i + self._size] = reversed(board_rvr[i:i + self._size])
            if (board_str[i:i + self._size]).count('O') == self._size:
                return 100
            if (board_str[i:i + self._size]).count('X') == self._size:
                return -100

        # Diagonals
        if self._size == board_str[::self._size + 1].count('O'):
            return 100
        if self._size == board_str[::self._size + 1].count('X'):
            return -100
        if self._size == board_rvr[::self._size + 1].count('O'):
            return 100
        if self._size == board_rvr[::self._size + 1].count('X'):
            return -100

        if 0 == self._board.count('-'):
            return 0

        return None


    def __str__(self):
        board_string = ""
        for i in xrange(self._size):
            for j in xrange(self._size):
                board_string += self._board[i * self._size + j]
            board_string += '\n'
        return board_string


    """
        In this function we return features:
        - #X's in top left corner
        - #O's in top left corner
        - #X's in top right corner
        - #O's in top right corner
        - #X's in middle
        - #O's in middle
        - #X's in bottom left corner
        - #O's in bottom left corner
        - #X's in bottom right corner
        - #O's in bottom right corner
    """
    def get_features(self):
        x_1 = self._board[0].count('X')
        x_2 = self._board[0].count('O')
        x_3 = self._board[2].count('X')
        x_4 = self._board[2].count('O')
        x_5 = self._board[4].count('X')
        x_6 = self._board[4].count('O')
        x_7 = self._board[6].count('X')
        x_8 = self._board[6].count('O')
        x_9 = self._board[8].count('X')
        x_a = self._board[8].count('O')

        return [1, x_1, x_2, x_3, x_4, x_5, x_6, x_7, x_8, x_9, x_a]



    def get_possible_positions(self):
        possible_positions = []
        for i in xrange(self._size**2):
            if '-' == self._board[i]:
                possible_positions.append(i)

        return possible_positions


    def calculate_utility(self, W):
        X = self.get_features()
        utility = 0
        for i in xrange(len(X)):
            utility += X[i] * W[i]

        return utility

    def max_learner_utility(self, weights):
        max_utility = None
        learner_position = None

        for i in self.get_possible_positions():
            self._board[i] = 'O'
            current_utility = self.calculate_utility(weights)
            if current_utility > max_utility or max_utility is None:
                max_utility = current_utility
                learner_position = i
            self._board[i] = '-'

        return learner_position
