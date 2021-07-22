# 1. Large Power
# For the first code challenge, we are going to create a method that tests whether the result of taking the power of one number to another number provides an answer which is greater than 5000. We will use a conditional statement to return True if the result is greater than 5000 or return False if it is not. In order to accomplish this, we will need the following steps:

# Define the function to accept two input parameters called base and exponent
# Calculate the result of base to the power of exponent
# Use an if statement to test if the result is greater than 5000. If it is then return True. Otherwise, return False

# Write your large_power function here:
def large_power(base,exponent):
  if (base ** exponent) > 5000:
    return True
  else:
    return False
# Uncomment these function calls to test your large_power function:
print(large_power(2, 13))
# should print True
print(large_power(2, 12))
# should print False

# 2. Over Budget
# Let’s say we are trying to save some money and we are watching our budget. We need to make sure that the result of our spending is less than the total amount we have allocated for each of the categories. Our function will accept a parameter called budget which describes our spending limit. The next four parameters describe what we are spending our money on. We need to sum all of our spendings and compare it to the budget. If we have gone over budget, we will return True. Otherwise we return False. Here are the steps we need:

# Define the function to accept five parameters starting with budget then food_bill, electricity_bill, internet_bill, and rent
# Calculate the sum of the last four parameters
# Use if and else statements to test if the budget is less than the sum of the calculated sum from the previous step.
# If the condition is true, return True otherwise return False

# Write your over_budget function here:
def over_budget( budget, food_bill, electricity_bill, internet_bill,  rent):
  sum = food_bill + electricity_bill + internet_bill +  rent
  if budget < sum:
    return True
  else:
    return False
# Uncomment these function calls to test your over_budget function:
print(over_budget(100, 20, 30, 10, 40))
# should print False
print(over_budget(80, 20, 30, 10, 30))
# should print True

# 3. Twice As Large
# In this challenge, we will determine if one number is twice as large as another number. To do this, we will compare the first number with two times the second number. Here are the steps:

# Define our function with two inputs num1 and num2
# Multiply the second input by 2
# Use an if statement to compare the result of the last calculation with the first input
# If num1 is greater then return True otherwise return False

# Write your twice_as_large function here:
def twice_as_large(num1, num2):
  if num1 > (num2 * 2):
    return True
  else:
    return False
# Uncomment these function calls to test your twice_as_large function:
print(twice_as_large(10, 5))
# should print False
print(twice_as_large(11, 5))
# should print True

# 4. Divisible By Ten
# To make things a bit more challenging, we are going to create a function that determines whether or not a number is divisible by ten. A number is divisible by ten if the remainder of the number divided by 10 is 0. Using this, we can complete this function in a few steps:

# Define the function header to accept one input num
# Calculate the remainder of the input divided by 10 (use modulus)
# Use an if statement to check if the remainder was 0. If the remainder was 0, return True, otherwise, return False

# Write your divisible_by_ten() function here:
def divisible_by_ten(num):
  if num % 10 == 0:
    return True
  else:
    return False

# Uncomment these print() function calls to test your divisible_by_ten() function:

print(divisible_by_ten(20))
# should print True
print(divisible_by_ten(25))
# should print False

# 5. Not Sum To Ten
# Finally, we are going to check if the summation of two inputs does not equal ten. Our function will accept two inputs and add them together. If the two numbers added together are not equal to ten, then we will return True, otherwise, we will return False. Here is what we need to do:

# Define the function to accept two parameters, num1 and num2
# Add the two parameters together
# Test if the result is not equal to 10
# If the sum is not equal, return True, otherwise, return False

# Write your not_sum_to_ten function here:
def not_sum_to_ten(num1, num2):
  if(num1 + num2) == 10:
    return False
  else:
    return True
# Uncomment these function calls to test your not_sum_to_ten function:
print(not_sum_to_ten(9, -1))
# should print True
print(not_sum_to_ten(9, 1))
# should print False
print(not_sum_to_ten(5,5))
# should print False


# CONTROL FLOW ADVANCED

# 1. In Range
# Let’s start the advanced challenge problems by testing if a number falls within a certain range. We will accept three parameters where the first parameter is the number we are testing, the second parameter is the lower bound and the third parameter is the upper bound of our range. These are the steps required:

# Define the function to accept three numbers as parameters
# Test if the number is greater than or equal to the lower bound and less than or equal to the upper bound
# If this is true, return True, otherwise, return False

# Write your in_range function here:
def in_range(num, lower, upper):
  if num >= lower and num <= upper:
    return True
  else:
    return False
# Uncomment these function calls to test your in_range function:
print(in_range(10, 10, 10))
# should print True
print(in_range(5, 10, 20))
# should print False

# 2. Same Name
# We need to write a program that checks different names and determines if they are equal. We need to accept two strings and compare them. Here are the steps:

# Define the function to accept two strings, your_name and my_name
# Test if the two strings are equal
# Return True if they are equal, otherwise return False

# Write your same_name function here:
def same_name(your_name, my_name):
  if your_name == my_name :
    return True
  else:
    return False 
# Uncomment these function calls to test your same_name function:
print(same_name("Colby", "Colby"))
# should print True
print(same_name("Tina", "Amber"))
# should print False

# 3. Always False
# There are some situations that you normally want to avoid when programming using conditional statements. One example is a contradiction. This occurs when your condition will always be false no matter what value you pass into it. Let’s create an example of a function that contains a contradiction. It will contain a few steps:

# Define the function to accept a single parameter called num
# Use a combination of <, > and and to create a contradiction in an if statement.
# If the condition is true, return True, otherwise return False. The trick here is that because we’ve written a contradiction, the condition should never be true, so we should expect to always return False.

# Write your always_false function here:
def always_false(num):
  if num >= num or num <=num:
    return False
# Uncomment these function calls to test your always_false function:
print(always_false(0))
# should print False
print(always_false(-1))
# should print False
print(always_false(1))
# should print False

# 4. Movie Review
# We want to create a function that will help us rate movies. Our function will split the ratings into different ranges and tell the user how the movie was based on the movie’s rating. Here are the steps needed:

# Define our function to accept a single number called rating
# If the rating is equal to or less than 5, return "Avoid at all costs!"
# If the rating was less than 9, return "This one was fun."
# If neither of the if statement conditions were met, return "Outstanding!"

# Write your movie_review function here:
def  movie_review(rating):
  if rating <= 5:
    return "Avoid at all costs!"
  elif rating > 5 and rating < 9:
    return "This one was fun."
  else:
    return "Outstanding!"

# Uncomment these function calls to test your movie_review function:
print(movie_review(9))
# should print "Outstanding!"
print(movie_review(4))
# should print "Avoid at all costs!"
print(movie_review(6))
# should print "This one was fun."