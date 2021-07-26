# 1.Let’s replicate a function you are already familiar with, len().
# Write a new function called get_length() that takes a string as an input and returns the number of characters in that string. Do this by iterating through the string, don’t cheat and use len()!

def get_length(string):
    count = 0
    for letter in string:
        count += 1
    return count


print(get_length("Javier"))
