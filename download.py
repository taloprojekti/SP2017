# Downloader for price data from Nordpool API.
import time
import ftplib

def import_credentials():
    from jsonhandler import importJSON 
    data = importJSON("data/credentials.json")
    username = data["username"]
    password = data["password"]
    return username, password

def download(year, week):
    print("Starting downloader")
    print("Trying to download data for week {:d} of {:d}".format(week, year))
    
    if week < 10:
        week = str("0{}".format(week))
    command = str("RETR spot{}{}.sdv".format((year-2000), week)) # Muodostetaan tiedostonimi serveriltä haettavalle tiedostolle kaavan spot{yy}{ww}.sdv mukaan, missä {yy} on vuosiluku ja {ww} viikko

    try:
        username, password = import_credentials()
        ftp = ftplib.FTP("ftp.nordpoolgroup.com")
        print(ftp.login(username, password)) # Kirjaudutaan tunnukset.txt -tiedostosta luetuilla tunnuksilla
        time.sleep(5)
        ftp.cwd("Elspot")
        time.sleep(5)
        ftp.cwd("Elspot_file") # Siirrytään haluttuun kansioon
        time.sleep(5)
        print(ftp.retrbinary("{}".format(command), open("data/hinta.sdv", "wb").write, blocksize=4096)) # Luetaan hintatiedot serveriltä hinta.sdv -tiedostoon data-kansiossa
    
    except FileNotFoundError:
        print("ERROR: Credentials file not found")
        
    except ftplib.error_perm as e:
        print("ERROR: Failed to read the file from FTP server: Error code {}".format(e.args[0][:3]))
    
    finally:
        time.sleep(5)
        print(ftp.quit())
