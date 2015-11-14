class Critic(object):

    def __init__(self, generalizer):
        self._boards = []
        self._values = []
        self._generalizer = generalizer

    def add_training_example(self, board, value):
        self._boards.append(board)

        if len(self._values) > 0 and self._values[-1] is None:
            weights = self._generalizer.get_weights()
            self._values[-1] = board.calculate_utility(weights)

        self._values.append(value)

    def get_training_examples(self):
        return self._boards, self._values
