# 1. Tenth Power
# Let’s create some functions which can help us solve math problems! For this first function, we are going to take the tenth power of a number. In order to do this we need to do three things:

# Set up the function header for tenth_power which accepts one parameter
# Take the tenth power of the input value
# Return the result
# Write your tenth_power function here:
def tenth_power(num):
    return num ** 10


# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024

# 2. Square Root
# Another useful function for solving math problems is the square root function. We can create this using similar steps from the last problem. The code will look very similar. We need to:

# Set up the function header for square_root which accepts one parameter
# Take the square root of the input value
# Return the result

# Write your square_root function here:


def square_root(num):
    return num ** 0.5


# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10

# 3. Win Percentage
# Next, we will create a function which calculates the percentage of games won. In order to do this, we will need to know how many total games there were and divide the number of wins by the total number of games. For this function, there will be two input parameters, the number of wins and the number of losses. We also need to make sure that we return the result as a percentage (in the range of 0 to 100). In order to create this method we need the following steps:

# Define the function header with two parameters, wins and losses
# Calculate the total number of games using the number of wins and losses
# Get the ratio of winning using the number of wins out of the total number of games.
# Convert the ratio to a percentage
# Return the percentage

# Write your win_percentage function here:


def win_percentage(wins, losses):
    total = wins / (wins + losses)
    return total * 100


# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100
