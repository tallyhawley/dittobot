import torch
import gensim, logging
import os
import gensim.downloader as api

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

model = gensim.models.KeyedVectors.load_word2vec_format("./tmp/glove-twitter-25.txt")
print(model.most_similar("king"))
