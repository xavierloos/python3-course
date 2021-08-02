# 1.In script.py import the random library.

# 2.Create a variable random_list and set it equal to an empty list

# 3.Turn the empty list into a list comprehension that uses random.randint() to generate a random integer between 1 and 100 (inclusive) for each number in range(101).

# 4.Create a new variable randomer_number and set it equal to random.choice() with random_list as an argument.

# 5.Print randomer_number out to see what number was picked!

# Import random below:
import random

# Create random_list below:
random_list = []

# Create randomer_number below:
random_list = [random.randint(1, 100) for i in range(101)]

# Print randomer_number below:
randomer_number = random.choice(random_list)

print(randomer_number)
