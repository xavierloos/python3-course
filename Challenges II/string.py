# 1. Count Letters
# For the first code challenge, we are going to count the number of unique letters in a string. This means that when we are looking at the word, any new letters should be counted and any duplicates should not be counted. There are a few ways to solve this, but we can use the provided alphabet string to ensure that duplicates are not counted. Here is what we need to do:
# Define the function to accept one parameter — the word whose letters we are counting
# Create a counter to keep track of unique letters
# Loop through every letter in our alphabet string. If the current letter was found in our word, increase our count
# Return the count after looping through all letters.

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:


def unique_english_letters(word):
    counter = []
    for letter in word:
        if letter in letters:
            if not letter in counter:
                counter.append(letter)

    return len(counter)


# Uncomment these function calls to test your function:
print(unique_english_letters("mississippi"))
# should print 4
print(unique_english_letters("Apple"))
# should print 4

# 2. Count X
# Next, we are going to try something a bit different. This time we are going to count the number of occurrences of a certain letter within a string. Our function will accept a parameter for a string and another for the character which we are going to count. For example, providing the word "mississippi" and the character 's' would result in an answer of 4. These are the steps we need to take:
# Define the function to accept two parameters. word for the input string and x for the single character
# Create a counter to keep track of the occurrences
# Loop through every letter in the string. If the current letter is equal to the input letter, increase our counter
# Return the counter after looping through the entire string.


def count_char_x(word, x):
    counter = 0
    for letter in word:
        if letter == x:
            counter += 1
    return counter


# Uncomment these function calls to test your tip function:
print(count_char_x("mississippi", "s"))
# should print 4
print(count_char_x("mississippi", "m"))
# should print 1
