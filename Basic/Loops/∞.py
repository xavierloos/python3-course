# Suppose we have two lists of students, students_period_A and students_period_B. We want to combine all students into students_period_B.

# In your code editor, we have provided you a loop. Go ahead and uncomment line 5 and before you run the code ponder why this code would cause an infinite loop.

# When you are ready, run this code. What do you notice happens? Over the run button, notice the loading circle is continuing without anything happening.

# This is an infinite loop! To end this program we must refresh the page. (Note: The reason this loop is infinite is that we’re adding each student in students_period_A to students_period_A which would create a never-ending list of all the student names.)

# Delete the line causing the infinite loop and fix it to accomplish the original goal of combining all students from students_period_A into students_period_B.

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:
  # students_period_A.append(student)
  print(student)