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
	
def maksimi(tiedot):
	maxim = max(tiedot, key=tiedot.get)
	print(maxim)
	return maxim

def min_delta(tiedot, min): # Funktio laskee tuntien välisen hintaeron. Päivän ensimmäinen tunti näytetään nollana.
	lista=[]
	print(min)
	print("paska")
	for rivi in tiedot:
		arvo=float(((tiedot[rivi]-tiedot[min])/tiedot[min]))
		lista.append(arvo)
		print("{:.4f}".format(arvo))
		
	print(lista)
	return lista
	
def max_delta(tiedot, max): # Funktio laskee tuntien välisen hintaeron. Päivän ensimmäinen tunti näytetään nollana.
	lista=[]
	print(max)
	print("paska")
	for rivi in tiedot:
		arvo=float(((tiedot[rivi])/tiedot[max]))
		lista.append(arvo)
		print("{:.2f}".format(arvo))
	return lista
		
def hinta_delta(tiedot): # Funktio laskee tuntien välisen hintaeron. Päivän ensimmäinen tunti näytetään nollana.
	lista=[]
	for rivi in tiedot:
		arvo=float(tiedot[rivi+1]-tiedot[rivi])
		lista.append(arvo)
		print("{:.2f}".format(arvo))
	return lista

def deltadeltaP(delta):
	i=0
	ddP=[]
	while i <= 22:
		arvo=delta[i+1]-delta[i]
		ddP.append(arvo)
		print(arvo)
		i+=1
	return ddP
		
def xmlparsinta(tiedot): # Funktio hakee parsinta.py -moduulin, joka lukee hintatiedot xml-tiedostosta python-sanakirjaksi muuttujaan tiedot
	import parsinta
	tiedot = parsinta.luexml(tiedot)
	return tiedot
	
def sdvparsinta(tiedot, pvm): # Funktio hakee parsinta.py -moduulin, joka lukee hintatiedot sdv-tiedostosta python-sanakirjaksi muuttujaan tiedot
	import parsinta
	tiedot = parsinta.luesdv(tiedot, pvm)
	return tiedot
	
######### MAIN #########
def luetiedot(pvm):
	tiedot={}
	try:
		tiedot=sdvparsinta(tiedot, pvm)
		if tiedot==False:
			tiedot=sdvparsinta(tiedot, pvm)
		for rivi in tiedot:
			print(rivi, tiedot[rivi])

		jarj=jarjestys(tiedot)
		minim=minimi(tiedot)

	except OSError:
		print("Virhe tiedoston lukemisessa.")
		
	return tiedot
