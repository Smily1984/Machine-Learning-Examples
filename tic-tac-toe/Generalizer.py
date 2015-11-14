import random

class Generalizer(object):

    def __init__(self, weights_len):
        self._training_examples = []
        self._training_values = []
        self._weights = []
        for i in xrange(weights_len):
            self._weights.append(random.random())

    """
        Function for updating weights using list of board states and values
        given to each board state.
    """
    def gradient_descent(self):
        alpha = .1

        for board, V_train in zip(self._training_examples, self._training_values):
            """
            """
            V_b = board.calculate_utility(self._weights)
            X   = board.get_features()

            for i in xrange(len(self._weights)):
                # w(i) = w(i) + alpha * (Vtrain - Vb) * X(i)
                self._weights[i] += alpha * (V_train - V_b) * X[i]

    def get_weights(self):
        return self._weights

    def set_training_examples(self, training_examples):
        self._training_examples = training_examples

    def set_training_values(self, training_values):
        self._training_values = training_values
