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

# 3. Add Ten
# Let’s loop through the keys again, but this time let’s modify the values within the dictionary. Our function should add 10 to every value in the dictionary and return the modified dictionary. Here is what we need to do:
# Define the function to accept one parameter for our dictionary
# Loop through every key in the dictionary
# Retrieve the value using the key and add 10 to it. Make sure to re-save the new value to the original key.
# After the loop, return the modified dictionary


def add_ten(my_dictionary):
    for key in my_dictionary.keys():
        my_dictionary[key] += 10
    return my_dictionary


# Uncomment these function calls to test your  function:
print(add_ten({1: 5, 2: 2, 3: 3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10: 1, 100: 2, 1000: 3}))
# should print {10:11, 100:12, 1000:13}

# 4. Values That Are Keys
# We are making a program that will create a family tree. Using a dictionary, we want to return a list of all the children who are also parents of other children. Using dictionaries we can consider those people to be values which are also keys in our dictionary of family data. Here is what we need to do:
# Define the function to accept one parameter for our dictionary
# Create an empty list to hold the values we find
# Loop through every value in the dictionary
# Inside the loop, test if the current value is a key in the dictionary. If it is then append it to the list of values we found
# After the loop, return the list of values which are also keys


def values_that_are_keys(my_dictionary):
    value_keys = []
    for value in my_dictionary.values():
        if value in my_dictionary:
            value_keys.append(value)
    return value_keys


# Uncomment these function calls to test your  function:
print(values_that_are_keys({1: 100, 2: 1, 3: 4, 4: 10}))
# should print [1, 4]
print(values_that_are_keys({"a": "apple", "b": "a", "c": 100}))
# should print ["a"]

# 5. Largest Value
# For the last challenge, we are going to create a function that is able to find the maximum value in the dictionary and return the associated key. This is a twist on the max algorithm since it is using a dictionary rather than a list. These are the steps:
# Define the function to accept one parameter for our dictionary
# Initialize the starting key to a very low number
# Initialize the starting value to a very low number
# Iterate through the dictionary’s key/value pairs.
# Inside the loop, if the current value is larger than the current largest value, replace the largest key and largest value with the current ones you are looking at
# Once you are done iterating through all key/value pairs, return the key which has the largest value


def max_key(my_dictionary):
    largest_key = float("-inf")
    largest_value = float("-inf")
    for key, value in my_dictionary.items():
        if value > largest_value:
            largest_value = value
            largest_key = key
    return largest_key


# Uncomment these function calls to test your  function:
print(max_key({1: 100, 2: 1, 3: 4, 4: 10}))
# should print 1
print(max_key({"a": 100, "b": 10, "c": 1000}))
# should print "c"

# Dictionaries (Advanced)

# 1. Word Length Dict
# Let’s start by writing a function that creates a new dictionary based on a list of strings. The keys of our dictionary will be every string in our list of strings, while the values will be the length of each of the words in the string list. Here are the steps:
# Define the function to accept one parameter for our list of strings
# Create a new empty dictionary
# Loop through every string in the list of strings
# Inside the loop, add the string as a key and the length of the string as the value to the dictionary
# After the loop, return the new dictionary


def word_length_dictionary(words):
    word_lengths = {}
    for word in words:
        word_lengths[word] = len(word)
    return word_lengths


# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}

# 2. Frequency Count
# This next function is similar, but instead of counting the length of each string in the list of strings, we will be counting the frequency of each string. This function will also accept a list of strings as input and return a new dictionary. Here is what we need to do:
# Define the function to accept one parameter for our list of strings
# Create a new empty dictionary
# Loop through every string in the list of strings
# Inside the loop, if the string is not already in our dictionary, store the string as a key with a value of 0 in our dictionary. Then, increment the value by 1.
# After the loop, return the new dictionary


def frequency_dictionary(words):
    freqs = {}
    for word in words:
        if word not in freqs:
            freqs[word] = 0
        freqs[word] += 1
    return freqs


# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0, 0, 0, 0, 0]))
# should print {0:5}

# 3. Unique Values
# Now let’s try reading a dictionary as input and finding how many values are unique. The function should return a number which is the count of all values from the dictionary without including duplicates. These are the steps:
# Define the function to accept one parameter for our dictionary
# Create a new empty list
# Loop through every value in our dictionary
# Inside the loop, if the value is not already in our list, append the value to our list
# After the loop, return the length of our list


def unique_values(my_dictionary):
    seen_values = []
    for value in my_dictionary.values():
        if value not in seen_values:
            seen_values.append(value)
    return len(seen_values)


# Uncomment these function calls to test your  function:
print(unique_values({0: 3, 1: 1, 4: 1, 5: 3}))
# should print 2
print(unique_values({0: 3, 1: 3, 4: 3, 5: 3}))
# should print 1

# 4. Count First Letter
# This function accepts a dictionary where the keys are last names and the values are lists of first names of people who have that last name. We need to calculate the number of people who have the same first letter in their last name. Here are the steps we need:
# Define the function to accept one parameter for our dictionary
# Create a new empty dictionary called letters
# Loop through every key in our names dictionary
# Inside the loop, get the first letter of the last name we are looking at. If the first letter is not in our letter dictionary, add it as a key with a value of 0. Then, increment that key by the number of people that have that last name
# After the loop, return the letters dictionary


def count_first_letter(names):
    letters = {}
    for key in names:
        first_letter = key[0]
        if first_letter not in letters:
            letters[first_letter] = 0
        letters[first_letter] += len(names[key])
    return letters


# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": [
      "Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow": [
      "Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
