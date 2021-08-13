# 1. Examine the while loop from the narrative in your code editor. There are additional print() statements to help visualize the iterations.
# Run the code to see what happens on each iteration of the loop. When you are finished, comment out the example to make space for the rest of the checkpoints.
# To quickly comment out the code, use your cursor or mouse to highlight all the code and press command ⌘ + / on a Mac or CTRL + / on a Windows machine.

# 2.Let’s write a while loop that counts down from 10 to 0(inclusive). Once our loop is finished we will commemorate our accomplishment by printing "We have liftoff!".
# As we saw in the narrative, our key components will be:
# A variable to keep track of the count, and also help our loop eventually stop.
# A condition that our while loop will check on each iteration.
# Several code statements to execute on each iteration of the loop.
# Let’s tackle the first component!
# Create a variable named countdown and set the value to 10.

# 3.Now let’s tackle the actual while loop. Define a while loop that will run while our countdown variable is greater than or equal to zero.
# On each iteration:
# We should print() the value of the countdown variable.
# We should decrease the value of the countdown variable by 1
# If you notice the Run button spinning continuously or a “Lost connection to Codecademy” message in an exercise, you may have an infinite loop! If the stop condition for our loop is never met, we will create an infinite loop which stops our program from running anything else. To exit out of an infinite loop in an exercise, refresh the page — then fix the code for your loop.

# 4.Now that we have built our loop, let’s commemorate our success by printing "We have liftoff!" after the while loop.

countdown = 10

while countdown >= 0:
    print(countdown)
    countdown -= 1

print("We have liftoff!")

# While Loops: Lists
# 1.We are going to write a while loop to iterate over the provided list python_topics.
# First, we will need a variable to represent the length of the list. This will help us know how many times our while loop needs to iterate.
# Create a variable length and set its value to be the length of the list of python_topics.

# 2.Next, we will require a variable to compare to our length variable to make sure we are able to implement a condition that eventually allows the loop to stop.
# Create a variable called index and initialize the value to be 0.

# 3.Let’s now build our loop. We want our loop to iterate over the list of python_topics and on each iteration print "I am learning about <element from python_topics>". For this loop we will need the following components:
# A condition for our while loop
# A statement in the loop body to print from our condition
# A statement in the loop body to increment our index forward.
# The end result should output:
# I am learning about variables
# I am learning about control flow
# I am learning about loops
# I am learning about modules
# I am learning about classes
# If you notice the Run button spinning continuously or a “Lost connection to Codecademy” message in an exercise, you may have an infinite loop!If the stop condition for our loop is never met, we will create an infinite loop which stops our program from running anything else.To exit out of an infinite loop in an exercise, refresh the page — then fix the code for your loop.

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)

index = 0

while index < length:
  print("I am learning about ", python_topics[index])
  index += 1