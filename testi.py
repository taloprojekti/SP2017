import serial
ser = serial.Serial('/dev/ttyACM0', 9600)
i=0

while(1):

    response1 = ser.readline().strip().decode()
    response2 = ser.readline().strip().decode()
    print(response1)
    print(response2)

    i+=1
