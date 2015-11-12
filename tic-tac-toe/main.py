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

import math, random, datetime, copy

NO_OF_TRAINING_EXAMPLES = 1000

W = [5, 5, 5, 5, 5, 5, 5]

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

def gradient_descent(list_of_tuples):
    alpha = .1
    # pair - V(b), Vtrain(b)
    # Ako je Vtrain(b) = None => Vtrain(b) = V(b)[i+1]
    j = 0
    # print len(list_of_tuples)
    # board, train_value
    for pair in list_of_tuples:
        # print pair
        V_b = calculate_utility(pair[0])
        # print list_of_tuples[j+1]
        V_train = pair[1]
        X = get_feature_vector(pair[0])
        if V_train is None:
            # print list_of_tuples[j+1]
            V_train = calculate_utility(list_of_tuples[j+1][0])

        for i in xrange(len(W)):
            W[i] = W[i] + alpha * (V_train - V_b) * X[i]
                # wi = wi + alpha * (V_train - V_b) * xi
        j += 1


def number_of_ox(board):
    board_size = int(math.sqrt(len(board)))
    number_x = 0
    number_o = 0

    board_str = "".join(board)
    for i in xrange(board_size):
        if 1 == board_str[i*board_size : (i+1)*board_size].count('X') and 2 == board_str[i*board_size : (i+1)*board_size].count('-'):
            number_x += 1
        elif 1 == board_str[i*board_size : (i+1)*board_size].count('O') and 2 == board_str[i*board_size : (i+1)*board_size].count('-'):
            number_o += 1

    for i in xrange(board_size):
        if 1 == board_str[i::3].count('X') and 2 == board_str[i::3].count('-') :
            number_x += 1
        if 1 == board_str[i::3].count('O') and 2 == board_str[i::3].count('-'):
            number_x += 1

    diagonal_1 = board_str[0] +  board_str[4] +  board_str[8]
    diagonal_2 = board_str[2] +  board_str[4] +  board_str[6]

    if 1 == diagonal_1.count('X') and diagonal_1.count('-') == 2:
        number_x += 1

    if 1 == diagonal_2.count('X') and diagonal_1.count('-') == 2:
        number_x += 1

    if 1 == diagonal_1.count('O') and diagonal_1.count('-') == 2:
        number_o += 1

    if 1 == diagonal_2.count('O') and diagonal_1.count('-') == 2:
        number_o += 1

    return number_o, number_x



def number_of_two_consecutive_ox(board):

    board_size = int(math.sqrt(len(board)))
    number_x = 0
    number_o = 0

    board_str = "".join(board)
    for i in xrange(board_size):
        if 2 == board_str[i*board_size : (i+1)*board_size].count('X') and 1 == board_str[i*board_size : (i+1)*board_size].count('-'):
            number_x += 1
        elif 2 == board_str[i*board_size : (i+1)*board_size].count('O') and 1 == board_str[i*board_size : (i+1)*board_size].count('-'):
            number_o += 1

    for i in xrange(board_size):
        if 2 == board_str[i::3].count('X') and 1 == board_str[i::3].count('-') :
            number_x += 1
        if 2 == board_str[i::3].count('O') and 1 == board_str[i::3].count('-'):
            number_x += 1

    diagonal_1 = board_str[0] +  board_str[4] +  board_str[8]
    diagonal_2 = board_str[2] +  board_str[4] +  board_str[6]

    if 2 == diagonal_1.count('X') and diagonal_1.count('-') == 1:
        number_x += 1

    if 2 == diagonal_2.count('X') and diagonal_1.count('-') == 1:
        number_x += 1

    if 2 == diagonal_1.count('O') and diagonal_1.count('-') == 1:
        number_o += 1

    if 2 == diagonal_2.count('O') and diagonal_1.count('-') == 1:
        number_o += 1


    return number_o, number_x



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
            number_o += 1

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


    return number_o, number_x

def generate_move(board):
    possible_moves = get_possible_positions(board)
    # print possible_moves
    if len(possible_moves) > 0:
        move = random.randint(0, len(possible_moves) - 1)
        return possible_moves[move]
    return None

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

def get_train_value(board):
    X = get_feature_vector(board)
    if X[5] == 1:
        return 100

    if X[6] == 1:
        return -100

    if board.count('-') == 0:
        return 0

    return None

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
        # board = del board[:]
        board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
        # print_board(board)

        if random.randint(0, 1) == 0:
            board[random.randint(0, len(board) - 1)] = 'X'

        train_value = None
        list_of_tuples = []
        while board.count('-') > 0 and train_value is None:

            # print get_feature_vector(board)

            max_utility = None

            for i in get_possible_positions(board):
                board[i] = 'O'
                current_utility = calculate_utility(board)
                # print "Current utility: ", current_utility
                if current_utility > max_utility or max_utility is None:
                    max_utility = current_utility
                    computer_move = i
                # print current_utility
                board[i] = '-'

            # feature_vector = get_feature_vector(board)

            train_value = get_train_value(board)
            list_of_tuples.append((copy.deepcopy(board), train_value))
            board[computer_move] = 'O'

            learner_move = generate_move(board)
            # print "LERNM:", learner_move
            if learner_move is not None:
                board[learner_move] = 'X'
                #train_value = get_train_value(board)
                #list_of_tuples.append((copy.deepcopy(board), train_value))
                # train_value = get_train_value(board)
                # list_of_tuples.append((copy.deepcopy(board), train_value))

            # print_board(board)
        # feature_vector = get_feature_vector(board)

        train_value = get_train_value(board)
        list_of_tuples.append((copy.deepcopy(board), train_value))

        # print W
        #print list_of_tuples
        # print W
        #print
        # print list_of_tuples
        gradient_descent(list_of_tuples)

    # print number_of_two_consecutive_ox(board)
    # print datetime.datetime.now() - start_time
    print W


    human_board = ['-', '-', '-', '-', 'X', '-', '-', '-', '-']

    while (human_board.count('-') != 0):
        max_utility = None

        for i in get_possible_positions(human_board):
            human_board[i] = 'O'
            current_utility = calculate_utility(human_board)
            # print "Current utility: ", current_utility
            if current_utility > max_utility or max_utility is None:
                max_utility = current_utility
                computer_move = i
            # print current_utility
            human_board[i] = '-'

        human_board[computer_move] = 'O'
        print_board(human_board)
        coor_x = int(raw_input(" Input X coordinate: "))
        coor_y = int(raw_input(" Input X coordinate: "))



        human_board[coor_x * 3 + coor_y] = 'X'

main()
