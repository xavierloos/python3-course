# 1.Jiho is pleased with how we can store orders for our tables. However, the staff now wants to distinguish between food items and drinks.
# Since food items get prepared in the kitchen and drinks are prepared at the bar, it’s important to distinguish between the two in our application.
# The tables dictionary has been changed to support the staff’s requests. Take some time to examine the changed structure.
# Run the code to move on to the next checkpoint!

# 2.Since our program now requires a distinction between food items and drinks, this is a great place to utilize the power of **kwargs.
# Define a function called assign_food_items() that has one parameter, order_items. Pair this parameter with a ** operator to handle any keyword arguments.
# For now, just have the function print order_items.

# 3.Now we want to capture the food items and drinks in order_items. Use the .get() method to do the following:
# Capture the values from a keyword argument called food and assign it to a variable called food
# Capture the values from a keyword argument called drinks and assign it to a variable called drinks
# Refer to the commented example call at the bottom of the script for a reference on how we will call this function later on.

# 4.Lastly, inside of our function use print() to output the food variable and another print() to output the drinks variable.

# 5.Uncomment the example call provided to test our function!

tables = {
    1: {
        'name': 'Chioma',
        'vip_status': False,
        'order': {
            'drinks': 'Orange Juice, Apple Juice',
            'food_items': 'Pancakes'
        }
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}

print(tables)


# Write your code below:

def assign_food_items(**order_items):
    print(order_items)
    food = order_items.get("food")
    drinks = order_items.get("drinks")
    print(food)
    print(drinks)


# Example Call
assign_food_items(food='Pancakes, Poached Egg', drinks='Water')

# 1.In the last exercise, we saw how using ** allowed us to capture different food items that a table will order. In the next few checkpoints, we will finish implementing the functionality of our assign_food_items() function.
# Take some time to get reacquainted with the program. Note the changes in the assign_food_items() function.
# Run the code to move on!

# 2.Unfortunately, when we originally implemented assign_food_items we did not assign the values we capture into our tables dictionary.
# Adjust the function definition of assign_food_items():
# Add a positional parameter called table_number followed by the **order_items parameter we already defined.
# Uncomment the 2 lines inside the function.
# Adding the parameter and uncommenting the lines will now allow us to assign the food to a specific table.

# 3.Great! Now that we have the base functionality set up, let’s give it a test run. Luckily a new customer named Douglas just came in and is ready to place an order.
# Under print('\n --- tables after update --- \n'), call the assign_food_items() function with the following arguments:
# A positional argument table_number with the value 2
# A keyword argument food with the value 'Seabass, Gnocchi, Pizza'
# A keyword argument drinks with the value 'Margarita, Water'
# Print tables to see the change!

tables = {
    1: {
        'name': 'Chioma',
        'vip_status': False,
        'order': {
            'drinks': 'Orange Juice, Apple Juice',
            'food_items': 'Pancakes'
        }
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}


def assign_table(table_number, name, vip_status=False):
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = {}


assign_table(2, 'Douglas', True)

print('--- tables with Douglas --- \n', tables)


def assign_food_items(table_number, **order_items):
    food = order_items.get('food')
    drinks = order_items.get('drinks')
    tables[table_number]['order']['food_items'] = food
    tables[table_number]['order']['drinks'] = drinks


print('\n --- tables after update --- \n')
assign_food_items(2, food='Seabass, Gnocchi, Pizza', drinks='Margarita, Water')
print(tables)
