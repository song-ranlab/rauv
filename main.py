#!/usr/bin/env python

# Objective: create a script that the vehicle executes once powered on. In remote control mode,
# the script reads in commands from remote controller and sends corresponding commands to the
# motors. This script also coordinates all the functions that govern each sensor, communication
# module, etc. In autonomy mode, this script triggers the autonomy sub function, which takes inputs
# from relevant sensors, makes logic decisions based on sensor data, and sends commands to the
# motor. The script determines when to start and terminate the autonomy function. The script links
# all of the sub-functions from our software architecture and behaves as an entrance to the system
# logic.

# CURRENT QUESTIONS:
# 1. Do ALL of the executable .py files derive from this? Or do some run in parallel?
# 		yes, this is the only code on this top-level
# 2. Doesn't QGroundControl take care of sending corresponding commands from controller to motors?
# 3. Is it better to have two distinct while loops for modes rc and auto, or better to have it nested? or other?
# 		auto is nested inside rc
# 4. What would it look like to have sensor input in the autonomy mode section of the code?

# modes: remote_control (rc) and autonomous (auto)

# sensors: camera_F (front), camera_B (bottom), depth, temp_cpv (custom pressure vessel),
		 # temp_pv (cylindrical pv), leak_cpv, leak_pv, kill_switch, sonar

# actuators: arm, thruster(0 thru 7) (map to locations (ie. front-left) to avoid confusion)

#---------------------------------------------------------------------------
#                        Beginning of Code
#---------------------------------------------------------------------------

# import all required files
import file_1 file_2 ... file_n

# Initiate nodes? (sensors, control, etc.)
roslaunch node_1 node_2 ... node_n

# See if the auv mode is rc or auto
mode = check_mode(self)

# Initialize time
startTime = time.initialize()

# Set debug = False initially (flags true if problem encountered)
debug = false  

# Set some convenient thruster configurations
surge() = thruster(0,1,2,3)
heave() = thruster(4,5,6,7)
yaw() = thruster(0,1,2,3)
sway() = thruster(0,1,2,3)
pitch = thruster(4,5,6,7)

# ---------------- INITIALIZATION -----------------------#

# Initialize logging
dataLogger = DataLogger.InitializeLogging(startTime)
systemLogger = logging.getLogger("systemLogger")

# Initialize sensors / actuators for initial diagnostics check
initialize() # reads data from sensors, spins/reads data from thrusters

# make sure the vehicle is operating
while auv == running(in water, powered on, != shutdown):

	mode = check_mode(self)
# -------------- REMOTE CONTROL MODE --------------------#

	while mode == rc:

		#take command from joystick and pass it to thrusters
		command() = joystick.input() (array of xyz translation and rotation?)
		control_thrusters() = command

		# check to make sure still in rc mode and running
		if check_mode(self) == auto && running():
			
			#----------------    AUTONOMY MODE    ------------------#

			# NEED TO ADD CODE THAT READS VEHICLE POSITION AND ORIENTATION

			# sample autonomy code aimed at driving the auv around the perimeter of an imaginary square.
			while mode == auto:

			
				# Begin legs of path
				for i in range(4): # 4 sides in a square

					while clear_path() # performs movement if it won't collide 
					
						# Drive forward (figure out how to add duration -- add while time < xx)
						surge[200,200,200,200] (assumes -500 == full reverse, 0 == stopped, 500 == full ahead) 							

						# Turn right 90 degrees
						yaw[100, 100, -100, -100] (arbitrary signs, don't know how it will be yet)
					

						mode == check_mode(self)	
			

