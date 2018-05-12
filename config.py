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
        {	"pin":18, "name":"WASHER_A", "machinetype": WASHER, "paymenttype":PAY_EZLINK	},
	{	"pin":23, "name":"WASHER_B", "machinetype": WASHER, "paymenttype":PAY_EZLINK	},
	{	"pin":24, "name":"WASHER_C", "machinetype": WASHER, "paymenttype":PAY_EZLINK	},
	{	"pin":25, "name":"WASHER_D", "machinetype": WASHER, "paymenttype":PAY_COIN	},
	{	"pin":8,  "name":"WASHER_E", "machinetype": WASHER, "paymenttype":PAY_COIN	},
]

DRYERS = [
        {	"pin":18, "name":"DRYER_A", "machinetype": WASHER, "paymenttype": PAY_EZLINK	},
	{	"pin":23, "name":"DRYER_B", "machinetype": WASHER, "paymenttype": PAY_EZLINK	},
	{	"pin":24, "name":"DRYER_C", "machinetype": WASHER, "paymenttype": PAY_COIN		},
	{	"pin":25, "name":"DRYER_D", "machinetype": WASHER, "paymenttype": PAY_COIN		},
]
