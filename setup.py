import json

def read_setup():
    file = json.load(open("data/setup.json","r"))
    return file
def main_switch(data):
    """returns 0 for testing and 1 for operational use."""

    main_switch = int(data["main_switch"])

    return main_switch

def temperatures(data):

    Tfav = int(data["temperatures"]["Tfav"]) #Favourite temp, which is set, when electricity price is low  
    Tmin = int(data["temperatures"]["Tmin"]) #Minimum temp which is allowed in building
    Tmax = int(data["temperatures"]["Tmax"]) #Maximum temp which is allowed in building
    return Tfav, Tmin, Tmax

def pid_tuning(data):
    """gains for the pid-controller"""

    Pgain = float(data["pid-tuning"]["Pgain"])
    Igain = float(data["pid-tuning"]["Igain"])                               
    Dgain = float(data["pid-tuning"]["Dgain"])
    Imax = float(data["pid-tuning"]["Imax"])
    Imin = float(data["pid-tuning"]["Imin"])

    return Pgain, Igain, Dgain, Imax, Imin

def hardware_settings(data):
    """GPIO-pinn consistent of Board-pinn-distribution,which is connected by relay"""
    Rele_pin = int(data["hardware_settings"]["Rele_pin"])
    return Rele_pin

def relay_settings(data):

    DBmin = float(data["relay_settings"]["DBmin"])
    DBmax = float(data["relay_settings"]["DBmax"])
    return DBmin, DBmax


