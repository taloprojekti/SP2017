import json
import jsonhandler
import os


def create_folder(filedir):
    """Creates data-folder for credentials.json and setup.json"""
    path = os.getcwd() #detect the current working directory and print it
    path = str(path) + filedir
    try:
        os.mkdir(path)
        print ("Successfully created the directory", filedir)
   
    except FileExistsError:
            print ("Directory", filedir, "already exists")

def create_tauhka():
    from jsonhandler import writeJSON
    data = {}
    data["running_times"] = ""
    data["downloader_time"] = ""
    writeJSON("tasklists/tasklist.json", data)

def check_credentials():
    """Creates credentials json-file at the beginning"""
    username = str(input("Enter username: ")) #username and password are needed for FTP-server
    password = str(input("Enter password: "))
    data = {"username":username,"password":password}
    try:
        with open("data/credentials.json", "x") as outfile:
            json.dump(data,outfile)
            return 1
    except FileExistsError:
        return 0

def create_tasklist():
    try:
        file = open("tasklists/tasklist.json", "x")
        file.close()
        return 1
    except FileExistsError:
        return 0


def check_setup():
    """Creates setup settings json-file at the beginning"""
    main_switch = int(input("Enter 0 if testing, enter 1 if operating: "))
    while True:
        if main_switch == 0 or main_switch == 1:
            break
        else:
            main_switch = int(input("Enter 0 if testing, enter 1 if operating: "))
    while True:

        TMin = int(input("Enter minimum allowable temperature: "))
        TMax = int(input("Enter maximum allowable temperature: "))
        if TMax < TMin:
            print("Maximum temperature must be bigger value than minimum temperature")
        else:
            break
    while True:
    
        TFav = int(input("Enter favourite temperature: "))
        if TFav <= TMax and TFav >= TMin:
            break
        else:
            print("Favourite temperature must be between minimum and maximum temperature")

    Hardware_settings = int(input("Enter relays GPIO-pin. GPIO-pin must be one of the following: (7,11,13,15,16,18,22,29,31,32,33,35,36,37,38,40) "))
    input_list = [7,11,13,15,16,18,22,29,31,32,33,35,36,37,38,40]
    while Hardware_settings not in input_list:

        Hardware_settings = int(input("Enter relay's GPIO-pin. GPIO-pin must be one of the following: (7,11,13,15,16,18,22,29,31,32,33,35,36,37,38,40) "))
    input_list.remove(Hardware_settings)

    setup_settings = {"main_switch":main_switch,"temperatures":{"Tmax":TMax,"Tmin":TMin,"Tfav":TFav},"pid-tuning":{"Pgain":1.0,"Igain":0.1,"Dgain":0.0,"Imax":3.0,"Imin":3.0},"relay_settings":{"DBmin":0.0,"DBmax":0.5},"hardware_settings":{"Rele_pin":Hardware_settings},"Temperature_sensor":{"Temp_pin":7}}

    try:
        with open("data/setup.json", "x") as outfile:
            json.dump(setup_settings,outfile)
            return 1
    except FileExistsError:
        return 0
 
def main():
   
    create_folder("/data")
    create_folder("/tasklists")
    if create_tasklist() == 0:
        pass
    
    else:
        print("File 'tasklist.json' created and added to directory 'tasklists'")

    if check_setup() == 0:
        print("The file 'tasklist.json' already exists")
        pass

    else:
        print("File 'setup.json' created and added to directory 'data'")

    if check_credentials() == 0:
        print("The file 'check_credentials' already exists")
        pass
    
    else:
        print("File 'credentials.json' created and added to directory 'data'")
    create_tauhka()

main()
