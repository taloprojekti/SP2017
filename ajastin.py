def downloader(year, month, day, week):
    import download
    download.download(year, week)
    return 0

def rele(mode, PID, temp_req, temp_now, deadband_max, deadband_min, rele_pin):
    import rele
    tila = rele.switch(mode, PID, temp_req, temp_now, deadband_max, deadband_min, rele_pin)
    return tila
    
def rele_cleanup(rele_pin):
    import rele
    rele.cleanup(rele_pin)
    print("GPIO cleanup done")
    
def tempread_all():
    import tempread
    return tempread.read_temp()
    
def write_temp(pvm):
    import tempread
    tempread.write_temp(pvm)

def ptulkinta(day, month, year, hour):
    import tulkinta
    tulkinta.main(day, month, year, hour)
    
def mode_switch(hour, minute, second):
    import csv
    with open('tasklists/tasklist-prog.csv', "r") as f: 
        fileReader = csv.reader(f)
        arr = []                    #matriisi jonka yksi rivi sisältää aina yhden rivin tiedot
        for row in fileReader:
            arr.append(row)
    f.close()
    #for looppi joka vetää filen läpi start-end-intervalleissa
    #flag joka nousee jos time sekä date ovat jollain näistä väleistä

    if second < 10:
        second = str(second)
        second = "0"+second
    if minute < 10:
        minute = str(minute)
        minute = "0"+minute
    if hour < 10:
        hour = str(hour)
        hour = "0"+hour
    taim = str("{}:{}:{}".format(hour, minute, second))
    n = 1
    print("len:{:d}".format(len(arr)))
    flag = 0
    while n < len(arr):
        if taim > arr[n-1][2] and taim < arr[n][2]:
            flag = 1
            n += 1
        else:    
            print("kierros:{:d}".format(n))
            n += 1    
    if flag == 1:
        mode = "prog"
        flag = 0
    else:
        mode = "PIDctrl"
    return mode

def main():
    import time          
    import datetime
    
    import setup
    import PIDclass
    import checklist
    
    n = 0
    ret1 = 0
    t0 = time.time()

    print("Checking downloader state.")
    ret = checklist.main()
    print("Initialising clock.")
    now = datetime.datetime.now()
    d = now.day
    m = now.month
    y = now.year
    week = datetime.date(y, m, d).isocalendar()[1] #Haetaan viikkonumero

    if ret == 0:
        downloader(y, m, d, week)

        if d < 10:
            if m < 10:
                strN = "0" + str(d) + "0" + str(m) + str(y)
            else:    
                strN = "0" + str(d) + str(m) + str(y)
        if m < 10 and d > 10:
            strN = str(d) + "0" + str(m) + str(y)
        else:
            strN = str(d) + str(m) + str(y)
        file = open("tasklists/tasklist-downloader.txt", "w")
        file.write(strN)

        file.close()
        # Setup.py -tiedostosta luettujen muuttujien alustus
    data = setup.read_setup()
    main_switch = setup.main_switch(data) # checks if the program is in testing- or operating mode
    rele_pin = setup.hardware_settings(data)
    Tfav, Tmin, Tmax = setup.temperatures(data)
    Pgain, Igain, Dgain, Imax, Imin = setup.pid_tuning(data)
    DBmin, DBmax = setup.relay_settings(data)
    
    PIDajo = PIDclass.PID(Pgain, Igain, Dgain, Imax, Imin) # PID-ajon alustus setup-tiedoston gain-arvoilla
    
    print("Setup complete:")
    print("    PID-Gains: P={:.1f}, I={:.1f}, D={:.1f}".format(Pgain,Igain,Dgain))
    print("    PID-Deadband: {:.1f} - {:.1f}".format(DBmin,DBmax))
    print("    Integrator range: {:.1f} - {:.1f}\n".format(Imin,Imax))

    flag = 0    #tarvitaan downloaderissa

    try:
        print("Entering loop")
        while ret1 == 0:
            time.sleep(10)    
            if(main_switch == 1):
                #Lämpötilan lukeminen
                temp_all = tempread_all()
                temp_in = float(temp_all[0])
                temp_out = float(temp_all[1])
                
                now = datetime.datetime.now()
            elif(main_switch == 0): # kiinteästi asetettavat lämpötilat testausta varten
                temp_in = 20.0
                temp_out = 10.0

            PID_curr = PIDajo.process(Tfav, temp_in)
            # t = tämä hetki
            # n = start-end-intervallien määrä
                            
            mode = mode_switch(now.hour, now.minute, now.second)

            print("{:d}:{:d}:{:d}".format(now.hour, now.minute, now.second))
            
            #PID-ajo
            print("{:.4f}".format(PID_curr)) #PID-ajon testi, pitää myöhemmin integroida ajasta riippuvan if-ehdon sisään ja yhdistää lämmittimen hallintaan.
            if(main_switch == 1):
                print("{}\n".format(rele(mode, PID_curr, 21, temp_in, DBmax, DBmin, rele_pin)))

            #Telemetria

            pvm = str("{}-{}-{},{}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
            if(main_switch == 1):
                write_temp(pvm)
            if (now.minute == 0 and now.hour == 0) or (now.minute == 1 and now.hour == 0):
                print(flag)
                if flag == 0:    
                    flag = 1                    #jotta mentäisiin tähän vain kerran
                    d = now.day
                    m = now.month
                    y = now.year
                    week = datetime.date(y, m, d).isocalendar()[1] #Haetaan viikkonumero
                    downloader(y, m, d, week)
                    if d < 10:
                        if m < 10:
                            stringtowrite = "0" + str(d) + "0" + str(m) + str(y)
                        else:    
                            stringtowrite = "0" + str(d) + str(m) + str(y)
                    elif d > 10 and m < 10:
                        stringtowrite = str(d) + "0" + str(m) + str(y)
                    else:    
                        stringtowrite = str(d) + str(m) + str(y)
                    file = open("checklist.txt", "w")
                    file.write(stringtowrite)
                    file.close()

                    while now.minute == 0:
                        time.sleep(1)
                        now = datetime.now()
                else:
                    continue
                    
            if (now.minute == 5 and now.hour == 0):     #resetoi flagin nollaksi, jotta sitä voidaan käyttää ensi keskiyönä
                flag = 0
                
            if (now.minute == 54 and now.hour == 3) or (now.minute == 55 and now.hour == 3):
                ptulkinta(now.day, now.month, now.year, now.hour)

            #if now.minute % 30 == 0:
            #    while now.minute % 30:
            #        time.sleep(1)
            #        datetime.now()
                    
    except KeyboardInterrupt:
        if(main_switch == 1):
            rele_cleanup(rele_pin)
        print("Exiting loop\n")
        return
    
main() 
