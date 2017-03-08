import setup
import lampotila

def lukuohjelma():
	import lukuohjelma
	lukuohjelma.main()

def fav():
	fav = setup.Tfav()
	return fav	
	
def Tmin():
	Tmin = setup.Tmin()
	return Tmin
	
def Tmax():
	Tmax = setup.Tmax()
	return Tmax

def delta():
	delta = lampotila.delta()
	return delta

def hintadelta((year - 2000), month, day, hour):
	import lukeminen
	string = str(day + month + (year - 2000))
	tiedot = lukeminen.luetiedot(string)
	minimi = lukeminen.minimi()
	delta = lukeminen.delta(tiedot, minimi)

def sisalampotila()
	sisanyt = tempread.read_temp_in()
	return sisanyt
	
	
def main((year - 2000), month, day, hour):
	lukuohjelma()
	Tfav = fav()
	Tmin = Tmin()
	Tmax = Tmax()
	Tdelta = delta()
	Pdelta = hintadelta((year - 2000), month, day, hour)
	Tnow = sisalampotila()
