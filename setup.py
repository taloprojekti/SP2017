# Setup-tiedosto


##### LÄMPÖTILA-ASETUKSET #####
def Tmin():
	return int(19) # Minimilämpötila, johon rakennuksen sisälämmön annetaan laskea.

def Tmax():
	return int(23) # Maksimilämpötila, johon rakennuksen sisälämmön annetaan nousta.

def Tfav():
	return int(21) # Suosikkilämpötila, johon rakennuksen sisälämpö asetetaan, kun päivän sähkönhinnat ovat tasaiset.
	
def Pgain():
	return float(1.0)
	
def Igain():
	return float(1.0)
	
def Dgain():
	return float(0.0)