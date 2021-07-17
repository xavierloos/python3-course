# 1. In script.py, another teammate Alex wrote a Who Wants to Be A Millionaire question and four options. If the answer is an uppercase or lowercase “A”, then the score goes up.

# Run the program to check it out.
 
# 2. Oh no, there are two NameError errors!

# Can you find them both?

# Who Wants To Be A Millionaire 💰 

score = 0

option1 = 'Fresca'
option2 = 'V8'
option3 = 'Certo'
option4 = 'A&W'
  
print("For ordering his favorite beverages on demand, LBJ had four buttons installed in the Oval Office labeled 'Coffee', 'Tea', 'Coke', and what?\n")

print("A.", option1)
print("B.", option2)
print("C.", option3)
print("D.", option4)
  
answer = 'a'

if answer == 'A' or answer == 'a': 
  score += 100
  print("\nCorrect!")
else:
  print("\nNope, sorry!")