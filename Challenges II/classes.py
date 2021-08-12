# 1. Setting Up Our Robot
# Let’s begin by creating the class for our robot. We will begin by setting up the instance variables to keep track of important data related to the robot. Here are the steps we need to do:
# Create a new class called DriveBot
# Set up a basic constructor (no parameters needed)
# Initialize three instance variables within our constructor which all default to 0: motor_speed, direction, and sensor_range

class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0


robot_1 = DriveBot()
robot_1.motor_speed = 5
robot_1.direction = 90
robot_1.sensor_range = 10

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)


# 2. Adding Robot Logic
# Now we want to add some logic to our robot. It would be very useful to be able to control our robot, se we are going to create a control_bot method which changes the speed and direction. We are also going to create a method called adjust_sensor. This method is used to change the range of our robot’s sensors which are used to detect obstacles. Here are the steps:
# Define a function within the DriveBot class which accepts two additional parameters: one for a new speed and one for a new direction
# Replace the instance variables for speed and direction with the input parameters
# Define another function called adjust_sensor which accepts one additional parameter
# Replace the instance variable sensor_range with the input parameter

class DriveBot:
    def __init__(self):
        self.motor_speed = 0
        self.direction = 0
        self.sensor_range = 0

    def control_bot(self, new_speed, new_direction):
        self.motor_speed = new_speed
        self.direction = new_direction

    def adjust_sensor(self, new_sensor_range):
        self.sensor_range = new_sensor_range


robot_1 = DriveBot()
robot_1.control_bot(10, 180)
robot_1.adjust_sensor(20)

print(robot_1.motor_speed)
print(robot_1.direction)
print(robot_1.sensor_range)
