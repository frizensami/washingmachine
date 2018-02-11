# The Tembusu Washing Machine Project
This project aims to detect the current running state of all washing machines and dryers in Tembusu College. The information can then be passed to users through a Telegram bot / mobile website.

This repository has -x- sections.
1. `detect.py` - Python script running on a Raspberry Pi that checks the curent state of all op-amps sending digital signals to its GPIO pins.


## detect.py
`detect.py` runs on the Raspberry Pi at startup. It runs forever, and continually checks the state of the LDRs connected to the washing machines / dryer plugged into the Pi's GPIO pins. 
