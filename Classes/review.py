# 1.Define a class Student this will be our data model at Jan van Eyck High School and Conservatory.

# 2.Add a constructor for Student. Have the constructor take in two parameters: a name and a year. Save those two as attributes .name and .year.

# 3.Create three instances of the Student class:
# Roger van der Weyden, year 10
# Sandro Botticelli, year 12
# Pieter Bruegel the Elder, year 8
# Save them into the variables roger, sandro, and pieter.

# 4.Create a Grade class, with minimum_passing as an attribute set to 65.

# 5.Give Grade a constructor. Take in a parameter score and assign it to self.score.

# 6.In the body of the constructor for Student, declare self.grades as an empty list.

class Student():
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []


roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)


class Grade():
    minimum_passing = 65

    def __init__(self, score):
        self.score = score
