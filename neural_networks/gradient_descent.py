import random

# training_example = [x1 x2 ... xn training_value]
# weights = [w0 w1 w2 ... wn]
def learn_weights(training_examples, iterations = 100):
    
    # len(training_example) == len(weights)
    n = len(training_examples[0])
    
    # Generate random weights 
    weights = [random.random() for w in xrange(n)]
    # print weights
    
    # Learning rate
    alpha = .1
    for iteration in xrange(iterations):
        delta_weights = [0 for w in xrange(n)]
        for example in training_examples:
            X = [1]
            X.extend(example[:-1])
            training_value = example[-1]
            
            output = weights_mul_X(weights, X)
            
            # Stochastic approximation to gradient descent
            # for i in xrange(n):
            #    weights[i] += alpha*(training_value - output)*X[i]
            
            # Standard gradient descent
            for i in xrange(n):
                delta_weights[i] += alpha*(training_value - output)*X[i]
        
        # Standard gradient descent    
        for i in xrange(n):
            weights[i] += delta_weights[i]
    
    return weights
        
# weights * X    
def weights_mul_X(weights, X):
    s = 0
    n = len(X)
    for i in xrange(n):
        s += weights[i]*X[i]
    return s
        
        