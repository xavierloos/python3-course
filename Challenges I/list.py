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

# Write your function here


def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst


# Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

# 3. Larger List
# Let’s say we are working with two conveyor belts that contain items represented by a numerical ID. If one conveyor belt contains more items than the other, then we need to return the ID of the last item on that belt. In the case where they have the same number of items, return the last item from the first conveyor belt. In our code, we can represent the belts using lists. Here are the steps:

# Define the function to accept two parameters for our two lists of numbers
# Check if the length of the first list is greater than or equal to the length of the second list
# If true, then return the last element from the first list. Otherwise, return the last element from the second list

# Write your function here


def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    elif len(lst1) < len(lst2):
        return lst2[-1]
    else:
        return lst1[-1]


# Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

# 4. More Than N
# Our factory produces a variety of different flavored snacks and we want to check the number of instances of a certain type. We have a conveyor belt full of different types of snacks represented by different numbers. Our function will accept a list of numbers (representing the type of snack), a number for the second parameter (the type of snack we are looking for), and another number as the third parameter (the maximum number of that type of snack on the conveyor belt). The function will return True if the snack we are searching for appears more times than we provided as our third parameter. These are the steps we need:

# Define the function to accept three parameters, a list of numbers, a number to look for, and a number for the number of instances
# Count the number of occurrences of item (the second parameter) in lst (the first parameter)
# If the number of occurrences is greater than n (the third parameter), return True. Otherwise, return False

# Write your function here


def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False


# Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

# 5. Combine Sort
# Finally, let’s create a function that combines two different lists together and then sorts them. To do this we can combine the lists with an operation and then sort using a function call. Here are the steps we need to use:

# Define the function to accept two parameters, one for each list.
# Combine the two lists together
# Sort the result
# Return the sorted and combined list

# Write your function here


def combine_sort(lst1, lst2):
    new_list = lst1 + lst2
    new_list.sort()
    return new_list


# Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))


# LIST ADVANCED
# 1. Every Three Numbers
# Let’s start our challenging problems with a function that creates a list of numbers up to 100 in increments of 3 starting from a number that is passed to the function as an input parameter. Here is what we need to do:

# Define the function to accept one parameter for our starting number
# Calculate the numbers between the starting number and 100 while incrementing by 3
# Store the numbers in a list
# Return the list

# Write your function here
def every_three_nums(start):
    lst = range(start, 101, 3)
    return list(lst)


# Uncomment the line below when your function is done
print(every_three_nums(91))

# 2. Remove Middle
# Our next function will remove all elements from a list with an index within a certain range. The function will accept a list, a starting index, and an ending index. All elements with an index between the starting and ending index should be removed from the list. Here are the steps:

# Define the function to accept three parameters: the list, the starting index, and the ending index
# Get all elements before the starting index
# Get all elements after the ending index
# Combine the two partial lists into the result
# Return the result

# Write your function here


def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1:]


# Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

# 3. More Frequent Item
# Let’s go back to our factory example. We have a conveyor belt of items where each item is represented by a different number. We want to know, out of two items, which one shows up more on our belt. To solve this, we can use a function with three parameters. One parameter for the list of items, another for the first item we are comparing, and another for the second item. Here are the steps:

# Define the function to accept three parameters: the list, the first item, and the second item
# Count the number of times item1 shows up in our list
# Count the number of times item2 shows up in our list
# If item1 shows up more, return item1. Otherwise, return item2

# Write your function here


def more_frequent_item(lst, item1, item2):
    if lst.count(item1) > lst.count(item2):
        return item1
    elif lst.count(item2) > lst.count(item1):
        return item2
    else:
        return item1


# Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

# 4. Double Index
# Our next function will double a value at a given position. We will provide a list and an index to double. This will create a new list by replacing the value at the index provided with double the original value. If the index is invalid then we should return the original list. Here is what we need to do:

# Define the function to accept two parameters, one for the list and another for the index of the value we are going to double
# Test if the index is invalid. If its invalid then return the original list
# If the list is valid then get all values up to the index and store it as a new list
# Append the value at the index times 2 to the new list
# Add the rest of the list from the index onto the new list
# Return the new list

# Write your function here


def double_index(lst, index):
    if len(lst) <= index:
        return lst
    else:
        lst.insert(index, lst[index] * 2)
        lst.remove(lst[index+1])
        return lst


# Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))
