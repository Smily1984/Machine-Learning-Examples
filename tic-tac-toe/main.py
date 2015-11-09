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

# Return list of free board positions
def get_possible_positions(board):
    possible_positions = []
    for i in xrange(len(board)):
        if '-' == board[i]:
            possible_positions.append(i)

    return possible_positions


def gradient_descent():
    # alpha = 0.1
    # for each training example
    #     V(b) = X * weights
    #     wi = wi + alpha * (Vtrain(b) - V(b)) * xi
    pass

def number_of_ox(board):
    return board.count('O'), board.count('X')



def number_of_two_consecutive_ox(board):
    pass


def number_of_three_consecutive_ox(board):
    pass

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

    print number_of_ox(['X', 'O', '-', '-', 'X', 'X', '-', '-', 'O'])

main()
