import random

def zufall():
	return random.randint(1, 49)


Array = [ [0] * 6 ] * 10

for x in range(len(Array)):
	for y in range(len(Array[1])):
		Array[x][y] = zufall()

print(Array)
