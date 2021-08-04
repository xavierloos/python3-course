# 1.Create a variable called users and assign it to be a dict_keys object of all of the keys of the user_ids dictionary.

# 2.Create a variable called lessons and assign it to be a dict_keys object of all of the keys of the num_exercises dictionary.

# 3.Print users to the console.

# 4.Print lessons to the console.

user_ids = {"teraCoder": 100019, "pythonGuy": 182921,
            "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15,
                 "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()

lessons = num_exercises.keys()

print(users)

print(lessons)
