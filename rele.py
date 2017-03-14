import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

def virta_on(rele_pin):
	GPIO.setup(rele_pin, GPIO.OUT)
	GPIO.output(rele_pin, GPIO.HIGH)
	
def virta_off(rele_pin):
	GPIO.output(rele_pin, GPIO.LOW)
	
def cleanup():
	GPIO.cleanaup()
	
def switch(mode, PID, temp_req, temp_now, deadband_max, deadband_min, rele_pin)
	if mode == "active":
		if temp_req > temp_now:
			virta_on(rele_pin)
		else:
			virta_off(rele_pin)
			
	elif mode == "PIDctrl":
		if PID > deadband_max:
			virta_on(rele_pin)
		if PID < deadband:
			virta_off(rele_pin)