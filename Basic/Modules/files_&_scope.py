# 1.Tab over to library.py and define a function always_three() with no parameters that returns 3.

# 2.Call your always_three() function in script.py. Check out that error message you get in the output terminal and the consequences of file scope.

# 3.Resolve the error with an import statement at the top of script.py that imports your function from library. Run your code and watch import do its magic!

# library.py 
# Add your always_three() function below:
def always_three():
  return 3

# script.py
# Import library below:
from library import always_three


# Call your function below:
print(always_three())