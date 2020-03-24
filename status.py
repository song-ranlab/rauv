#!/usr/bin/env python

# Objective: Code that acts as the intitialization and diagnostics check for the vehicle. 
# Diagnostic errors will be coded as follows:
# 'k' = killswitch
# 'l' = leak sensor 
# 't' = temp/humid sensor 
# 'r' = thrusters
# 'd' = depth sensor
# 'c' = camera 
# 'p' = processor
# 'b' = battery

import rospy

def initialize(debug): #debug should be set to False initially and will be updated to the above letters upon encountering errors
	# I'm sure there's 100 better ways to write this out
	
	# Run kill switch initialization
	killswitch = check.killswitch()
	if killswitch == False:
		if debug == False:
			debug = 'k'
		else:
			debug += 'k'
	
	# Run leak sensor initialization
	if leak_sensor == False:
		if debug == False:
			debug = 'l'
		else:
			debug += 'l'
	
	# Run temp/humidity initialization
	if temp_humidity == false:
		if debug == False:
			debug = 't'
		else debug += 't'
	
	# Run thruster initialization
	if thrusters == False:
		if debug == False:
			debug = 'r'
		else:
			debug += 'r'
			
	#Run depth sensor initialization
	if depth_sensor == False:
		if debug == False:
			debug = 'd'
		else:
			debug += 'd'
	#Run camera initialization
	if camera == False:
		if debug == False:
			debug = 'c'
		else:
			debug += 'c'

	#Run processor initialization
	if processor == False:
		if debug == False:
			debug = 'p'
		else:
			debug += 'p'

	#Run battery initialization
	if battery == False:
		if debug == False:
			debug = 'b'
		else:
			debug += 'b'
			
	return debug
	
# Define function that indicates that the AUV is underwater, initialized, and no killswitch
def running(debug):
	
	if depth.reading > nominal air pressure:
		if debug == False:
			return True
	else:
		return False

# Define function that checks whether the vehicle is in rc or auto mode
def check_mode():
	if joystick signal received:
		return rc
	else
		return auto
