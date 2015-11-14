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

from Board import Board
from ExperimentGenerator import Generator
from Generalizer import Generalizer
from Critic import Critic


NO_OF_TRAINING_EXAMPLES = 1000
BOARD_LENGTH = 9

def main():

    print " Playing against itself... Please wait... "

    generator = Generator(BOARD_LENGTH)
    generalizer = Generalizer(11)
    critic = Critic(generalizer)

    wins = 0
    ties = 0
    loses = 0

    for i in xrange(NO_OF_TRAINING_EXAMPLES):

        board = generator.generate_board()
        ended = board.winner()
        while ended is None:

            weights = generalizer.get_weights()
            position = board.max_learner_utility(weights)
            # print position
            board._board[position] = 'O'

            critic.add_training_example(copy.deepcopy(board), board.winner())

            learner_move = generator.next_trainer_move(board, weights)
            if learner_move is not None:
                  board._board[learner_move] = 'X'

            ended = board.winner()

        if ended == 100:
            wins+=1
        elif ended == -100:
            loses += 1
        elif ended == 0:
            ties += 1

        critic.add_training_example(copy.deepcopy(board), ended)

        examples, values = critic.get_training_examples()
        generalizer.set_training_examples(examples)
        generalizer.set_training_values(values)
        generalizer.gradient_descent()


    W = generalizer.get_weights()

    print wins, ties, loses

    while True:
        human_board = Board(['-', '-', '-', '-', '-', '-', '-', '-', '-', ])

        vs_human = human_board.winner()
        while vs_human is None:
            x = int(raw_input(" X coordinate: "))
            y = int(raw_input(" Y coordinate: "))

            human_board._board[x*3 + y] = 'X'

            computer_position = human_board.max_learner_utility(W)
            human_board._board[computer_position] = 'O'

            print human_board

            vs_human = human_board.winner()



main()
