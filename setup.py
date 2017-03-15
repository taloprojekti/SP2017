# Setup-tiedosto

##### HW SETTINGS #####
def Rele_pin():
	return int(29) # Board-pinnijaon mukainen GPIO-pinni, johon lämmittimen rele on kytketty.
	
##### LÄMPÖTILA-ASETUKSET #####
def Tmin():
	return int(19) # Minimilämpötila, johon rakennuksen sisälämmön annetaan laskea.

def Tmax():
	return int(23) # Maksimilämpötila, johon rakennuksen sisälämmön annetaan nousta.

def Tfav():
	return int(22) # Suosikkilämpötila, johon rakennuksen sisälämpö asetetaan, kun päivän sähkönhinnat ovat tasaiset.
	
##### PID-TUNING #####	
def Pgain():
	return float(1.0)
	
def Igain():
	return float(0.1)
	
def Dgain():
	return float(0.0)
	
##### RELEEN DEADBAND-ASETUKSET #####
def DBmin():
	return -0.5
	
def DBmax():
	return 0.5
