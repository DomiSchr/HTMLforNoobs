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
	ret = True
	while ret :
		s1 = "Spieler: "
		s2 = " Feld eingeben: "
		inp = input( s1 + x + s2)
		#Check:
		if inp < 1 or inp > 9 :
			print("Eingabe ungueltig!")
		elif spielfeld[inp - 1] !=  " " : 
			print("Zug geht nicht!")
		else:
			spielfeld[inp - 1] = x
			ret = False


gewinn = True
spieler = "x"
runde = 1

while gewinn and runde < 10:
	ausg()
	spielen(spieler)

	gewinn = gewinncheck(spieler)

	if gewinn:
		if spieler == "x":
			spieler = "o"
		else:
			spieler = "x"
	
	runde += 1


if runde == 10  :
	print("Unentschieden!")
else:
	print("Spieler " + spieler + " hat gewonnen!")

ausg()
