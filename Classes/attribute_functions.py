# 1.In script.py we have a list of different data types: a dictionary, a string, an integer, and a list all saved in the variable can_we_count_it.
# For every element in the list, check if the element has the attribute count using the hasattr() function. If so, print the following line of code:
# print(str(type(element)) + " has the count attribute!")

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in can_we_count_it:
    if hasattr(element, "count"):
        print(str(type(element)) + " has the count attribute!")
