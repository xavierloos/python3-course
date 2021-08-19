# 1.For the final change to our painting app, we are going to expand on the paint_mix() function to allow for new combinations to be added to our color_data.
# For the first step, define a new nested function called add_new_mixture() inside of the paint_mix() function which accepts no arguments.

# 2.Inside of the new function, access the global variable color_data and write a key, value pair using the(first_color, second_color) tuple as a key and the resulting_color as a value.

# 3.Finally, try calling paint_mix with different color combinations and adding them to the color_data variable.Any new combinations will be saved in the dictionary and can be used by the function due to it’s global scope.

color_data = {('red', 'yellow'): 'orange',
              ('yellow', 'blue'): 'green',
              ('blue', 'red'): 'purple'}


def paint_mix(first_color, second_color, resulting_color=None):
    print('Mixing ' + first_color + ' and ' +
          second_color + ' will result in:')

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
    def add_new_mixture():
        global color_data

    if resulting_color is not None:
        add_new_mixture()
        color_data[(first_color, second_color)] = resulting_color

    print(find_mixed_color())


paint_mix('blue', 'white', 'light blue')

paint_mix('blue', 'white')

# Write your code below!
paint_mix('red', 'blue')
