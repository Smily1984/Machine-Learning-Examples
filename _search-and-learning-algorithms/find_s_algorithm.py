"""
    @author:    Dragutin Marjanovic
    @e-mail:    dmarjanovic94@gmail.com

    FIND-S algorithm
        This is algorithm that search most specific hypothesis. It means that
        we find hypotesis that all learning examples have to satisfy. Also, we
        avoid negative training examples.

        hypotesis <- most specific [-, -, -, - ... -]

        for each 'example' in 'training_examples':
            if 'example' is 'positive':
                for each 'feature' in 'features':
                    if 'feature' != hypotesis.feature
                        if  hypotesis.feature = '-':
                            hypotesis.feature = 'feature'
                        else:
                            hypotesis.feature = '?'
            else:
                we just pass negative example...
"""

# We will just add some training examples to the list
def generate_examples():
    training_examples = []

    training_examples.append(['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same', True])
    training_examples.append(['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same', True])
    training_examples.append(['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change', False])
    training_examples.append(['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change', True])

    return training_examples


def find_s(feature_no, training_examples):
    most_specific = []
    for i in xrange(feature_no):
        most_specific.append('-')

    for example in training_examples:
        if example[feature_no] is True:
            for i in xrange(feature_no):
                if example[i] != most_specific[i]:
                    if most_specific[i] == '-':
                        most_specific[i] = example[i]
                    else:
                        most_specific[i] = '?'

    return most_specific

def main():
    print find_s(6, generate_examples())

main()
