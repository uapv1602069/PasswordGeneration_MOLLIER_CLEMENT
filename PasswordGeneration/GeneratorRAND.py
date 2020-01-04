
# Load LSTM network and generate text
import sys
import numpy
import random

filename = "corpus/corpus2train.txt"
raw_text = open(filename, 'r').read()

chars = sorted(list(set(raw_text)))
chars.remove("\n")
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))

n_vocab = len(chars)
print("Total Vocab: ", n_vocab)

newFile = open("generated_passwords/passwordsRand.txt", "a+")

print("Generating passwords: ")
for i in range(2000000):
	result = "";
	i = 0;
	size = random.randint(4,11)
	while(i != size):
		char = random.randint(0,n_vocab-1)
		result = int_to_char[char]
		newFile.write(result)
		i = i+1
	newFile.write("\n")
newFile.close()
print("\nDone.")

#Taux d'erreur mot
