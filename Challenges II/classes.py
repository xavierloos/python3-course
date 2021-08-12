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
