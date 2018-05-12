print "Booting python script..."

import RPi.GPIO as GPIO
import time
import datetime

from firebase import firebase
from config import *

# Util functions
current_milli_time = lambda: int(round(time.time() * 1000))

class Device():

    def __init__(self, name=None, pin=None, machinetype=None, paymenttype=None):
        self.pin = pin
        self.state = LIGHT_OFF
        self.machinetype = machinetype
        self.paymenttype = paymenttype
        self.name = name

        # These two vars measure the number of times an ON or OFF was detected in the last ON_OFF_COUNT_INTERVAL_SEC
        self.num_on = 0
        self.num_off = 0

    def callback(self, pin):
        # For some reason, adding a sleep causes the reading to be more reliable
        time.sleep(0.01)

        # Get and invert reading
        reading = 1 - GPIO.input(self.pin)
        if reading == LIGHT_ON:
            self.num_on += 1
        else:
            self.num_off += 1
        
        print str(self)

    def compute_and_reset_state(self):
        reading = 1 - GPIO.input(self.pin)

        # PROBLEM: doesn't update unless rising / falling edge, and if no change but not detected first time
        if self.num_on > ON_OFF_COUNT_BLINK_THRESHOLD and self.num_off > ON_OFF_COUNT_BLINK_THRESHOLD:
            self.state = LIGHT_BLINKING
        else:

            self.state = reading
        # Output to test LED if the correct pin is activated 
        if self.pin == TEST_GPIO_PIN:
            print "Setting GPIO output to " + str(reading)
            GPIO.output(LED_PIN, self.state)

        # Reset on/off count
        self.num_on = 0
        self.num_off = 0
        return self.state

        
    def __str__(self):
        return "Device: name - " + str(self.name) + ", pin - " + str(self.pin) + ", state - " + str(self.state) + " - num_on: " + str(self.num_on) + " num_off: " + str(self.num_off)
    
    def get_status_string(self):
        status_string = "unknown"
        if self.state == LIGHT_BLINKING:
            status_string = "blinking"
        elif self.state == LIGHT_OFF:
            status_string = "off"
        else:
            status_string = "on"
        return status_string



def setup_devices_gpio(devices):
    # Use BCM Mode
    GPIO.setmode(GPIO.BCM)

    # Set all relevant pins as input, pull down to 0V to have standard washing machine status as off
    # Note for the button case - this has to be PUD_UP
    for device in devices:
        GPIO.setup(device.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(device.pin, GPIO.BOTH, callback=device.callback, bouncetime=BOUNCETIME) 

    GPIO.setup(LED_PIN, GPIO.OUT)

def exception_handler(request, exception):
    print "For request: " + str(request) + " got exception: " + str(exception)


def response_callback(response):
    print response

if __name__ == "__main__":
    print "Initializing Firebase connection"
    # Open up network conn to Firebase
    firebase = firebase.FirebaseApplication('https://tlaundry2.firebaseio.com', None)
    print "Firebase connection set up."

    print "Starting async firebase get"

    # Initialize washers and dryers
    DEVICES = [Device(**washer) for washer in WASHERS]
    DEVICES += [Device(**dryer) for dryer in DRYERS]

    setup_devices_gpio(DEVICES)

    # Begin main timer loop
    while True:
        # Sleep until we want to check the current washer state
        time.sleep(ON_OFF_COUNT_INTERVAL_SEC)
        # Go through all the washers and check the state
        current_state = {}
        current_state["timestamp"] = datetime.datetime.now().isoformat()
        for device in DEVICES:
            device_state = device.compute_and_reset_state()
            current_state[str(device.name)] =  device.get_status_string()

        print str(current_state)

        result = firebase.put_async('/', FLOOR_NUMBER, current_state, callback=response_callback)


