def main():    
    from datetime import datetime
    from jsonhandler import importJSON
    nownew = datetime.now()
    p = nownew.day
    k = nownew.month
    v = nownew.year
    strN = str("{:02d}{:02d}{:4d}".format(p, k, v))
    data = importJSON("tasklists/tasklist.json")
    strL = data["downloader_time"]
    print(strL, strN)
    if  strN != strL:
        print("Downloader ajo")
        return 0
    print("Downloader ei ajo")
    return 1
