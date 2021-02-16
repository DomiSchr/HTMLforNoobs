spielfeld = [" "] * 9

def ausg():
	print(spielfeld[0:3])
	print(spielfeld[3:6])
	print(spielfeld[6:9])

def gewinncheck(x):
		#Zeile:
	if (spielfeld[0] == x) and (spielfeld[1] == x) and (spielfeld[2] == x):
		return False
	elif (spielfeld[3] == x) and (spielfeld[4] == x) and (spielfeld[5] == x):
		return False
	elif (spielfeld[6] == x) and (spielfeld[7] == x) and (spielfeld[8] == x):
		return False
		#Spalten:
	elif (spielfeld[0] == x) and (spielfeld[3] == x) and (spielfeld[6] == x):
		return False
	elif (spielfeld[1] == x) and (spielfeld[4] == x) and (spielfeld[7] == x):
		return False
	elif (spielfeld[2] == x) and (spielfeld[5] == x) and (spielfeld[8] == x):
		return False
		#Diagonal:
	elif (spielfeld[0] == x) and (spielfeld[4] == x) and (spielfeld[8] == x):
		return False
	elif (spielfeld[2] == x) and (spielfeld[4] == x) and (spielfeld[6] == x):
		return False
	else:
		return True

def spielen(x):
	s1 = "Spieler: "
	s2 = " Feld eingeben: "
	inp = input( s1 + x + s2)
	spielfeld[inp - 1] = x

gewinn = True
spieler = "x"

while gewinn:
	ausg()
	spielen(spieler)

	gewinn = gewinncheck(spieler)

	if spieler == "x":
		spieler = "o"
	else:
		spieler = "x"


print("Spieler " + spieler + " hat gewonnen!")
ausg()


spielfeld = ["x", " ", " ", " ", "x", " ", " ", " ", "x"]