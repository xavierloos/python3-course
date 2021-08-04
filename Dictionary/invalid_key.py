# 1. Run the code inside script.py. You should get an error:
# TypeError: unhashable type
# Make the code run without errors by flipping the items in the dictionary so that the strings are the keys and the lists are the values

# children = {["Johannes", "Rosmarie", "Eleonore"]: "von Trapp", ["Sonny", "Fredo", "Michael"]: "Corleone"}

children = {"von Trapp": ["Johannes", "Rosmarie",
                          "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

# 1.Run the code. It should throw a KeyError! "energy" does not exist as one of the elements.

# 2.Add the key "energy" to the zodiac_elements. It should map to a value of "Not a Zodiac element". Run the code. Did this resolve the KeyError?

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": [
    "Taurus", "Virgo", "Capricorn"], "air": ["Gemini", "Libra", "Aquarius"], "energy": "Not a Zodiac element"}

# print(zodiac_elements["energy2"])

print(zodiac_elements["energy"])
