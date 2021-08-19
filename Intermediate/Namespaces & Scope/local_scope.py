# 1.Our close friend Jiho wants to start a painting business. In order to help, we have created a small painting application that will print out the required colors for a specific painting.
# Take some time to examine the code provided, and run it to see an error come up! Why are we getting a NameError?

# 2.Let’s fix the scoping error by moving the print statement right above the for loop defined in the painting() function. This will put the function call in the correct local scope to be able to access painting_statement.

def painting(paint_colors, picture):
    painting_statement = "To paint the " + \
        picture + " we need the following colors: "
    print(painting_statement)
    for color in paint_colors:
        print(color)


painting(['Orange', 'White', 'Green'], 'Indian Flag')
