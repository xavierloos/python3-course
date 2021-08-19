# 1.The users of our applications have requested that we add a way of calculating the amount of paint needed for an entire room or multiple rooms.
# In order to accomplish this, we need to make some modifications to our script from earlier. The function calc_paint_amount() now accepts a single parameter which is assumed to be a list of tuples containing the width and height of each wall.
# For the first step, define another function nested inside of calc_paint_amount() called calc_square_feet() which defines no parameters.

# 2.Next, inside of calc_square_feet(), for every width and height provided in the list of tuples, multiply them together and add them to our square_feet variable.
# Since we need to modify square_feet in an enclosing scope, make sure to mark it as nonlocal!

# 3.Finally, add a call to our new nested function before the call to calc_gallons().Run the code and take a look at the result!

walls = [(20, 9), (25, 9), (20, 9), (25, 9)]


def calc_paint_amount(wall_measurements):

    square_feet = 0

    # Write your code below!
    def calc_square_feet():
        nonlocal square_feet
        for width, height in wall_measurements:
            square_feet += (width * height)

    def calc_gallons():
        return square_feet / 400

    # Write your code below!
    calc_square_feet()
    return calc_gallons()


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(walls)))
