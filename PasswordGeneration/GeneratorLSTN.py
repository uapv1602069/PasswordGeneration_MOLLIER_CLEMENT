
import sys
import numpy
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
from keras.models import load_model

# --- Définition des données ---
filename = "corpus/corpus2train.txt"
raw_text = open(filename, 'r').read()

chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)

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

# --- Chargement du réseau ---
model = load_model("improvements/weights-LSTN2.hdf5")

filename = "improvements/weights-LSTN2.hdf5"
model.load_weights(filename)
model.compile(loss='categorical_crossentropy', optimizer='adam')


newFile = open("generated_passwords/passwords.txt", "a+")

# --- Génération des mots de passe
print("Generating passwords: ")
for i in range(2000000):
	result = "";
	pattern = [char_to_int[value] for value in "Seedpassw\n"]
	while(result != "\n"):
		x = numpy.reshape(pattern, (1, len(pattern), 1))
		x = x / float(n_vocab)
		#Ici, l'on choisi un caractère en fonction des probabilités définies par le modèle
		prediction = model.predict(x, verbose=0)
		probaTable = prediction[0]
		probaTable = probaTable/probaTable.sum(axis=0,keepdims=1)
		index = numpy.random.choice(range(n_vocab), p=probaTable)
		result = int_to_char[index]
		seq_in = [int_to_char[value] for value in pattern]
		newFile.write(result)
		pattern.append(index)
		pattern = pattern[1:len(pattern)]
newFile.close()
print("\nDone.")

#Taux d'erreur mot
