# 1.Using the LEGB rule, we are going to try and correct this function to behave how we expect it to. It should replace the color with a new provided color and print out the old and new colors. Try running the code to see what the first issue is .

# 2.The LEGB rule starts with “Local”. Let’s take a look at any local variable issues that we could be running into. Looking at each of the local variables, we can see that to_update is local to the function disp_color(), but we attempt to access it from change_color(). Move the initialization of to_update so that the scope is local to change_color(). Try running the code now and see what happens.

# 3.Now we are not getting any errors, but the output is not correct.There doesn’t seem to be any encompassing scope issues, but there is an issue with the global variable.We are using the global keyword to allow this variable to be modified in order to print the new color, but if we look at the order of operations, we modify the global variable before calling disp_color.To fix this, define and call that function before the global variable is modified!Run the code and see that happens!

color = 'green'

# Fix the function below:


def change_color(new_color):
    to_update = new_color
    global color

    def disp_color():
        print('The original color was: ' + color)

    disp_color()
    color = to_update
    print('The new color is: ' + color)


change_color('blue')
