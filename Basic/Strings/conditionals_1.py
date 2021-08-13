# 1.Write a function called letter_check that takes two inputs, word and letter.
# This function should return True if the word contains the letter and False if it does not.

def letter_check(word, letter):
    for w in word:
        if w == letter:
            return True
    return False


print(letter_check("strawberry", "a"))
