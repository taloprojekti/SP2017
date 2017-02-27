# Tulkintaohjelma Nordpoolin day ahead -hintatietojen lukemiseen
# txt-tiedostosta ja niiden tulkintaan aikatauluttaja-ohjelmaa varten

######### DATAN TUOTTO #########

jarj=[] #Alustetaan hintajärjestyksen muuttuja
minim=0 #Alustetaan minimiarvon muuttuja

def jarjestys(tiedot): # Funktio luo listan tunneista, joka on järjestetty halvimmasta kalleimpaan.
	i=0
	keys=tiedot.keys()
	
	lista=sorted(keys, key=tiedot.__getitem__)
	return lista

def minimi(tiedot):
	minim = min(tiedot, key=tiedot.get)
	print(minim)
	return minim

def delta(tiedot, min): # Funktio laskee tuntien välisen hintaeron. Päivän ensimmäinen tunti näytetään nollana.
	lista=[]
	for rivi in tiedot:
		if rivi > 0:
			arvo=float(((tiedot[rivi]-tiedot[min])/tiedot[min]))
			lista.append(arvo)
		else:
			arvo = 0
			lista.append(arvo)
		print("{:.2f}".format(arvo))
	return lista
		
def xmlparsinta(tiedot): # Funktio hakee parsinta.py -moduulin, joka lukee hintatiedot xml-tiedostosta python-sanakirjaksi muuttujaan tiedot
	import parsinta
	tiedot = parsinta.luexml(tiedot)
	return tiedot
	
def sdvparsinta(tiedot, aika): # Funktio hakee parsinta.py -moduulin, joka lukee hintatiedot sdv-tiedostosta python-sanakirjaksi muuttujaan tiedot
	import parsinta
	tiedot = parsinta.luesdv(tiedot, aika)
	return tiedot
	
######### MAIN #########
def main():
	tiedot={}
	aika="18.02.17"
	try:
		tiedot=sdvparsinta(tiedot, aika)
		for rivi in tiedot:
			print(rivi, tiedot[rivi])

		jarj=jarjestys(tiedot)
		minim=minimi(tiedot)
		muutos=delta(tiedot, minim)
		print(muutos)
	except OSError:
		print("Virhe tiedoston lukemisessa.")
	
main()