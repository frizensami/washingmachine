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
TEST_GPIO_PIN = 18
LED_PIN = 12

# Debouncing time
BOUNCETIME = 50

# Floor number for installed pi
FLOOR_NUMBER = "9"

WASHERS = [
        {	"pin":21, "name":"WASHER A", "machinetype": WASHER, "paymenttype":PAY_EZLINK	},
	{	"pin":20, "name":"WASHER B", "machinetype": WASHER, "paymenttype":PAY_EZLINK	},
	{	"pin":16, "name":"WASHER C", "machinetype": WASHER, "paymenttype":PAY_EZLINK	},
	{	"pin":12, "name":"WASHER D", "machinetype": WASHER, "paymenttype":PAY_COIN	},
	{	"pin":7,  "name":"WASHER E", "machinetype": WASHER, "paymenttype":PAY_COIN	},
]

DRYERS = [
        {	"pin":25, "name":"DRYER A", "machinetype": DRYER, "paymenttype": PAY_EZLINK	},
	{	"pin":24, "name":"DRYER B", "machinetype": DRYER, "paymenttype": PAY_EZLINK	},
	{	"pin":23, "name":"DRYER C", "machinetype": DRYER, "paymenttype": PAY_COIN	},
	{	"pin":18, "name":"DRYER D", "machinetype": DRYER, "paymenttype": PAY_COIN	},
]
