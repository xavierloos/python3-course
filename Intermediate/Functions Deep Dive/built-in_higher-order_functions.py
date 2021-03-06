# Say we stored our course grades in a list, but some of the grades were on a four-point scale and others were on a 100-point scale. To get all the grades on the same scale, try using a lambda function with the map() function to multiply just the grades on the four-point scale by 25 to get all of the grades on the same 100-point-scale.

from functools import reduce

grade_list = [3.5, 3.7, 2.6, 95, 87]

# Your code below:
# assign the result of your map function to the variable grades_100scale

grades_100scale = map(lambda grade: grade*25 if grade <=
                      4.0 else grade, grade_list)

# convert grades_100scale to a list and save it as updated_grade_list
updated_grade_list = list(grades_100scale)

# print updated_grade_list
print(updated_grade_list)

# We were given a list of lists, where each sublist holds the title of a famous book that has a year as its title and the last name of the author that wrote the book. Unfortunately, when this list was made, each of the books was accidentally entered twice—once with the title as a numeric value and once with the title as a string. Use the filter() function to deduplicate the list and keep only the sublists that have the book title stored as a string:

books = [["Burgess", 1985], ["Orwell", "Nineteen Eighty-four"], ["Murakami", "1Q85"],
         ["Orwell", 1984], ["Burgess", "Nineteen Eighty-five"], ["Murakami", 1985]]

# Your code below:

# assign the result of your filter function to the variable  string_titles

string_titles = filter(lambda value: type(value[1]) == str, books)

# convert your filter object to a list stored in the variable string_titles_list

string_titles_list = list(string_titles)

# print the list string_titles_list

print(string_titles_list)

# Given a list of letters, use the reduce() higher-order function with a lambda function to combine the letters into a single word:
letters = ['r', 'e', 'd', 'u', 'c', 'e']

# your code below:

# remember to import the reduce function

# store the result of your reduce function in the variable word

word = reduce(lambda x, y: x+y, letters)

# print word

print(word)
