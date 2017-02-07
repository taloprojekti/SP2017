def main():
	import time
	from datetime import datetime
	import msvcrt	#kirjasto toimii vaan ilmeisesti vaa windowsil, pitää kattoo PI:lle joku muu ratkasu
	ret1 = 0
	t0 = time.time()
	while time.time() - t0 < 5:
		ret1 = msvcrt.kbhit()	#tutkii onko kone valmis ottamaan syötettä vastaan ja palauttaa True jos kyllä
		if ret1 != False:
			if msvcrt.getch():		#reagoi näppäimen painamiseen
				return

	while ret1 == 0:
		now1 = datetime.now()
		print("{:d}:{:d}:{:d}".format(now1.hour, now1.minute, now1.second))
		t0 = time.time()
		while time.time() - t0 < 5:		#ennen while-looppia oleva näppäinreagointi ominaisuus kopsattu looppiin
			ret1 = msvcrt.kbhit()			#takaa että voi pysäyttää ohjelman missä vaiheessa tahansa
			if ret1 != False:
				if msvcrt.getch():
					return

		now2 = datetime.now()
		print ("{:d}:{:d}:{:d}".format(now2.hour, now2.minute, now2.second)) 
		t0 = time.time()
		while time.time() - t0 < 5:		#ennen while-looppia oleva näppäinreagointi ominaisuus kopsattu looppiin
			ret1 = msvcrt.kbhit()
			if ret1 != False:
				if msvcrt.getch():
					return

main()		
