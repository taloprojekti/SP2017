def sisalampotila():
	sisanyt = tempread.read_temp_in()
	return sisanyt
	
def main(day, month, year, hour):
	# Setup-osa
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
	
	# Etsitään ohjelma-tilan alut ja loput
	print("entering loop")
	h=1
	while(True):
		print("h=", h)
		for rivi in min_delta[h-1:]:
			print(rivi)
			h+=1
			print("h=", h)
			if rivi > 0.19:
				print("alku") # Tähän alkuhetken tallennus
				for rivi in min_delta[h-1:]:
					print(rivi)
					h+=1
					if rivi < 0.19:
						print("stop") # Tähän päättymishetken tallennus
						break
				break
			
		# ongelmatilanne, jossa päivän viimeinen luku ei ole alle Pd tai Pdd, jolloin looppi jää avoimeksi.
		
		if h>24:
			break
	

main(19, 4, 2017, 20)

#Ratkaistaan prog-tilan aikaväli, jonka jälkeen lasketaan mihin lämpötilaan rakennus pitää lämmittää ennen välin alkua.
#Välin aikana lasketaan milloin pitää lämmittää lisää jotta lämpötila pysyy Tmin yläpuolella.