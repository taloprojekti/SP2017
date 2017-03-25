def downloader(year):
	import download
	download.download(year-2000)
	return 0

def rele(mode, PID, temp_req, temp_now, deadband_max, deadband_min, rele_pin):
	import rele
	tila = rele.switch(mode, PID, temp_req, temp_now, deadband_max, deadband_min, rele_pin)
	return tila
	
def rele_cleanup(rele_pin):
	import rele
	rele.cleanup(rele_pin)
	print("GPIO cleanup done")
	
def tempread_in():
	import tempread
	return tempread.read_temp_in()
	
def tempread_out():
	import tempread
	return tempread.read_temp_out()

def main():
	
	import time          
	from datetime import datetime
	
	import setup
	import PIDclass
	
	
	
	n = 0
	ret1 = 0
	t0 = time.time()
	
	# Setup.py -tiedostosta luettujen muuttujien alustus
	rele_pin = setup.Rele_pin()
	Tfav = setup.Tfav()
	Pgain = setup.Pgain()
	Igain = setup.Igain()
	Dgain = setup.Dgain()
	DBmin = setup.DBmin()
	DBmax = setup.DBmax()
	Imax = setup.Imax()
	Imin = setup.Imin()
	
	PIDajo = PIDclass.PID(Pgain, Igain, Dgain, Imax, Imin) # PID-ajon alustus setup-tiedoston gain-arvoilla
	
	print("Setup complete:")
	print("	PID-Gains: P={:.1f}, I={:.1f}, D={:.1f}".format(Pgain,Igain,Dgain))
	print("	PID-Deadband: {:.1f} - {:.1f}".format(DBmin,DBmax))
	print("	Integrator range: {:.1f} - {:.1f}\n".format(Imin,Imax))
	
	try:
		print("Entering loop")
		while ret1 == 0:
			time.sleep(10)

			
			now = datetime.now()
			PID_curr = PIDajo.process(Tfav, tempread_in())
			mode = "PIDctrl"
			print("{:d}:{:d}:{:d}".format(now.hour, now.minute, now.second))
			print("{:.4f}".format(PID_curr)) #PID-ajon testi, pitää myöhemmin integroida ajasta riippuvan if-ehdon sisään ja yhdistää lämmittimen hallintaan.
			print("{:.2f}".format(tempread_in()))
			print("{:.2f}".format(tempread_out()))
			print(rele(mode, PID_curr, 21, tempread_in(), DBmax, DBmin, rele_pin))
			print()
			if now.minute == 58 and now.hour == 1:
				downloader(now.year)
				while now.minute == 0:
					time.sleep(1)
					now = datetime.now()

			if now.minute % 30 == 0: 
				tempread_in() 
				while now.minute % 30:
					time.sleep(1)
					datetime.now()
					
	except KeyboardInterrupt:
		print("Exiting loop\n")
		rele_cleanup(rele_pin)
		return
	
main()	
