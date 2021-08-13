# 1.We have been provided a list of grades in a physics class. Using a list comprehension, create a new list called scaled_grades that scales the class grades based on the highest score.

# Since the highest score was a 90 we simply want to add 10 points to all the grades in the list.

# 2.Print scaled_grades.

grades = [90, 88, 62, 76, 74, 89, 48, 57]

scaled_grades = [grade + 10 for grade in grades]

print(scaled_grades)

# List Comprehensions: Conditionals
# 1.We have defined a list heights of visitors to a theme park. In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters.
# Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.

# 2.Print can_ride_coaster.

heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = []

for height in heights:
  if height > 161:
    can_ride_coaster.append(height)

print( can_ride_coaster)