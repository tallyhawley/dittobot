import torch
import gensim, logging
import os
import gensim.downloader as api
from urllib.request import urlopen
from keras.layers.recurrent import LSTM
from keras.layers.embeddings import Embedding
from keras.models import Model, Sequential
from keras.layers import Dense, Activation
import numpy as np

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
keras_model.compile(optimizer='adam', loss='categorical_crossentropy')


def sample(preds, temperature=1.0):
  if temperature <= 0:
    return np.argmax(preds)
  preds = np.asarray(preds).astype('float64')
  preds = np.log(preds) / temperature
  exp_preds = np.exp(preds)
  preds = exp_preds / np.sum(exp_preds)
  probas = np.random.multinomial(1, preds, 1)
  return np.argmax(probas)


def generate_next(text, num_generated=10):
  word_idxs = [word2idx(word) for word in text.lower().split()]
  for i in range(num_generated):
    prediction = model.predict(x=np.array(word_idxs))
    idx = sample(prediction[-1], temperature=0.7)
    word_idxs.append(idx)
  return ' '.join(idx2word(idx) for idx in word_idxs)
