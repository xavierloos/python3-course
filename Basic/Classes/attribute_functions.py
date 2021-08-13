# 1.In script.py we have a list of different data types: a dictionary, a string, an integer, and a list all saved in the variable can_we_count_it.
# For every element in the list, check if the element has the attribute count using the hasattr() function. If so, print the following line of code:
# print(str(type(element)) + " has the count attribute!")

# 2.Now let’s add an else statement for the elements that do not have the attribute count. In this else statement add the following line of code:
# print(str(type(element)) + " does not have the count attribute :(")

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in can_we_count_it:
    if hasattr(element, "count"):
        print(str(type(element)) + " has the count attribute!")
    else:
        print(str(type(element)) + " does not have the count attribute :(")

# 3.Let’s go over the terminal output of the past two instructions. You should see the following output in your terminal right now:
# <class 'dict'> does not have the count attribute :(
# <class 'str'> has the count attribute!
# <class 'int'> does not have the count attribute :(
# <class 'list'> has the count attribute!
# This is because dictionaries and integers both do not have a count attribute, while strings and lists do. In this exercise, we have iterated through can_we_count_it and used hasattr() to determine which elements have a count attribute. We never actually used the count method, but you can read more about it here if you are curious about what it is.
# Click run to move onto the next exercise!