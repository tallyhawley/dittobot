import torch
import gensim, logging
import os
import gensim.downloader as api
from urllib.request import urlopen

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

class initsentences(object):
    def __init__(self, dirname):
        self.dirname = dirname

    def __iter__(self):
        for fname in os.listdir(self.dirname):
            if fname == ".DS_Store":
                pass
            else:
                for line in open(os.path.join(self.dirname, fname)):
                    yield line.split()


#sentences = initsentences('./data')  # a memory-friendly iterator


#model = gensim.models.Word2Vec(sentences)

corpus = urlopen("https://dittobot.s3-us-west-1.amazonaws.com/semeval-2016-2017-task3-subtaskA-unannotated.gz")

model = gensim.models.KeyedVectors.load_word2vec_format("https://dittobot.s3-us-west-1.amazonaws.com/glove-twitter-200.txt")
#model.train(corpus)
print(model.most_similar("cat"))
print(model.most_similar("king"))
