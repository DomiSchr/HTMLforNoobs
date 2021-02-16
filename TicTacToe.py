spielfeld = [" "] * 9

def ausg():
	print(spielfeld[0:3])
	print(spielfeld[3:6])
	print(spielfeld[6:9])

def gewinncheck(x):
		#Zeile:
	if (spielfeld[0] == x) and (spielfeld[1] == x) and (spielfeld[2] == x):
		return True
	elif (spielfeld[3] == x) and (spielfeld[4] == x) and (spielfeld[5] == x):
		return True
	elif (spielfeld[6] == x) and (spielfeld[7] == x) and (spielfeld[8] == x):
		return True
		#Spalten:
	elif (spielfeld[0] == x) and (spielfeld[3] == x) and (spielfeld[6] == x):
		return True
	elif (spielfeld[1] == x) and (spielfeld[4] == x) and (spielfeld[7] == x):
		return True
	elif (spielfeld[2] == x) and (spielfeld[5] == x) and (spielfeld[8] == x):
		return True
		#Diagonal:
	elif (spielfeld[0] == x) and (spielfeld[4] == x) and (spielfeld[8] == x):
		return True
	elif (spielfeld[2] == x) and (spielfeld[4] == x) and (spielfeld[6] == x):
		return True
	else:
		return False

#input = input("Spieler 'x' Feld eingeben: ")
#spielfeld[input - 1] = "x"

spielfeld = ["x", " ", " ", " ", "x", " ", " ", " ", "x"]

print(gewinncheck("x"))


ausg()
