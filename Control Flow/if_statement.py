# 1. There is an if statement. I wrote this because my coworker Dave kept using my computer without permission and he is a real doofus. If the user_name is Dave, it tells him to stay off my computer.

# Enter a user name in the field for user_name and try running the program.

# 2. Oh no! We got a SyntaxError! This happens when we make a small error in the syntax of the conditional statement.

# Read through the error message carefully and see if you can find the error. Then, fix it, and run the code again.

# 3. Ugh! Dave got around my security and has been logging onto my computer using our coworker Angela’s user name, angela_catlady_87.

# Set your user_name to be angela_catlady_87.

# Update the program with a second if statement so it checks for Angela’s user name as well and prints

# "I know it is you, Dave! Go away!"
# in response.That’ll teach him!

# Enter a user name here, make sure to make it a string
user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")
if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")