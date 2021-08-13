# 1.Use a try block to try to print the caffeine level of "matcha". If there is a KeyError, print "Unknown Caffeine Level".

# 2.Above the try block, add "matcha" to the dictionary with a value of 30.

caffeine_level = {"espresso": 64, "chai": 40,
                  "decaf": 0, "drip": 120, "matcha": 30}

try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Unknown Caffeine Level")
