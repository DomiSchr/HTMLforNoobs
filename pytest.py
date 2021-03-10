import random
class Adresse:

	def __init__(self, strasse = "", hausnummer = "", wohnort = "", plz = ""):
		self.__strasse = strasse
		self.__hausnummer = hausnummer
		self.__wohnort = wohnort
		self.__plz = plz

	def getStrasse(self):
		print("Getter")
		return self.__strasse

	def setStrasse(self, strasse):
		print("Setter")
		self.__strasse = strasse

	def getHausnr(self):
		return self.__hausnummer

	def setHausnr(self, hausnummer):
		self.__hausnummer = hausnummer

	def getWohnort(self):
		return self.__wohnort

	def setWohnort(self, wohnort):
		self.__wohnort = wohnort

	strasse = property(getStrasse, setStrasse)


class Kunde:
	
	def __init__(self, name, vorname, kdnr, Adresse):
		self.__name = name
		self.__vorname = vorname
		self.__kdnr = kdnr
		self.__Adresse = Adresse

	def getName(self):
		return self.__name

	def getAdresse(self):
		return self.__Adresse

	def setAdresse(self, Adresse):
		self.__Adresse = Adresse


a = Adresse("Immenstadterstrasse", "62", "Mindelheim", "12345")
b = Adresse()

k = Kunde("Le", "Hai-Son", 1, a)

print(k.getAdresse().getHausnr())

