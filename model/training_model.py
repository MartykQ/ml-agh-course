import numpy as np
import pandas as pd
import matplotlib.pylab as plt
from livelossplot import PlotLossesKeras
np.random.seed(7)
from sklearn.model_selection import train_test_split
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, LSTM
from keras.layers.embeddings import Embedding
from keras.utils import np_utils
from tensorflow.keras.preprocessing import sequence
from gensim.models import Word2Vec, KeyedVectors, word2vec
import gensim
from gensim.utils import simple_preprocess
from tensorflow.keras.utils import to_categorical
import pickle
import h5py
from time import time



filename = 'data/polish_sentiment_dataset.csv'

dataset = pd.read_csv(filename, delimiter = ",")



# Delete unused column
del dataset['length']

# Delete All NaN values from columns=['description','rate']
dataset = dataset[dataset['description'].notnull() & dataset['rate'].notnull()]

# We set all strings as lower case letters
dataset['description'] = dataset['description'].str.lower()



#print(dataset.head())

X = dataset['description']
y = dataset['rate']

#podzial na uczacy, walidacyjny, testowy
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.2, random_state=42)

#stworzenie wektoru słów na bazie modelu z polskiej akademii nauk
word2vec_model = gensim.models.KeyedVectors.load_word2vec_format('nkjp.txt', binary=False)