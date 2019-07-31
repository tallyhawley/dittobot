import torch
import gensim, logging
import os
import gensim.downloader as api
from urllib.request import urlopen
from keras.layers.recurrent import LSTM
from keras.layers.embeddings import Embedding
from keras.models import Model, Sequential
from keras.layers import Dense, Activation

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


# sentences = initsentences('./data')  # a memory-friendly iterator


# model = gensim.models.Word2Vec(sentences)

corpus = urlopen("https://dittobot.s3-us-west-1.amazonaws.com/semeval-2016-2017-task3-subtaskA-unannotated.gz")

model = gensim.models.KeyedVectors.load_word2vec_format("https://dittobot.s3-us-west-1.amazonaws.com/glove-twitter-200.txt")
# model.train(corpus)

pretrained_weights = model.wv.syn0
vocab_size, embedding_size = pretrained_weights.shape

print('Result embedding shape:', pretrained_weights.shape)
print('Checking similar words:')
for word in ['model', 'network', 'train', 'learn']:
    most_similar = ', '.join('%s (%.2f)' % (similar, dist)
                           for similar, dist in model.most_similar(word)[:8])
    print('  %s -> %s' % (word, most_similar))


def word2idx(word):
    return model.wv.vocab[word].index


def idx2word(idx):
    return model.wv.index2word[idx]

keras_model = Sequential()
keras_model.add(Embedding(input_dim=vocab_size, output_dim=embedding_size,
                    weights=[pretrained_weights]))
keras_model.add(LSTM(units=embedding_size))
keras_model.add(Dense(units=vocab_size))
keras_model.add(Activation('softmax'))
keras_model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')
