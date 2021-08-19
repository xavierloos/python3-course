# 1.Take a look at the two functions defined. One function named print_avaliable() prints the number of gallons we have available for a specific color. The other function named print_all_colors_avaliable() simply prints all available colors!
# Ponder what might happen when we run the script and then run it to find out!

# 2.Whoops! Looks like we have an error with accessing paint_gallons_avaliable in our print_all_colors_avaliable() function. This is because the dictionary is locally scoped.
# Fix the issue by moving paint_gallons_avaliable into the global scope.

paint_gallons_avaliable = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
}

def print_avaliable(color):
    print('There are ' +
          str(paint_gallons_avaliable[color]) + ' gallons avaliable of ' + color + ' paint.')


def print_all_colors_avaliable():
    for color in paint_gallons_avaliable:
        print(color)


print_avaliable('red')
print_all_colors_avaliable()
