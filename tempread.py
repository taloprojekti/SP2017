def read_temp():
	import serial
	ser = serial.Serial('/dev/ttyACM0', 9600)
	i=0
	while(i<5):
		response1 = ser.readline().strip().decode()
		response2 = ser.readline().strip().decode()
		i+=1
				
	print("temp_in: {}, temp_out: {}\n".format(response1,response2))
				
	return (response1,response2)

def jako(n):
        return float(read_temp()[n])

def read_temp_in():
        return jako(0)

def read_temp_out():
        return jako(1)

def write_temp(pvm): #tallentaa lämpötilatiedot tiedoston uudelle riville
    tiedosto = open("tiloja.csv", "a")
    temp = read_temp_in() #tallentaa lämpötilan ja päivämäärän erotettuna puolipisteellä
    temp2 = read_temp_out()
    tiedosto.write("{:.2f},{:.2f},{}\n".format(temp,temp2,pvm))

    tiedosto.close()
