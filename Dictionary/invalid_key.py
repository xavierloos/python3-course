# 1. Run the code inside script.py. You should get an error:
# TypeError: unhashable type
# Make the code run without errors by flipping the items in the dictionary so that the strings are the keys and the lists are the values

# children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"}

children = {"von Trapp": ["Johannes", "Rosmarie",
                          "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}
