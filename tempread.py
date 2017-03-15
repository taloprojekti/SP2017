#read_temp() palauttaa hetkellisen lämpötila-arvon celsiuksina.
#Huom! OneWire support lisättävä Raspiin.
#Ohjeet sivulla:
#https://cdn-learn.adafruit.com/downloads/pdf/adafruits-raspberry-pi-lesson-11-ds18b20-temperature-sensing.pdf

import os
import glob
import time

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

device_folder2 = glob.glob(base_dir + '22*')[0]
device_file2 = device_folder2 + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp_raw2():
    f = open(device_file2, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp_out():
    lines = read_temp_raw2()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c


def read_temp_in():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c

def write_temp(pvm): #tallentaa lämpötilatiedot tiedoston uudelle riville
    tiedosto = open("tiloja.txt", "a")
    temp = read_temp_in() #tallentaa lämpötilan ja päivämäärän erotettuna puolipisteellä
    temp2 = read_temp_out()
    tiedosto.write("{:.2f};{:.2f};{}\n".format(temp,temp2,pvm))
    tiedosto.close()

# osio jonka avulla voi testata lämpötilamittarin toimivuutta
def main():
    while True:
        print(read_temp_in())
        print (read_temp_out())
        time.sleep(1)
