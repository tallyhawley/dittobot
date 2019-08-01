import random

def tokenize(text):
    return text.split()


class MarkovGenerator:
    n = 2
    maxwords = 10
    ngrams = {}
    beginnings = []

    def __init__(self, n, maxwords):
        self.n = n
        self.maxwords = maxwords


    def feed(self, text):

        # tokenize the line
        tokens = tokenize(text)

        # discard the line if too short (< n)
        if len(tokens) < self.n:
            return

        # get beginning n-gram
        beginning = ' '.join(tokens[0:self.n])
        self.beginnings.add(beginning)

        # create dictionary
        for i in range(0, len(tokens)-self.n):
            ngram = ' '.join(tokens[i:i + self.n])

            next = tokens[i+self.n]

            self.ngrams[ngram] = next

    def generate(self):
        current = random.choice(self.beginnings)
