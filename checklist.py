def main():	
	from datetime import datetime
	nownew = datetime.now()
	p = nownew.day
	k = nownew.month
	v = nownew.year
	if p < 10: 
		if k < 10:
			strN = "0" + str(p) + "0" + str(k) + str(v)
		else:	
			strN = "0" + str(p) + str(k) + str(v)
	if k < 10 and p > 10:
		strN = str(p) + "0" + str(k) + str(v)
	else:	
		strN = str(p) + str(k) + str(v)
	file = open("checklist.txt", "r")
	strL = file.read()
	if  strN != strL:
		return 0
	return 1	
main()	
