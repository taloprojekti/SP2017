# Hintatietojen parsiminen Nordpoolin API:sta saatavasta XML-tiedostosta

def luexml(tiedot):
	import xml.etree.ElementTree as ET
	root = ET.parse("data/hinta.xml").getroot()

	for interval in root[9][6].findall("{urn:ediel:org:neg:ecan:publicationdocument:1:0}Interval"):
		pos = interval[0].get('v')
		price = interval[1].get('v')
		tiedot[int(pos)] = float(price)
	
	return tiedot
	
def luesdv(tiedot):
	var1=[]
	with open("data/hinta.sdv", "r") as file:
		for rivi in file:
			if "14.02.17" in rivi:
				var1=rivi.split(";")
				i=0
				while (i < 25):
					var1[i+1]=var1[i+1].replace(",",".")
					i+=1
				var1 = list(filter(None, var1))
				print(var1)
				i=0
				while (i < 24):
					tiedot[int(i)]=float(var1[i+1])
					i+=1
	return tiedot

def main():
	luesdv({})
	
main()