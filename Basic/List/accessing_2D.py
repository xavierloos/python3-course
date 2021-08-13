# 1. We want to have a way to store all of our classroom test score data.

# Using the provided table, create a two-dimensional list called class_name_test to represent the data. Each sublist in class_name_test should have one student’s name and their associated score.

# Name	     Test Score
# "Jenny"	   90
# "Alexus"	 85.5
# "Sam"	     83
# "Ellie"	   101.5

# Print class_name_test to see the result.

# 2. Use double square brackets ([][]) to select Sam‘s test score from the list class_name_test.

# Save it to the variable sams_score.

# Print the variable sams_score to see the result.

# 3. Use double square brackets ([][]) to select Ellies test score from the list class_name_test. This time only use negative indices!

# Save it to the variable ellies_score.

# Print the variable ellies_score to see the result.

# Your code below:
class_name_test = [["Jenny",	90], [
    "Alexus",	85.5], ["Sam",	83], ["Ellie",	101.5]]
print(class_name_test)

sams_score = class_name_test[2][1]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)
