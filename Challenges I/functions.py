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

# 4. Average
# Let’s create a function which takes the average of two numbers. These two numbers will be the input of the function and the output will be the average of the two. In order to do this, we need to do a few steps:

# Define the function with two input parameters, num1 and num2
# Calculate the sum of the two numbers
# Divide the sum by the number of inputs to the function
# Return the answer

# Write your average function here:


def average(num1, num2):
    return (num1 + num2) / 2


# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0

# 5. Remainder
# For the final challenge in this group, we are going to take the remainder of two numbers while performing other mathematical operations on them. We are going to multiply the numerator by 2 and divide the denominator by 2. After the two values have been modified, we will divide them and return the remainder. In order to do this we will need to:

# Define the function to accept two parameters
# Multiply the first input value by 2
# Divide the second input value by 2
# Calculate the remainder of the modified first input value divided by the modified second input value (using modulus)
# Return the answer

# Write your remainder function here:


def remainder(num1, num2):
    return (num1 + num1) % (num2 / 2)


# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0

# FUNCTIONS ADVANCED
# 1. First Three Multiples
# Let’s start by creating a function which both prints and returns values. For this function, we are going to print out the first three multiples of a number and return the third multiple. This means that we are going to print 1, 2, and 3 times the input number and then return the value of 3 times the input number. For this, we are going to need a few steps:

# Define the function header to accept one input parameter called num
# Print out 1 times num
# Print out 2 times num
# Print out 3 times num
# Return the value of 3 times num

# Write your first_three_multiples function here


def first_three_multiples(num):
    print(num)
    print(num * 2)
    print(num * 3)
    return num * 3


# Uncomment these function calls to test your first_three_multiples function:
first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0

# 2. Tip
# Let’s say we are going to a restaurant and we decide to leave a tip. We can create a function to easily calculate the amount to tip based on the total cost of the food and a percentage. This function will accept both of those values as inputs and return the amount of money to tip. In order to do this, we will need a few steps:

# Define the function to accept the total cost of the food called total and the percentage to tip as percentage
# Calculate the tip amount by multiplying the total and percentage and dividing by 100
# Return the tip amount

# Write your tip function here:


def tip(total, percentage):
    return (total * percentage) / 100


# Uncomment these function calls to test your tip function:
print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0
