# Block Letters
# ASCII art is a graphic design technique that uses computers for presentation and consists of pictures pieced together from individual characters.

# Write a Python program called initials.py that displays the initials of your name in block letters as shown and dip your toes into ASCII art.

# What we are building in this project:
# 1. Take a look at the complete alphabet and find your initials. Notice how each block letter is 7x5 and formed by the letter itself.

# My initials are S and L, so my initials.py program should output:

#  SSS   L
# S   S  L
# S      L
#  SSS   L
#     S  L
# S   S  L
#  SSS   LLLLL
# Once you are ready, mark this task complete by checking off the box.

# Setting up:
# 2. First, write two comments with:

# Your first and last name.
# A fun fact about yourself.

# 3. Output your first initial as a block letter. There are a few ways to do this!

# Press Save to run your program.

# 4. Output your second initial as a block letter by adding to the print() statements.

# Press Save to run your program.

# Javier Lopez
first_initial = """
JJJJJ  
   J
   J
   J
J  J
J  J
JJ
"""

second_initial = """
L
L
L 
L
L
L
LLLLL
"""
print(first_initial + second_initial)