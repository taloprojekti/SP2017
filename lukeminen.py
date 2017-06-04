# Tulkintaohjelma Nordpoolin day ahead -hintatietojen lukemiseen
# txt-tiedostosta ja niiden tulkintaan aikatauluttaja-ohjelmaa varten

minim=0 #Alustetaan minimiarvon muuttuja

def minimi(tiedot):
	print(tiedot)
	minim = min(tiedot, key=tiedot.get)
	print("Min: {:.2f}".format(minim))
	return minim

def min_delta(tiedot, min): # Funktio laskee tuntien välisen hintaeron. Päivän ensimmäinen tunti näytetään nollana.
	lista=[]
	print(min)
	for rivi in tiedot:
		arvo=float(((tiedot[rivi]-tiedot[min])/tiedot[min]))
		lista.append(arvo)
		print("{:.4f}".format(arvo))
		
	print(lista)
	return lista
	
def sdvparsinta(tiedot, pvm): # Funktio hakee parsinta.py -moduulin, joka lukee hintatiedot sdv-tiedostosta python-sanakirjaksi muuttujaan tiedot
	import parsinta
	tiedot = parsinta.luesdv(tiedot, pvm)
	return tiedot

def luetiedot(pvm):
	tiedot={}
	try:
		tiedot=sdvparsinta(tiedot, pvm)

		if tiedot==False:
			tiedot=sdvparsinta(tiedot)

		for rivi in tiedot:
			print(rivi, tiedot[rivi])

	except OSError:
		print("Virhe tiedoston lukemisessa.")
		
	return tiedot
