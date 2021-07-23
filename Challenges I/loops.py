# 1. Divisible By Ten
# Let’s start our code challenges with a function that counts how many numbers are divisible by ten from a list of numbers. This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. Every time a number is divisible by 10, a counter will be incremented and the final count will be returned. These are the steps we need to complete this:

# Define the function to accept one input parameter called nums
# Initialize a counter to 0
# Loop through every number in nums
# Within the loop, if any of the numbers are divisible by 10, increment our counter
# Return the final counter value

# Write your function here
def divisible_by_ten(nums):
    count = 0
    for n in nums:
        if n % 10 == 0:
            count += 1
    return count


# Uncomment the line below when your function is done
print(divisible_by_ten([20, 25, 30, 35, 40]))

# 2. Greetings
# You are invited to a social gathering, but you are tired of greeting everyone there. Luckily we can create a function to accomplish this task for us. In this challenge, we will take a list of names and prepend the string 'Hello, ' before each name. This will require a few steps:

# Define the function to accept a list of strings as a single parameter called names
# Create a new list of strings
# Loop through each name in names
# Within the loop, concatenate 'Hello, ' and the current name together and append this new string to the new list of strings
# Afterwards, return the new list of strings

# Write your function here


def add_greetings(names):
    greetings = []
    for name in names:
        greetings.append(("Hello, " + name))
    return greetings


# Uncomment the line below when your function is done
print(add_greetings(["Owen", "Max", "Sophie"]))

# 3. Delete Starting Even Numbers
# Let’s try a tricky challenge involving removing elements from a list. This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements. It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed. To do this, we will need the following steps:

# Define our function to accept a single input parameter lst which is a list of numbers
# Loop through every number in the list if there are still numbers in the list and if we haven’t hit an odd number yet
# Within the loop, if the first number in the list is even, then remove the first number of the list
# Once we hit an odd number or we run out of numbers, return the modified list

# Write your function here


def delete_starting_evens(lst):
    while len(lst) >= 1 and lst[0] % 2 == 0:
        lst = lst[1:]
    return lst


# Uncomment the lines below when your function is done
print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))

# 4. Odd Indices
# This next function will give us the values from a list at every odd index. We will need to accept a list of numbers as an input parameter and loop through the odd indices instead of the elements. Here are the steps needed:

# Define the function header to accept one input which will be our list of numbers
# Create a new list which will hold our values to return
# Iterate through every odd index until the end of the list
# Within the loop, get the element at the current odd index and append it to our new list
# Return the list of elements which we got from the odd indices.

# Write your function here


def odd_indices(lst):
    new_list = []
    index = 0
    while index < len(lst):
        if index % 2 != 0:
            new_list.append(lst[index])
        index += 1
    return new_list


# Uncomment the line below when your function is done
print(odd_indices([4, 3, 7, 10, 11, -2]))

# 5. Exponents
# In this challenge, we will be using nested loops in order to raise a list of numbers to the power of a list of other numbers. What this means is that for every number in the first list, we will raise that number to the power of every number in the second list. If you provide the first list with 2 elements and the second list with 3 numbers, then there will be 6 final answers. Let’s look at the steps we need:

# Define the function to accept two lists of numbers, bases and powers
# Create a new list that will contain our answers
# Create a loop that iterates through every base in bases
# Within that loop, create another loop that iterates through every power in power
# Within that nested loop, append the result of the current base raised to the current power.
# After all iterations of both loops are complete, return the list of answers

# Write your function here


def exponents(bases, powers):
    new_list = []
    for base in bases:
        for power in powers:
            new_list.append(base ** power)
    return new_list


# Uncomment the line below when your function is done
print(exponents([2, 3, 4], [1, 2, 3]))

# LOOPS ADVANCED
# 1. Larger Sum
# We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. We will iterate through each of the list and calculate the sums, afterwards we will compare the two and return which one has a greater sum. Here are the steps we need:

# Define the function to accept two input parameters: lst1 and lst2
# Create two variables to record the two sums
# Loop through the first list and add up all of the numbers
# Loop through the second list and add up all of the numbers
# Compare the first and second sum and return the list with the greater sum

# Write your function here


def larger_sum(lst1, lst2):
    sum1 = 0
    sum2 = 0
    for l1 in lst1:
        sum1 += l1
    for l2 in lst2:
        sum2 += l2
    print(sum1)
    print(sum2)
    if sum1 >= sum2:
        return lst1
    else:
        return lst2
