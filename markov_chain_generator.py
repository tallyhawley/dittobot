import random

def tokenize(text):
    return text.split()


class MarkovGenerator:
    n = 2
    maxwords = 25
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
        self.beginnings.append(beginning)

        # create dictionary
        for i in range(0, len(tokens)-self.n):
            ngram = ' '.join(tokens[i:i + self.n])

            next_token = tokens[i+self.n]

            if ngram in self.ngrams:
                pass
            else:
                self.ngrams[ngram] = []

            self.ngrams[ngram].append(next_token)

    def generate(self):
        current_ngram = random.choice(self.beginnings)

        output = tokenize(current_ngram)

        for i in range(0, self.maxwords):
            if current_ngram in self.ngrams:
                # get possible next tokens
                possible_next = self.ngrams[current_ngram]
                # use choice to get a random one
                next_token = random.choice(possible_next)
                output.append(next_token);
                # get the latest n entries to generate next
                current_ngram = ' '.join(output[len(output) - self.n : len(output)])
            else:
                break

        return ' '.join(output)


