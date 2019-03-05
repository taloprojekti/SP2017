# Setup-tiedosto

##### MAIN SWITCH ##### 
def Main_switch():
    return int(0) # Return 0 for testing and 1 for operational use

##### HW SETTINGS #####
def Rele_pin():
    return int(29) # Board-pinnijaon mukainen GPIO-pinni, johon lämmittimen rele on kytketty.
    
##### LÄMPÖTILA-ASETUKSET #####
def Tmin():
    return int(19) # Minimilämpötila, johon rakennuksen sisälämmön annetaan laskea.

def Tmax():
    return int(23) # Maksimilämpötila, johon rakennuksen sisälämmön annetaan nousta.

def Tfav():
    return int(27) # Suosikkilämpötila, johon rakennuksen sisälämpö asetetaan, kun päivän sähkönhinnat ovat tasaiset.
    
##### PID-TUNING #####    
def Pgain():
    return float(1.0)
    
def Igain():
    return float(0.1)
    
def Dgain():
    return float(0.0)
    
def Imax():
    return float(3.0)
    
def Imin():
    return float(3.0)
    
##### RELEEN DEADBAND-ASETUKSET #####
def DBmin():
    return 0.0
    
def DBmax():
    return 0.5
