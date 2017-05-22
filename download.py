# Downloaderi hintadatan lukemiseksi Nordpool API:sta.

import time
import ftplib

def download(year, week):
	print("Starting downloader")
	print("Trying to download data for week {:d} of {:d}".format(week, year))
	
	if week < 10:
		week = str("0{}".format(week))
	command = str("RETR spot{}{}.sdv".format((year-2000), week)) # Muodostetaan tiedostonimi serveriltä haettavalle tiedostolle kaavan spot{yy}{ww}.sdv mukaan, missä {yy} on vuosiluku ja {ww} viikko

	try:
		tunnus = []
		file=open("data/tunnukset.txt", "r")
		for rivi in file: # Luetaan serverin kirjautumistunnukset tiedostosta
			tunnus.append(rivi.rstrip())

		ftp = ftplib.FTP("ftp.nordpoolgroup.com")
		print(ftp.login(tunnus[0], tunnus[1])) # Kirjaudutaan tunnukset.txt -tiedostosta luetuilla tunnuksilla
		time.sleep(5)
		ftp.cwd("Elspot")
		time.sleep(5)
		ftp.cwd("Elspot_file") # Siirrytään haluttuun kansioon
		time.sleep(5)
		print(ftp.retrbinary("{}".format(command), open("data/hinta.sdv", "wb").write, blocksize=4096)) # Luetaan hintatiedot serveriltä hinta.sdv -tiedostoon data-kansiossa
	
	except FileNotFoundError:
		print("ERROR: Creditials file not found")
		
	except ftplib.error_perm as e:
		print("ERROR: Failed to read the file from FTP server: Error code {}".format(e.args[0][:3]))
	
	finally:
		time.sleep(5)
		print(ftp.quit())