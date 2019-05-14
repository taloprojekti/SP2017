import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

def virta_on(rele_pin):
    GPIO.output(rele_pin, GPIO.HIGH)
    
def virta_off(rele_pin):
    GPIO.output(rele_pin, GPIO.LOW)
    
def cleanup(rele_pin):
    GPIO.setup(rele_pin, GPIO.OUT)
    GPIO.output(rele_pin, GPIO.LOW)
    GPIO.cleanup()
    
def switch(mode, PID, temp_req, temp_now, deadband_max, deadband_min, rele_pin):
    GPIO.setup(rele_pin, GPIO.OUT)
    print(mode)
    #if heater is in energy saving mode
    if mode == 1:
            virta_on(rele_pin)
            return "on"
    else:
        virta_off(rele_pin)
        return "off"
    #if heater is turned on
    """elif mode == "PIDctrl":
        if PID > deadband_max:
            virta_on(rele_pin)
            return "on"
        elif PID < deadband_min:
            virta_off(rele_pin)
            return 1"""
