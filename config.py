# CHANGE THIS FILE TO REFLECT YOUR SETUP

### Constants
LIGHT_OFF = 0
LIGHT_ON = 1
LIGHT_BLINKING = 2

WASHER = 100
DRYER = 101

PAY_EZLINK = 200
PAY_COIN = 201

# Number of seconds to count on/off cycles for to check for blinking
ON_OFF_COUNT_INTERVAL_SEC = 6
ON_OFF_COUNT_BLINK_THRESHOLD = 2

# Which pin will be used to control the test LED (during debugging)
#TEST_GPIO_PIN = 18
#LED_PIN = 12

# Debouncing time
BOUNCETIME = 50

# Floor number for installed pi
FLOOR_NUMBER = "9"

WASHERS = [
        {	"pin":21, "name":"WASHER A (EZLINK)", "machinetype": WASHER, "paymenttype":PAY_EZLINK	},
	{	"pin":20, "name":"WASHER B (EZLINK)", "machinetype": WASHER, "paymenttype":PAY_EZLINK	},
	{	"pin":16, "name":"WASHER C (EZLINK)", "machinetype": WASHER, "paymenttype":PAY_EZLINK	},
	{	"pin":12, "name":"WASHER D (COIN)", "machinetype": WASHER, "paymenttype":PAY_COIN	},
	{	"pin":7,  "name":"WASHER E (COIN)", "machinetype": WASHER, "paymenttype":PAY_COIN	},
]

DRYERS = [
        {	"pin":25, "name":"DRYER A (EZLINK)", "machinetype": DRYER, "paymenttype": PAY_EZLINK	},
	{	"pin":24, "name":"DRYER B (EZLINK)", "machinetype": DRYER, "paymenttype": PAY_EZLINK	},
	{	"pin":23, "name":"DRYER C (COIN)", "machinetype": DRYER, "paymenttype": PAY_COIN	},
	{	"pin":18, "name":"DRYER D (COIN)", "machinetype": DRYER, "paymenttype": PAY_COIN	},
]
