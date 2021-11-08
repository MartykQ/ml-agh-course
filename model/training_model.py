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

embedding_matrix = word2vec_model.vectors

top_words = embedding_matrix.shape[0]
mxlen = 50
nb_classes = 3

#vocabulary index update
tokenizer = Tokenizer(num_words=top_words)
tokenizer.fit_on_texts(X_train)

#texts_to_sequences Transforms each text in texts to a sequence of integers
sequences_train = tokenizer.texts_to_sequences(X_train)
sequences_test = tokenizer.texts_to_sequences(X_test)
sequences_val = tokenizer.texts_to_sequences(X_val)

word_index = tokenizer.word_index

#Pads sequences to the same length.
X_train = sequence.pad_sequences(sequences_train, maxlen=mxlen)
X_test = sequence.pad_sequences(sequences_test, maxlen=mxlen)
X_val = sequence.pad_sequences(sequences_val, maxlen=mxlen)

#to categorical converts a class vector (integers) to binary class matrix.
y_train = np_utils.to_categorical(y_train, nb_classes)
y_test = np_utils.to_categorical(y_test, nb_classes)
y_val = np_utils.to_categorical(y_val, nb_classes)

#creating LST network model (kind of RNN)

batch_size = 32
nb_epoch = 3

embedding_layer = Embedding(embedding_matrix.shape[0],
                            embedding_matrix.shape[1],
                            weights=[embedding_matrix],
                            trainable=False)

model = Sequential()
model.add(embedding_layer)
model.add(LSTM(128, recurrent_dropout=0.5, dropout=0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))
#model.summary()


#compile and train

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
rnn = model.fit(X_train, y_train, epochs= nb_epoch, batch_size=batch_size, shuffle=True, validation_data=(X_val, y_val))
score = model.evaluate(X_val, y_val)


#saving model

# print('Save model...')
# model.save('Models/finalsentimentmodel.h5')
# print('Saved model to disk...')

# print('Save Word index...')
# output = open('Models/finalwordindex.pkl', 'wb')
# pickle.dump(word_index, output)
# print('Saved word index to disk...')



