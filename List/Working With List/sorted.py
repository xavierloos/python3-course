# 1.Use sorted() to order games and create a new list called games_sorted.

# 2.Print both games and games_sorted.How are they different?

games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)
print(games)
print(games_sorted)

# 4. Substring Between
# Here is a challenging problem. We need a function that is able to extract a portion of a string between two characters. The function will take three parameters where the first parameter is the string we are going to extract the substring from, the second input is the starting character of our substring and the third character is the ending character of our substring. Here are the steps we can use:
# Define the function to accept three parameters, one string and two characters
# find the starting index of our substring using the second input parameter
# find the ending index of our substring using the third input parameter
# If neither of the indices are -1, return the portion of the first input parameter string between the starting and ending indices (not including the starting and ending index)
# If either of the indices are -1, that means the start or end of the substring didn’t exist in our string. Return the original string in this case.


def substring_between_letters(word, start, end):
    start_ind = word.find(start)
    end_ind = word.find(end)
    if start_ind > -1 and end_ind > -1:
        return(word[start_ind+1:end_ind])
    return word


# Uncomment these function calls to test your function:
print(substring_between_letters("apple", "p", "e"))
# should print "pl"
print(substring_between_letters("apple", "p", "c"))
# should print "apple"

# 5. X Length
# Let’s use the split method in a different way. We need a new function that is able to accept two inputs: one for a sentence and another for a number. The function returns True if every single word in the sentence has a length greater than or equal to the number provided. These are the steps:
# Define the function to accept two parameters, one string, and one number
# Split up the sentence into an array of words
# Loop through the words. If the length of any of the words is less than the provided number return False
# If we made it through the loop without returning False then return True


def x_length_words(sentence, x):
    sentence = sentence.split()
    for word in sentence:
        if len(word) < x:
            return False
    return True
    # return sentence


# Uncomment these function calls to test your tip function:
print(x_length_words("i like apples", 2))
# should print False
print(x_length_words("he likes apples", 2))
# should print True

# Strings (Advanced)
# 1. Check Name
# You are creating an app that allows users to interact and share their coding project ideas online. The first step is to provide your name in the application and a greeting for other people to see which contains your name. Let’s create a function that is able to check if a user’s name is located within their greeting. We need a function that accepts two parameters, a string for our sentence and a string for a name. The function should return True if the name exists within the string (ignoring any differences in capitalization). Here is what we need to do:
# Define the function to accept two parameters, one string for the sentence and one string for the name
# Convert all of the strings to the same case so we don’t have to worry about differences in capitalization
# Check if the name is within the sentence. If so, then return True. Otherwise, return False


def check_for_name(sentence, name):
    if name.lower() in sentence.lower():
        return True
    else:
        return False


# Uncomment these function calls to test your  function:
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False


# 2. Every Other Letter
# For this next function, we are going to create a function that extract every other letter from a string and returns the resulting string. There are a few different ways you can solve this problem Here are the steps needed for one of the ways:
# Define the function to accept one parameter for the string
# Create a new empty string to hold every other letter from the input string
# Loop through the input string while incrementing by two every time
# Inside the loop, append the character at the current location to the new string we initialized earlier
# Return the new string

def every_other_letter(word):
    word_str = []
    indx = 0
    # for w in word:
    while indx < len(word):
        word_str.append(word[indx])
        indx += 2
    return "".join(word_str)


# Uncomment these function calls to test your function:
print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print

# 3. Reverse
# This one is similar to the last challenge. Instead of selecting every other letter, we want to reverse the entire string. This can be performed in a similar manner, but we will need to modify the range we are using. Here is what we need to do:
# Define the function to accept one parameter for the string
# Create a new empty string to hold the reversed string
# Loop through the input string by starting at the end, and working towards the beginning
# Inside the loop, append the character at the current location to the new string we initialized earlier
# Return the result


def reverse_string(word):
    reverse = ""
    for i in range(len(word)-1, -1, -1):
        reverse += word[i]
    return reverse


# Uncomment these function calls to test your  function:
print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string(""))
# should print

# 4. Make Spoonerism
# A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism is made when someone says “Belly Jeans” instead of “Jelly Beans”. We are going to make a function that is similar, but instead of using the first syllable, we are going to switch the first character of two words. Here is what we need to do:
# Define the function to accept two parameters for our two words
# Get the first character of the first word and the first character of the second word
# Get the remaining characters of the first word and the remaining characters of the second word.
# Append the first character of the second word to the remaining character of the first word
# Append a space character
# Append the first character of the first word to the remaining characters of the second word.
# Return the result


def make_spoonerism(word1, word2):
    word_1 = word2[0] + word1[1:]
    word_2 = word1[0] + word2[1:]
    return word_1 + " " + word_2


# Uncomment these function calls to test your function:
print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a
