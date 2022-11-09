import math as m
import random as r

print(m.pow(2, 5))

rand = r.random()
print(rand)

randOfList = r.choice([1, 2, 3, 4])
print(randOfList)

print(r.randrange(10, 20))
print(r.randrange(10))
print(r.randrange(9, 13, 2))

# =================================

numList = [10, 20, 30, 40, 45]
numTuple = (1, 2, 3, 4, 5)
text = 'Janusz'

print('Lista: ' + str(r.choice(numList)))
print('Tuple: ' + str(r.choice(numTuple)))
print('Text: ' + r.choice(text))

# =================================

print()
print(numList)
r.shuffle(numList)
print(numList)
