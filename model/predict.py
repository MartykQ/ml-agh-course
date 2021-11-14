import logging
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' # noqa
import pickle

import numpy as np
from keras.models import load_model
from keras.preprocessing import sequence
from keras.preprocessing.text import Tokenizer

model = load_model(os.path.join(os.getcwd(), 'model', 'finalsentimentmodel.h5'))
with open(os.path.join(os.getcwd(), 'model', 'finalwordindex.pkl'), 'rb') as picklefile:
    logging.info("Loading pickle")
    print("loading pickle")
    word_index = pickle.load(picklefile)


def predict(text):
    # possible classes
    text = str(text.encode('utf-8'))

    classes = ["Neutral", "Positive", "Negative"]
    logging.info(f"Making prediction for: {text}")
    # string to array
    text_array = [text]

    # model load

    # model.summary()

    # loading word index

    top_words = len(word_index)
    tokenizer = Tokenizer(num_words=top_words)
    tokenizer.word_index = word_index

    # converting text to integers
    test_sequences = tokenizer.texts_to_sequences(text_array)
    x_test = sequence.pad_sequences(test_sequences, maxlen=40)

    # results

    result = model.predict(x_test)
    # print(result)
    # print("Neutral: %.2f%%" % (result[:,0]*100))
    # print("Positive: %.2f%%" % (result[:,1]*100))
    # print("Negative: %.2f%%" % (result[:,2]*100))
    # print(np.argmax(result[0]))

    # predicted class
    predicted_class = classes[np.argmax(result[0])]

    return predicted_class
