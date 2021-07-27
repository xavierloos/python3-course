# 1.Write a function called poem_title_card that takes two inputs: the first input should be title and the second poet. The function should use .format() to return the following string:
# The poem "[TITLE]" is written by [POET].
# For example, if the function is given the inputs
# poem_title_card("I Hear America Singing", "Walt Whitman")
# It should return the string
# The poem "I Hear America Singing" is written by Walt Whitman.

def poem_title_card(title, poet):
    return "The poem \"{}\" is written by {}.".format(title, poet)


print(poem_title_card("I Hear America Singing", "Walt Whitman"))
