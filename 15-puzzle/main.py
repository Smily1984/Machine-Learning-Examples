from random import shuffle
from copy import deepcopy

def print_puzzle(puzzle):
    for i in xrange(4):
        for j in xrange(4):
            print str(puzzle[4*i + j]).ljust(2),
        print

def generate_puzzle():
    puzzle = [i for i in range(16)]
    shuffle(puzzle)
    return puzzle

def possible_moves(puzzle):
    moves = []

    null_position = puzzle.index(0)

    if (null_position + 4 <= 15):
        new_puzzle = deepcopy(puzzle)
        new_puzzle[null_position], new_puzzle[null_position + 4] = new_puzzle[null_position + 4], new_puzzle[null_position]
        moves.append(new_puzzle)

    if (null_position - 4 >= 0):
        new_puzzle = deepcopy(puzzle)
        new_puzzle[null_position], new_puzzle[null_position - 4] = new_puzzle[null_position - 4], new_puzzle[null_position]
        moves.append(new_puzzle)

    if (null_position + 1 <= 15 and null_position % 4 != 3):
        new_puzzle = deepcopy(puzzle)
        new_puzzle[null_position], new_puzzle[null_position + 1] = new_puzzle[null_position + 1], new_puzzle[null_position]
        moves.append(new_puzzle)

    if (null_position - 1 >= 0 and null_position % 4 != 0):
        new_puzzle = deepcopy(puzzle)
        new_puzzle[null_position], new_puzzle[null_position - 1] = new_puzzle[null_position - 1], new_puzzle[null_position]
        moves.append(new_puzzle)

    return moves


def main():

    puzzle = generate_puzzle()

    print_puzzle(puzzle)
    print
    for board in possible_moves(puzzle):
        print_puzzle(board)
        print

main()
