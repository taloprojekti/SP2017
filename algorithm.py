def derivatives(d, m, y):
    from jsonhandler import writeJSON
    from parsinta import luesdv
    from lukeminen import luetiedot
    tiedot ={}
    slopelist = []
    date = ("{:02}.{:02}.{:4d}".format(d, m, y))
    data = luesdv(tiedot,date)
    writeJSON("data/graph.json",data)
    i = 0
    #calculates the slopes of hinta.sdv for every hour.
    while i < 24:
        if i != 0:
            slope = data[i] - data[i-1]
            slopelist.append(slope)
            i += 1
        else:
            slope = 0
            slopelist.append(slope)
            i += 1

    return data, slopelist

def price_average(data):
    #Calculates the average price of electricity
    total = 0
    i = 0
    while i < 23: 
        total += data[i]
        i += 1
    average = total / i
    return average

def exception(data, average,on_off_list,i):
    on_off_list.append(0)
    on_off_list.insert(i+1, 1)
    i += 2
    return i


def compare_prices(data,slopelist,average,temp_in,Tfav,Tmin,Tmax):
    """Creates a list which includes hourly information if heating should be on/off"""
    on_off_list = []
    i = 0
    while i < 24:
        try:
            if temp_in >= Tmax:
                on_off_list.append(0)
                i += 1
                continue
            if temp_in <= Tmin:
                on_off_list.append(1)
                i += 1
                continue
            if data[i] > average:
                if data[i-1] >= data[i] and data[i+1] < average:
                        i = exception(data, average, on_off_list,i)
                        continue
                elif  data[i-1] < data[i] and data[i+1] < average:
                    i= exception(data, average,on_off_list,i)
                    continue
                #checks if there is current local minimum
                elif data[i+1] > average and slopelist[i+1] < 0:
                    if data[i] > data[i+1]:
                        if slopelist[i+2] > 0:
                           i = exception(data, average,on_off_list,i)
                           continue
                        else:
                            on_off_list.append(0)
                            i += 1
                    else:
                        on_off_list.append(0)
                        i += 1
                    
                    
                else:
                    on_off_list.append(0)
                    i += 1
            else:
                on_off_list.append(1)
                i += 1
        
        except IndexError:
            if data[i] < average:
                on_off_list.append(1)
                i += 1
        
            else:
                on_off_list.append(0)
                i += 1
        except KeyError:
            if i == 23:
                if data[i] < average:
                    on_off_list.append(1)
                    i += 1
                else:
                    on_off_list.append(0)
                    i += 1
            else:
                if data[i] < average:
                    on_off_list.append(1)
                    i += 1
                else:
                    on_off_list.append(0)
                    i += 1
    print("Rele mode values:")
    print(on_off_list)
    from jsonhandler import writeJSON
    writeJSON("data/graph2.json",on_off_list)
    return on_off_list

def mode_list(on_off_list,y,m,d):
    """Creates a list of times when heating is on"""
    from jsonhandler import writeJSON
    from jsonhandler import importJSON
    time_list = []
    i = 0
    mi = 0
    s = 0
    amount = 0
    #amount is the amount of time gaps when heating is on
    while i < 24:
        try:
            if i == 23:
                if on_off_list[i] == 1:
                    if on_off_list[i-1] == 0:
                        amount += 1
                        break
                else:
                    break
            if i == 0:
                if on_off_list[i] == 1:
                    amount += 1
                    i += 1
                    continue
                else:
                    i += 1
            elif on_off_list[i] == 1:
                if on_off_list[i-1] == 0:
                    amount += 1
                    i += 1
                else:
                    i += 1
            else:
                i += 1

        except IndexError:
            
            if i == 0 and  on_off_list[i] == 1:
                amount += 1
                i += 1

            else:
                i += 1
    running_times = {}
    for value in range(amount):
        time_list.append([])
    i = 0
    index = 0
    amount_of_ones = 0
    #Creates the correct form for the file tasklist is upgraded when needed
    while i < 24:
        try:
            if i == 0:
            
                if on_off_list[i] == 1:
                    time_list[index].append("{:4d}-{:02d}-{:02d} {:02}:{:02d}:{:02d}".format(y,m,d,i+1,mi,s))
                    i += 1
                    amount_of_ones += 1
                else:
                    i += 1
                    amount_of_ones += 1
            
            if i == 23:
                if on_off_list[i] == 1:
                    if on_off_list[i-1] == 0:
                        time_list[index].append("{:4d}-{:02d}-{:02d} {:02}:{:02d}:{:02d}".format(y,m,d,i+1,mi,s))
                        time_list[index].append("{:4d}-{:02d}-{:02d} {:02}:{:02d}:{:02d}".format(y,m,d,23,59,59))
                        i += 1
                    else:
                        time_list[index].append("{:4d}-{:02d}-{:02d} {:02}:{:02d}:{:02d}".format(y,m,d,23,59,59))
                        i += 1

                else:
                    i += 1
    
            elif on_off_list[i] == 1:
                if on_off_list[i-1] == 0:
                    if amount_of_ones != 0:
                        time_list[index].append("{:4d}-{:02d}-{:02d} {:02}:{:02d}:{:02d}".format(y,m,d,i+1,mi,s))
                        i += 1
                        amount_of_ones += 1
                    else:
                        i += 1
                
                else:
                    i += 1
                
            else:
                if on_off_list[i-1] == 1:
                    time_list[index].append("{:4d}-{:02d}-{:02d} {:02}:{:02d}:{:02d}".format(y,m,d,i+1,mi,s))
                    if index < amount:
                        index += 1
                        i += 1
                    else:
                         i += 1
                    

                else:
                    i += 1
        
        except IndexError:
            if on_off_list[i] == 1:
                if index < amount:
                    time_list[index].append("{:4d}-{:02d}-{:02d} {:02}:{:02d}:{:02d}".format(y,m,d,i,mi,s))
                    amount_of_ones += 1
                    i += 1
                else:
                    i += 1
            else:
                i += 1
    print("Running times:")
    print(time_list)
    data = importJSON("tasklists/tasklist.json")
    downloader_time = data["downloader_time"]
    running_times = {"running_times": time_list, "downloader_time": downloader_time}
    writeJSON("tasklists/tasklist.json",running_times)
    


def main(d,m,y,temp_in,Tfav,Tmin,Tmax):
    data, slopelist = derivatives(d, m, y)
    average = price_average(data)
    on_off_list = compare_prices(data, slopelist, average,temp_in,Tfav,Tmin,Tmax)
    mode_list(on_off_list,y,m,d)
