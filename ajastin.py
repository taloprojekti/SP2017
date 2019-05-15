def downloader(year, month, day, week):
    #downloads the data from Nordpool
    from download import download
    from jsonhandler import importJSON, writeJSON
    time = str("{:4d}-{:02d}-{:02d}".format(year, month,day))
    data = importJSON("tasklists/tasklist.json")
    if time != data["downloader_time"]:
        download(year, week)
        data["downloader_time"] = time
        writeJSON("tasklists/tasklist.json", data)
        return 1
    else:
        return 0


def rele(mode, PID, temp_req, temp_now, deadband_max, deadband_min, rele_pin):
    #Turns the relay on/off
    import rele
    tila = rele.switch(mode, PID, temp_req, temp_now, deadband_max, deadband_min, rele_pin)
    return tila
    
def rele_cleanup(rele_pin):
    #Sets the given GPIO pin for relay
    import rele
    rele.cleanup(rele_pin)
    print("GPIO cleanup done")
    
def tempread_all():
    #Reads the in- and out temperatures from sensors
    import tempread
    temp_in,temp_out = tempread.read_temp()
    return temp_in, temp_out

def write_temp(pvm):
    #Saves the temp information to data folder
    import tempread
    tempread.write_temp(pvm)

def ptulkinta(day, month, year, hour):
    #legacy code
    import tulkinta
    tulkinta.main(day, month, year, hour)
    
def mode_switch(current_time):
    #Checks if heating should be turned off
    from datetime import datetime
    from jsonhandler import importJSON
    data = importJSON("tasklists/tasklist.json")       
    i = 0
    for part in data["running_times"]:
        for time in part:
            starting_time = part[0]
            finishing_time = part[1]
            datetime1 = datetime.strptime(starting_time,"%Y-%m-%d %H:%M:%S")
            datetime2 = datetime.strptime(finishing_time,"%Y-%m-%d %H:%M:%S")
            datetime_now = datetime.strptime(current_time,"%Y-%m-%d,%H:%M:%S")
            i += 1
            if datetime_now > datetime1:
                if datetime2 > datetime_now:
                    return 1 
                else:
                    pass
            else:
                pass
    return 0
        
    #flag which rises if both time and date are in between one of these intervals
    taim = str("{:02d}:{:02d}:{:02d}".format(hour, minute, second))
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
    import algorithm
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
    week = datetime.date(y, m, d).isocalendar()[1] #Weeknumber is accessed
    ret = downloader(y, m, d, week)
    if ret == 1:
        print("download complete")
    else:
        ("download data already exists")
   
    #Initialisation of variables read from Setup.py -folder
    data = setup.read_setup()
    main_switch = setup.main_switch(data) # checks if the program is in testing- or operating mode
    rele_pin = setup.hardware_settings(data)
    Tfav, Tmin, Tmax = setup.temperatures(data)
    Pgain, Igain, Dgain, Imax, Imin = setup.pid_tuning(data)
    DBmin, DBmax = setup.relay_settings(data)
    
    PIDajo = PIDclass.PID(Pgain, Igain, Dgain, Imax, Imin) #Initialisation of PID-drive with gain values by setup-file
    
    print("Setup complete:")
    print("    PID-Gains: P={:.1f}, I={:.1f}, D={:.1f}".format(Pgain,Igain,Dgain))
    print("    PID-Deadband: {:.1f} - {:.1f}".format(DBmin,DBmax))
    print("    Integrator range: {:.1f} - {:.1f}\n".format(Imin,Imax))

    flag = 0    #This is needed in downloader
    try:
        print("Entering loop")
        print("Please wait...")
        while ret1 == 0:
            time.sleep(1)
            now = datetime.datetime.now()
            
            if(main_switch == 1):
                #Temperature reading
                temp_in,temp_out = tempread_all()
                print("Temp_in: {:.2f} Temp_out: {:.2f}".format(temp_in, temp_out))
                on_off_list = algorithm.main(d,m,y,temp_in,Tfav,Tmin,Tmax)
            elif(main_switch == 0): #Constant set temp values for testing mode
                temp_in = 20.0
                temp_out = 10.0 
                on_off_list = algorithm.main(d,m,y,temp_in,Tfav,Tmin,Tmax)
            PID_curr = PIDajo.process(Tfav, temp_in)
            # t = this moment
            # n = amount of start-end-intervals
            pvm = str("{:4d}-{:02d}-{:02d},{:02}:{:02d}:{:02d}".format(now.year, now.month, now.day, now.hour, now.minute, now.second))
            mode = mode_switch(pvm)
             

            print("Time: {:d}:{:d}:{:d}".format(now.hour, now.minute, now.second))
            
            #PID-drive
            print("PID-value: {:.4f}".format(PID_curr)) #Test of PID-drive, pitää myöhemmin integroida ajasta riippuvan if-ehdon sisään ja yhdistää lämmittimen hallintaan.
    
            if (main_switch == 1):
                print("Rele mode: {}\n".format(rele(mode, PID_curr, 21, temp_in, DBmax, DBmin, rele_pin)))
            
            else:
                print("Testing mode, heating is turned off")
            #Telemetry

            if (main_switch == 1):
                write_temp(pvm)
            if (now.minute == 0 and now.hour == 0) or (now.minute == 1 and now.hour == 0):
                print(flag)
                if flag == 0:    
                    flag = 1                    #so that this part runs only once
                    d = now.day
                    m = now.month
                    y = now.year
                    week = datetime.date(y, m, d).isocalendar()[1] #Weeknumber is accessed
                    downloader(y, m, d, week)
                    """legacy code"""
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
                        time.sleep(0.5)
                        now = datetime.now()
                else:
                    continue
            
            if (now.minute == 5 and now.hour == 0):     #resets the flag to zero value,in order to use it next time to download daily data from Nord pool
                flag = 0
                
            if (now.minute == 54 and now.hour == 3) or (now.minute == 55 and now.hour == 3):
                ptulkinta(now.day, now.month, now.year, now.hour)
            #if now.minute % 30 == 0:
            #    while now.minute % 30:
            #        time.sleep(0.5)
            #        datetime.now()
                    
    except KeyboardInterrupt:
        if(main_switch == 1):
            rele_cleanup(rele_pin)
        print("Exiting loop\n")
        return
    
main() 
