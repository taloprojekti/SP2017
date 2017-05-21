import RPi.GPIO as GPIO

def virta_on(rele_pin):
	GPIO.output(rele_pin, GPIO.HIGH)
	
def virta_off(rele_pin):
	GPIO.output(rele_pin, GPIO.LOW)
	
def cleanup(rele_pin):
	GPIO.output(rele_pin, GPIO.LOW)
	GPIO.cleanup()
	
def switch(mode, PID, temp_req, temp_now, deadband_max, deadband_min, rele_pin):
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(rele_pin, GPIO.OUT)
	if mode == "active":
		if temp_req > temp_now:
			virta_on(rele_pin)
			return "on"
		else:
			virta_off(rele_pin)
			return "off"
			
	elif mode == "PIDctrl":
		if PID > deadband_max:
			virta_on(rele_pin)
			return "on"
		elif PID < deadband_min:
			virta_off(rele_pin)
			return "off"
