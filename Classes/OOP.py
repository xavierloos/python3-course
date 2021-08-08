# 1.In script.py we see facade_1 from last exercise. Try calling type() on facade_1 and saving it to the variable facade_1_type.

# 2.Print out facade_1_type.

class Facade:
    pass

facade_1 = Facade()

facade_1_type = type(facade_1)

print(facade_1_type)
