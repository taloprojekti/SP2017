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
	file = open("tasklists/tasklist-downloader.txt", "r")
	strL = file.read()
	print(strL, strN)
	if  strN != strL:
		print("Downloader ajo")
		return 0
	print("Downloader ei ajo")
	return 1
