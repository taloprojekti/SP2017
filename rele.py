import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

while True:
	comm = input("syota komento\n")
	if comm != "stop":
		GPIO.output(rele_pin, GPIO.HIGH)
	else:
		print("keskeytetty")
		break

GPIO.output(rele_pin, GPIO.LOW)