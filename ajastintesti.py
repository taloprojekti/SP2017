def downloaderi():
	import downloaderi 
	downloaderi.main()
	
def lampotila():
	import lampotila
	lampotila.main()	
	

def main():
	import time                           #ohjelmassa kaksi time.time looppia sillä ensimmäisella loopilla mahdollisuus 
	from datetime import datetime         #lopettaa ennen 1. tulostusta ja toisella missä muussa vaiheessa tahansa.
	import msvcrt	                #kirjasto toimii vaan ilmeisesti vaa windowsil, pitää kattoo PI:lle joku muu ratkasu
	n = 0
	ret1 = 0
	t0 = time.time()
	while time.time() - t0 < 5:
		ret1 = msvcrt.kbhit()	#tutkii onko kone valmis ottamaan syötettä vastaan ja palauttaa True jos kyllä
		if ret1 != False:
			if msvcrt.getch():		#reagoi näppäimen painamiseen
				break

	while ret1 == 0:
		
		now1 = datetime.now()
		print("{:d}:{:d}:{:d}".format(now1.hour, now1.minute, now1.second))
		t0 = time.time() - n                 #n => apumuuttuja jätätyksen estoon
		while time.time() - t0 < 1800:		#ennen while-looppia oleva näppäinreagointi ominaisuus kopsattu looppiin
			ret1 = msvcrt.kbhit()			#takaa että voi pysäyttää ohjelman missä vaiheessa tahansa
			if ret1 != False:
				if msvcrt.getch():
					return
			now2 = datetime.now()       #tässä kohtaa ohjelma tarkastaa
		  								#onko kello nn.nn ja jos on se suorittaa jtn
			if now2.minute == 0 and now2.hour == 0:
				downloaderi()                      #downloaderi kestää ~35s joka näkyy sitten alemman while-loopin ajassa: 60s->35s
				lampotila()
				t1 = time.time()
				while time.time() - t1 < 35:	#oli aikaisemmin 60s ks. edellinen kommentti	 
					ret1 = msvcrt.kbhit()	
					if ret1 != False:
						if msvcrt.getch():
							return
				n = 60                    #apumuuttuja jätätyksen estoon
			
			else:
				lampotila()
			
			
main()					
