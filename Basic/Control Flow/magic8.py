# Setting up
# 1. In magic8.py, declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.
 
# 2. Next, declare a variable question, and assign to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.
 
# 3. We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.
 
# Generating a random number
# 4. In order for the answer to be different each time we run the program, we will utilize randomly generated values.

# Note: This will be something new! But don’t worry, we will try to explain this topic thoroughly and also supply the code.

# In Python, we can use the .randint() function from the random module to generate a random number from a range.

# But first, let’s import this module so we can use its functions. Add this line of code to the top of magic8.py:

# import random
 
# 5. Next, we’ll create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call:

# random.randint(1, 9)
# which will generate a random number between 1 (inclusive) and 9 (inclusive).

# Next, add a print() statement that outputs the value of random_number, and run the program several times to ensure random values are being generated as expected.

# Once you’re sure this is working as we expected, feel free to comment out this print() statement.
 
# Control Flow
# 6. Now that we’ve declared all the variables needed, it’s time to implement the core logic of our program!

# For this section, we’ll be utilizing control flow using an if/elif/else statement to assign different answers for each randomly generated value.

# First, write an if statement where if the random_number is equal to 1, answer is assigned to the phrase “Yes - definitely.”
 
# 7. Next, write an elif statement after the if statement where if the random_number is equal to 2, answer is assigned to the phrase “It is decidedly so”.

# Then, continue writing elif statements for each of the remaining phrases for the values 3 to 9.

# Recall that the 9 possible answers of the Magic 8-Ball are:

# Yes - definitely.
# It is decidedly so.
# Without a doubt.
# Reply hazy, try again.
# Ask again later.
# Better not tell you now.
# My sources say no.
# Outlook not so good.
# Very doubtful.
 
# 8. Following the if/elif statements, add an else statement that will set answer to the string “Error”, if the number was accidentally assigned a value outside of our range.
 
# Seeing the result
# 9. Now, let’s see our program in action! Write a print() statement to output the asker’s name and their question, which should be in the following format:

# [Name] asks: [Question]
# For example, when we run the program, the output should look something like: Joe asks: Will I win the lottery?

# 10. Add a second print() statement that will output the Magic 8-Ball’s answer in the following format:

# Magic 8-Ball's answer: [answer]
# For example, when running the program it should look something like: Magic 8-Ball's answer: My sources say no
 
# 11. Great job! You’ve successfully utilized your knowledge of conditionals and previous fundamental Python concepts to create a program that generates different fortunes.

# Run your program several times to see that it’s working as expected.

# Optional Challenges
# 12. If you’re up for some more challenges, try implementing the following features to your program.

# So far, the Magic 8-Ball provides 9 possible fortunes. Try to add a few more possible answers to the program.

# To do this, you will need to increase the range of randomly generated numbers and add additional elif statements for each new answer.
 
# 13. What if the asker does not provide a name, such that the value of name is an empty string? If the name string is empty, the output of the program looks like the following:

#  asks: Will I win the lottery?
# Magic 8 Ball's answer: Outlook not so good
# As you can see, the formatting of the output can use some improvement when there is no name provided.

# We can address this by printing out just the question, such that it looks like the following:

# Question: Will I win the lottery?
# Magic 8-Ball's answer: Outlook not so good
# You can implement this by creating an if/else statement such that:

# If the name is an empty string, it will only print the question.
# Else, the player’s name and question are both printed.

# 14. What if the question string is empty? If the user does not provide any question, then the Magic 8-Ball cannot provide a fortune, otherwise, the fabric of reality is at risk!

# To ensure that the fabric of reality is safe, we can create an if/else statement where:

# If the question is an empty string, print out a message to the user.
# Else, print the name and question, with the Magic 8-Ball’s answer.

import random
name = "Javi"
question = "Will I win the lottery?"
answer = ""
random_number = random.randint(1, 10)
# print(random_number)
if random_number == 1:
  answer = "Yes - definitely."
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt."
elif random_number == 4:
  answer = "Reply hazy, try again."
elif random_number == 5:
  answer = "Ask again later."
elif random_number == 6:
  answer = "Better not tell you now."
elif random_number == 7:
  answer = "My sources say no."
elif random_number == 8:
  answer = "Outlook not so good."
elif random_number == 9:
  answer = "Very doubtful."
elif random_number == 10:
  answer = "I'll tell you tomorrow."
else:
  answer = "Error"
if question== "":
  print("No question provided")
else:
  if name == "":
    print(question)
  else:
    print(name + " asks: " + question)
  print("Magic 8-Ball's answer: "+answer) 