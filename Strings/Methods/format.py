# 1.Write a function called poem_title_card that takes two inputs: the first input should be title and the second poet. The function should use .format() to return the following string:
# The poem "[TITLE]" is written by [POET].
# For example, if the function is given the inputs
# poem_title_card("I Hear America Singing", "Walt Whitman")
# It should return the string
# The poem "I Hear America Singing" is written by Walt Whitman.

def poem_title_card(title, poet):
    return "The poem \"{}\" is written by {}.".format(title, poet)


print(poem_title_card("I Hear America Singing", "Walt Whitman"))

# 1.The function poem_description is supposed to use .format() to print out some quick information about a poem, but it seems to be causing some errors currently.
# Fix the function by using keywords in the .format() method.

# 2.Run poem_description with the following arguments and save the results to the variable my_beard_description:
# author = "Shel Silverstein"
# title = "My Beard"
# original_work = "Where the Sidewalk Ends"
# publishing_date = "1974"


def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(
        title=title, author=author, original_work=original_work, publishing_date=publishing_date)
    return poem_desc


my_beard_description = poem_description(
    author="Shel Silverstein", title="My Beard", original_work="Where the Sidewalk Ends", publishing_date="1974")
