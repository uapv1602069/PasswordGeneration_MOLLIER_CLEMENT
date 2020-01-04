# Small LSTM Network to Generate Text for Alice in Wonderland
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint, TensorBoard
from keras.utils import np_utils

# --- Définition des données
filename = "corpus/corpus2train.txt"
raw_text = open(filename, 'r').read()

chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))

n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)

#DataX va correspondre à une séquence de caractère de taille 10 et dataY au caractère qui doit suivre
#L'on modifie ensuite DataX comme une fenêtre glissante afin d'avoir toute les combinaisons de 10 caractères qui se suivent
seq_length = 10
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
	seq_in = raw_text[i:i + seq_length]
	seq_out = raw_text[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)

X = numpy.reshape(dataX, (n_patterns, seq_length, 1))

X = X / float(n_vocab)

y = np_utils.to_categorical(dataY)

# --- Définition du réseau ---
model = Sequential()
model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2]), return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256))
model.add(Dropout(0.2))
model.add(Dense(y.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')

# Les poids sont sauvegardés et les logs tensorboards également
filepath="improvements/weights-LSTN.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, save_weights_only=False, mode='min')
tensorboard_callback = TensorBoard(log_dir="logs\logsLSTN", histogram_freq=1)
callbacks_list = [checkpoint, tensorboard_callback]

model.fit(X, y, epochs=30, batch_size=128, callbacks=callbacks_list)
