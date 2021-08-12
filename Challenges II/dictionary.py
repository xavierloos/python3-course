# 1. Sum Values
# For the first code challenge, we are going to look at only the values in a dictionary. This function should sum up all of the values from the key-value pairs in the dictionary. Here are the steps we need:
# Define the function to accept one parameter for our dictionary
# Create a variable to keep track of our sum
# Loop through every value in the dictionary
# Inside the loop, add each value to the sum
# Return the sum

def sum_values(my_dictionary):
    total = 0
    for key, value in my_dictionary.items():
        total += value
    return total


# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))
# should print 10
print(sum_values({10: 1, 100: 2, 1000: 3}))
# should print 6

# 2. Even Keys
# Next, we are going to do something similar, but we are going to use the keys in order to retrieve the values. Additionally, we are going to only look at every even key within the dictionary. Here are the steps:
# Define the function to accept one parameter for our dictionary
# Create a variable to keep track of our sum
# Loop through every key in the dictionary
# Inside the loop, if the key is even, add the value from the even key
# After the loop, return the sum


def sum_even_keys(my_dictionary):
    sum_key = 0
    for key in my_dictionary.keys():
        if key % 2 == 0:
            sum_key += my_dictionary[key]
    return sum_key


# Uncomment these function calls to test your  function:
print(sum_even_keys({1: 5, 2: 2, 3: 3}))
# should print 2
print(sum_even_keys({10: 1, 100: 2, 1000: 3}))
# should print 6
