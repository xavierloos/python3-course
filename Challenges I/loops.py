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

# 2. Over 9000
# We are constructing a device that is able to measure the power level of our coding abilities and according to the device, it will be impossible for our power levels to be over 9000. Because of this, as we iterate through a list of power values we will count up each of the numbers until our sum reaches a value greater than 9000. Once this happens, we should stop adding the numbers and return the value where we stopped. In order to do this, we will need the following steps:

# Define the function to accept a list of numbers
# Create a variable to keep track of our sum
# Iterate through every element in our list of numbers
# Within the loop, add the current number we are looking at to our sum
# Still within the loop, check if the sum is greater than 9000. If it is, end the loop
# Return the value of the sum when we ended our loop

# Write your function here


def over_nine_thousand(lst):
    sum_lst = 0
    for l in lst:
        if sum_lst <= 9000:
            sum_lst += l
    return sum_lst


# Uncomment the line below when your function is done
print(over_nine_thousand([8000, 900, 120, 5000]))

# 3. Max Num
# Here is a more traditional coding problem for you. This function will be used to find the maximum number in a list of numbers. This can be accomplished using the max() function in python, but as a challenge, we are going to manually implement this function. Here is what we need to do:

# Define the function to accept a list of numbers called nums
# Set our default maximum value to be the first element in the list
# Loop through every number in the list of numbers
# Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
# Return the maximum number

# Write your function here


def max_num(nums):
    nums.sort()
    return nums[-1]


# Uncomment the line below when your function is done
print(max_num([50, -10, 0, 75, 20]))

# 4. Same Values
# In this challenge, we need to find the indices in two equally sized lists where the numbers match. We will be iterating through both of them at the same time and comparing the values, if the numbers are equal, then we record the index. These are the steps we need to accomplish this:

# Define our function to accept two lists of numbers
# Create a new list to store our matching indices
# Loop through each index to the end of either of our lists
# Within the loop, check if our first list at the current index is equal to the second list at the current index. If so, append the index where they matched
# Return our list of indices

# Write your function here


def same_values(lst1, lst2):
    new_list = []
    for index in range(len(lst1)):
        if lst1[index] == lst2[index]:
            new_list.append(index)
    return new_list


# Uncomment the line below when your function is done
print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
