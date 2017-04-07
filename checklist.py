def main():	
	from datetime import datetime
	nownew = datetime.now()
	p = nownew.day
	k = nownew.month
	v = nownew.year
	strN = str(p) + str(k) + str(v)
	file = open("checklist.txt", "r")
	strL = file.read()
	if  strN != strL:
		return 0
	return 1	
main()	
