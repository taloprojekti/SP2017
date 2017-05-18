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
	
def tempread_all():
	import tempread
	return tempread.read_temp()
	
def write_temp(pvm):
	import tempread
	tempread.write_temp(pvm)

def main():
	
	import time          
	from datetime import datetime
	
	import setup
	import PIDclass
	import checklist
	
	
	n = 0
	ret1 = 0
	t0 = time.time()
	ret = checklist.main()
	print("Checking downloader state.")
	if ret == 0:
		downloader(now.year-2000)
		now = datetime.now()
		d = now.day
		m = now.month
		y = now.year
		stringtowrite = str(d) + str(m) + str(y)
		file = open("checklist.txt", "w")
		file.write(stringtowrite)
		file.close()
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
	
	pd_min = setup.pd_min()
	pdd_min = setup.pdd_min()
	
	PIDajo = PIDclass.PID(Pgain, Igain, Dgain, Imax, Imin) # PID-ajon alustus setup-tiedoston gain-arvoilla
	
	print("Setup complete:")
	print("	PID-Gains: P={:.1f}, I={:.1f}, D={:.1f}".format(Pgain,Igain,Dgain))
	print("	PID-Deadband: {:.1f} - {:.1f}".format(DBmin,DBmax))
	print("	Integrator range: {:.1f} - {:.1f}\n".format(Imin,Imax))
	
	try:
		print("Entering loop")
		while ret1 == 0:
			time.sleep(10)

			#Lämpötilan lukeminen
			temp_all = tempread_all()
			temp_in = float(temp_all[0])
			temp_out = float(temp_all[1])
			
			now = datetime.now()
			PID_curr = PIDajo.process(Tfav, temp_in)
			mode = "PIDctrl"
			print("{:d}:{:d}:{:d}".format(now.hour, now.minute, now.second))
			
			#PID-ajo
			print("{:.4f}".format(PID_curr)) #PID-ajon testi, pitää myöhemmin integroida ajasta riippuvan if-ehdon sisään ja yhdistää lämmittimen hallintaan.
			print(rele(mode, PID_curr, 21, temp_in, DBmax, DBmin, rele_pin))
			print()

			#Telemetria
			pvm = str("{}-{}-{};{}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
			write_temp(pvm)
			if now.minute == 57 and now.hour == 17:
				downloader(now.year)

			if now.minute == 0 and now.hour == 0:
				downloader(now.year - 2000)
				d = now.day
				m = now.month
				y = now.year
				if d < 10: 
					if m < 10:
						stringtowrite = "0" + str(d) + "0" + str(m) + str(y)
					else:	
						stringtowrite = "0" + str(d) + str(m) + str(y)
				elif d > 10 and m < 10:
					stringtowrite = str(d) + "0" + str(m) + str(y)
				else:	
					stringtowrite = str(d) + str(m) + str(y)
				file = open("checklist.txt", "w")
				file.write(stringtowrite)
				file.close()

				while now.minute == 0:
					time.sleep(1)
					now = datetime.now()
	

			#if now.minute % 30 == 0:
			#	while now.minute % 30:
			#		time.sleep(1)
			#		datetime.now()
					
	except KeyboardInterrupt:
		rele_cleanup(rele_pin)
		print("Exiting loop\n")
		return
	
main() 
