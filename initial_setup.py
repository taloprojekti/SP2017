import json
import jsonhandler
def check_credentials():
    """Creates credentials json-file at the beginning"""
    username = str(input("Enter username: ")) #username and password are needed for FTP-server
    password = str(input("Enter password: "))
    data = {"username":username,"password":password}
    try:
        with open("tunnukset.json", "w") as outfile:
            json.dump(data,outfile)
            return 1
    except FileExistsError:
        return 0

def check_setup():
    """Creates setup settings json-file at the beginning"""
    main_switch = int(input("Enter 0 if testing, enter 1 if operating"))
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

    Hardware_settings = int(input("Enter relays GPIO-pin"))
    setup_settings = {"main_switch":main_switch,"temperatures":{"Tmax":TMax,"Tmin":TMin,"Tfav":TFav},"pid-tuning":{"Pgain":1.0,"Igain":0.1,"Dgain":0.0,"Imax":3.0,"Imin":3.0},"relay_settings":{"DBmin":0.0,"DBmax":0.5},"hardware_settings":{"Rele_pin":Hardware_settings}}
    try:
        with open("data/setup.json", "w") as outfile:
            json.dump(setup_settings,outfile)
            return 1
    except FileExistsError:
        return 0
 
def main():
    
    if check_setup() == 0:
        print("The file already exists")
        pass

    else:
        print("File created")

    if check_credentials() == 0:
        print("The file already exists")
        pass
    
    else:
        print("File created")


main()
