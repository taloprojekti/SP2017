# Hintatietojen parsiminen Nordpoolin API:sta saatavasta SDV-tiedostosta
	
def luesdv(tiedot, pvm):
		var1=[]
		with open("data/hinta.sdv", "r", encoding='iso 8859-15') as file:
			for rivi in file:
				if (("FI;EUR" in rivi) and (pvm in rivi)):
					print(rivi)
					var1=rivi.split(";")
					i=0
					while (i < 25):
						var1[i+8]=var1[i+8].replace(",",".")
						i+=1
					var1 = list(filter(None, var1))
					print(var1)
					i=0
					while (i < 24):
						tiedot[int(i)]=float(var1[i+8])
						i+=1
		return tiedot
