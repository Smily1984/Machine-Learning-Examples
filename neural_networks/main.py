import gradient_descent
'''
    X = [1  x1 x2 ... xn]    - input vector
    W = [w0 w1 w2 ... wn]    - weights
    Perceptron = w0*1 + w1*x1 + ... + wn*xn
    
    if Perceptron > Threshold 
        calculated_value = 1 
    else 
        calculated_value = -1
'''

def main():
    
    # Training Examples
    TE = []
    
    # Read training examples (AND)
    f = open('gradient_descent_training_examples.txt', 'r')
    for line in f.readlines():
        example = []
        for x in line[:-1].split(' '):
            example.append(int(x))
        TE.append(example)
    f.close()
    
    learned_weights = gradient_descent.learn_weights(TE)
    print learned_weights
    
main()