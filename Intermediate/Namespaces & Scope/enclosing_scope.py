# 1.A new addition to our painting application that we are building for Jiho will be a function that calculates the amount of paint needed to cover a surface.
# Typically, a gallon of paint can cover about 400 square feet. Using that knowledge, we can accept a width and height of a surface to determine how much paint is needed! We will be using nested functions to organize our code to allow us to easily add more utility to this function in the next exercises.
# First, define a nested function called calc_gallons() inside of calc_paint_amount() which has no parameters.

# 2.Next, inside of calc_gallons() use enclosing scope to access the variable square_feet from the calc_gallons() function.
# Return the result of square_feet divided by 400.

# 3.Finally, in the calc_paint_amount() function, call the calc_gallons() function and return the result. Run the code and take a look at the result!


def calc_paint_amount(width, height):

    square_feet = width * height
    # Write your code below!

    def calc_gallons():
        return square_feet / 400

    return calc_gallons()


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30, 20)))
