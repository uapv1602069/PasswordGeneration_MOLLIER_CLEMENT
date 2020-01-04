import random

with open('corpus/corpus2.txt','r') as source:
    data = [ (random.random(), line) for line in source ]
data.sort()
with open('corpus/corpus2shuffled.txt','w') as target:
    for _, line in data:
        target.write( line )
