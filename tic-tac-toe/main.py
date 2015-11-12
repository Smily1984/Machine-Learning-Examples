"""
    Problem Task:
        Play tic-tac-toe against humans.

    Source of Experinece:
        Play games against itself.

    Measure of Performance:
        Percent of wins.
    ------------------------------------
    Target Function:
        Linear function.

    Target Function Representatnion:
        V = w0 + w1*x1 + ... + wn*xn
        where wi (i = 1..n) represents weights.

    Learning mechanism:
        LMS (Least mean squares), gradient descent.
"""

import math, random, datetime

NO_OF_TRAINING_EXAMPLES = 10000

W = [.1, .2, .3, .4, .5, .6, .7]

# Return list of free board positions
def get_possible_positions(board):
    possible_positions = []
    for i in xrange(len(board)):
        if '-' == board[i]:
            possible_positions.append(i)

    return possible_positions


def print_board(board):
    board_size = int(math.sqrt(len(board)))
    for i in xrange(board_size):
        for j in xrange(board_size):
            print (board[i*board_size + j]),
        print
    print

def gradient_descent():
    # alpha = 0.1
    # for each training example
    #     V(b) = X * weights
    #     wi = wi + alpha * (Vtrain(b) - V(b)) * xi
    pass

def number_of_ox(board):
    return board.count('O'), board.count('X')



def number_of_two_consecutive_ox(board):

    board_size = int(math.sqrt(len(board)))
    number_x = 0
    number_o = 0

    board_str = "".join(board)
    for i in xrange(board_size):
        if 2 == board_str[i*board_size : (i+1)*board_size].count('X'):
            number_x += 1
        elif 2 == board_str[i*board_size : (i+1)*board_size].count('O'):
            number_o += 1

    for i in xrange(board_size):
        if 2 == board_str[i::3].count('X'):
            number_x += 1
        if 2 == board_str[i::3].count('O'):
            number_x += 1

    diagonal_1 = board_str[0] +  board_str[4] +  board_str[8]
    diagonal_2 = board_str[2] +  board_str[4] +  board_str[6]

    if 2 == diagonal_1.count('X'):
        number_x += 1

    if 2 == diagonal_2.count('X'):
        number_x += 1

    if 2 == diagonal_1.count('O'):
        number_o += 1

    if 2 == diagonal_2.count('O'):
        number_o += 1

    return number_x, number_o



def number_of_three_consecutive_ox(board):
    board_size = int(math.sqrt(len(board)))
    number_x = 0
    number_o = 0

    board_str = "".join(board)
    for i in xrange(board_size):
        if 3 == board_str[i*board_size : (i+1)*board_size].count('X'):
            number_x += 1
        elif 3 == board_str[i*board_size : (i+1)*board_size].count('O'):
            number_o += 1

    for i in xrange(board_size):
        if 3 == board_str[i::3].count('X'):
            number_x += 1
        if 3 == board_str[i::3].count('O'):
            number_x += 1

    diagonal_1 = board_str[0] +  board_str[4] +  board_str[8]
    diagonal_2 = board_str[2] +  board_str[4] +  board_str[6]

    if 3 == diagonal_1.count('X'):
        number_x += 1

    if 3 == diagonal_2.count('X'):
        number_x += 1

    if 3 == diagonal_1.count('O'):
        number_o += 1

    if 3 == diagonal_2.count('O'):
        number_o += 1

    return number_x, number_o

def generate_move(board):
    possible_moves = get_possible_positions(board)
    # print possible_moves
    move = random.randint(0, len(possible_moves) - 1)
    return possible_moves[move]

def get_feature_vector(board):
    x_1, x_2 = number_of_ox(board)
    x_3, x_4 = number_of_two_consecutive_ox(board)
    x_5, x_6 = number_of_three_consecutive_ox(board)
    return 1, x_1, x_2, x_3, x_4, x_5, x_6

def calculate_utility(board):
    X = get_feature_vector(board)
    utility = 0
    for i in xrange(len(X)):
        utility += X[i] * W[i]

    return utility



def main():

    print " Playing against itself... Please wait... "

    """
        Features:
        - x_0   1 (bias)
        - x_1   Number of O's
        - x_2   Number of X's
        - x_3   Number of 2 consecutive O's
        - x_4   Number of 2 consecutive X's
        - x_5   Number of 3 consecutive O's (O won)
        - x_6   Number of 3 consecutive X's (X won)
    """

    # start_time = datetime.datetime.now()
    for k in xrange(NO_OF_TRAINING_EXAMPLES):
        board = ['-', '-', '-', '-', 'X', '-', '-', '-', '-']
        # print_board(board)

        while board.count('-') > 0:

            # print get_feature_vector(board)

            max_utility = -200
            for i in get_possible_positions(board):
                board[i] = 'O'
                current_utility = calculate_utility(board)
                # print "Current utility: ", current_utility
                if current_utility > max_utility:
                    max_utility = current_utility
                    computer_move = i
                # print current_utility
                board[i] = '-'

            board[computer_move] = 'O'

            learner_move = generate_move(board)
            # print "LERNM:", learner_move
            board[learner_move] = 'X'

            # print_board(board)

    # print number_of_two_consecutive_ox(board)
    # print datetime.datetime.now() - start_time

main()
