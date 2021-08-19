# 1.Let’s experiment with a way of recording historical data for our paint application. We want to save the last paints which were mixed and the result. To do this, we need some global variables which are not reinitialized every time we run the function, but instead are replaced by new values.
# Three global variables have been provided and initialized to None near the top of the code. In order to allow our function to replace the values stored in them, we need to use the global keyword. In this step, use the global keyword on each global variable at the top of the paint_mix() function so that we can modify those variables in the next step.

# 2.Now that we are able to modify those global variables and they are not seen as new local variables, go through the paint_mix() function and replace the values of those variables with the values corresponding to the first, second, and mixed colors.Use the input parameters for paint_mix() and the result of calling find_mixed_color().Run the code to see how our historical data is saved!

color_data = {('red', 'yellow'): 'orange',
              ('yellow', 'blue'): 'green',
              ('blue', 'red'): 'purple'}

previous_first_color = None
previous_second_color = None
previous_mixed_color = None


def paint_mix(first_color, second_color):
    # Write your code below!
    global previous_first_color
    global previous_second_color
    global previous_mixed_color

    print('Mixing ' + first_color + ' and ' +
          second_color + ' will result in:')

    # Write your code below!
    previous_first_color = first_color
    previous_second_color = second_color

    def find_mixed_color():

        if first_color == second_color:
            return first_color
        else:
            for colors in color_data.keys():
                if first_color in colors and second_color in colors:
                    if first_color == colors[0]:
                        return color_data[(first_color, second_color)]
                    else:
                        return color_data[(second_color, first_color)]
        return 'unknown'

    # Write your code below!
    previous_mixed_color = find_mixed_color()
    print(previous_mixed_color)


def show_last_mix():
    print()
    print('Repeating color mixture!')
    print('Mixing ' + previous_first_color + ' and ' +
          previous_second_color + ' will result in:')
    print(previous_mixed_color)


paint_mix('red', 'blue')

show_last_mix()
