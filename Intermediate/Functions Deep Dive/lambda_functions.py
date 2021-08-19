# Convert the function below into a lambda function

# def add_bang(sentence):
#   print(sentence + '!')

def add_bang(string): return print(string + '!')


# Add a lambda function named double_or_zero that takes an integer named num.If num is greater than 10, return double the value of num.Otherwise, return 0.

def double_or_zero(num): return num * 2 if num > 10 else 0
