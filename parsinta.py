
# Hintatietojen parsiminen Nordpoolin API:sta saatavasta SDV-tiedostosta
	
def luesdv(tiedot, pvm):
		var1=[]
		with open("data/hinta.sdv", "r", encoding='iso 8859-15') as file:
			for rivi in file:
				if pvm in rivi:
					print(rivi)
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
		
##### Legacy-koodia #####

def luexml(tiedot):
	import xml.etree.ElementTree as ET
	root = ET.parse("data/hinta.xml").getroot()

	for interval in root[9][6].findall("{urn:ediel:org:neg:ecan:publicationdocument:1:0}Interval"):
		pos = interval[0].get('v')
		price = interval[1].get('v')
		tiedot[int(pos)] = float(price)
	
	return tiedot

def encode_utf8():
	print("Trying to convert to UTF-8")
	import codecs
	block = 32
	with codecs.open("data/hinta.sdv", "r", "iso-8859-1") as src:
		with codecs.open("data/hinta2.sdv", "w", "utf-8") as target:
			while True:
				contents = src.read(block)
				if not contents:
					break
			target.write(contents)
