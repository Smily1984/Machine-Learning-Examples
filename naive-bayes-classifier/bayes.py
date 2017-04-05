def naive_bayes_classifier(input, hypotheses, X, D):
    """
        P(h|D) = P(D|h)*p(h)/p(D)

        We can ignore P(D) because it's same for all hypothesis.
        We have two hypothesis for this problem - Yes and No.
        
        :param input: Input example we want to predict output value
        :param hypotheses: List of available classes - in the particular case ['Yes', 'No']
        :param X: Matrix of train data
        :param D: Vector (list) of target values
    """
    for h in hypotheses:
        p_h = get_probability(h, D)
        # P(h|x1, x2, x3 ... xn) = P(h|x1) * P(h|x2) * ... * P(h|xn)
        p_hx = get_probability_of_hypothesis_if_data(input, h, X, D)

        print 'Probability of class {} for input {} is {}'.format(h, input, p_h*p_hx)


def get_probability(hypothesis, D):
    return D.count(hypothesis) / (float(len(D)))


def get_probability_of_hypothesis_if_data(input, hypothesis, X, D):
    probability = 1
    n = D.count(hypothesis)
    # For each attribute
    for i in xrange(len(X[0])):
        s = 0
        for j in xrange(len(X)):
            if D[j] == hypothesis and X[j][i] == input[i]:
                s += 1

        probability *= float(s)/n

    return probability
