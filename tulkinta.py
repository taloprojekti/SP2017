def hintadelta(year, month, day, hour):
	import lukeminen
	if day < 10:
		day = str(day)
		day = str("0"+day)
	if month < 10:
		month = str(month)
		month = str("0"+month)
	pvm = str("{}.{}.{}".format(day, month, year-2000))
	print(pvm)
	tiedot = lukeminen.luetiedot(pvm)
	minimi = lukeminen.minimi(tiedot)
	min_delta = lukeminen.min_delta(tiedot, minimi)
	ddP = lukeminen.deltadeltaP(min_delta)
#def sisalampotila()
#	sisanyt = tempread.read_temp_in()
#	return sisanyt
	
	
#def main((year - 2000), month, day, hour):
#	lukuohjelma()
#	Tfav = fav()
#	Tmin = Tmin()
#	Tmax = Tmax()
#	Tdelta = delta()
#	Pdelta = hintadelta((year - 2000), month, day, hour)
#	Tnow = sisalampotila()

def test():
	hintadelta(2017, 3, 2, 14)

test()	