# 1. Append Size
# For the first code challenge, we are going to calculate the length of a list and then append the value to the end of the list. Here is what we need to do:

# Define the function to accept one parameter for our list
# Get the length of the list
# Append the length of the list to the end of the list
# Return the modified list

# Write your function here
def append_size(lst):
    lst.append(len(lst))
    return lst


# Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

# 2. Append Sum
# Let’s create a function that calculates the sum of the last two elements of a list and appends it to the end. After doing so, it will repeat this process two more times and return the resulting list. You can choose to use a loop or manually use three lines. Here are the steps we need:

# Define the function to accept one parameter for our list of numbers
# Add the last and second to last elements from our list together
# Append the calculated value to the end of our list.
# Repeat steps 2 and 3 two more times
# Return the modified list

#Write your function here
def append_sum(lst):
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  lst.append(lst[-1] + lst[-2])
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))