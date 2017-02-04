# Hintatietojen parsiminen Nordpoolin API:sta saatavasta XML-tiedostosta

import xml.etree.ElementTree as ET

def luetiedot(tiedot):
	root = ET.parse("data/hinta.xml").getroot()

	for interval in root[9][6].findall("{urn:ediel:org:neg:ecan:publicationdocument:1:0}Interval"):
		pos = interval[0].get('v')
		price = interval[1].get('v')
		tiedot[int(pos)] = float(price)
	
	return tiedot