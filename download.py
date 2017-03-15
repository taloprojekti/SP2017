# Downloaderi hintadatan lukemiseksi Nordpool API:sta.

import time
from ftplib import FTP

def download(year): # parametrinä nykyinen vuosi muodossa yy (2017 -> 17)
	command="RETR heleur"+str(year)+".sdv" # Muodostetaan tiedostonimi serveriltä haettavalle tiedostolle kaavan heleuryy.sdv mukaan, missä yy on vuosiluku
	tunnus = []
	file=open("data/tunnukset.txt", "r")
	for rivi in file: # Luetaan serverin kirjautumistunnukset tiedostosta
		tunnus.append(rivi.rstrip())
	ftp = FTP("ftp.nordpoolgroup.com")
	print(ftp.login(tunnus[0], tunnus[1])) # Kirjaudutaan tunnukset.txt -tiedostosta luetuilla tunnuksilla
	time.sleep(5)
	ftp.cwd("Elspot")
	time.sleep(5)
	ftp.cwd("Elspot_prices")
	time.sleep(5)
	print(ftp.cwd("Finland")) # Siirrytään haluttuun kansioon
	time.sleep(5)
	print(ftp.retrbinary("RETR heleur17.sdv", open("data/hinta.sdv", "wb").write, blocksize=4096)) # Luetaan hintatiedot serveriltä hinta.sdv -tiedostoon data-kansiossa
	time.sleep(5)
	print(ftp.quit()) # Katkaistaan yhteys FTP-serveriin
