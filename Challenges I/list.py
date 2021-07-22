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
