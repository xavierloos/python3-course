# 1.Jiho wants to expand our restaurant application to also take orders from customers. This is the perfect time to use the unpacking operator since we never know how many items customers are going to order.
# To start, we want to build a function that will compile a list of all the items a customer wants to order and then print it out. This will help our kitchen know what to cook.
# Define a function called print_order() that will take in a variable number of arguments using a parameter called order_items. The function should simply print order_items.

# 2.Looks like our first order came in! Call our function print_order() with the following order items:
# 'Orange Juice'
# 'Apple Juice'
# 'Scrambled Eggs'
# 'Pancakes'

# Write your code below:
def print_order(*order_items):
    print(order_items)


print_order('Orange Juice', 'Apple Juice', 'Scrambled Eggs', 'Pancakes')

# 1.Jiho is having a lot of success with our restaurant application. Unfortunately, our original design did not account for storing orders for each specific table. Jiho asked us to adjust our application to be able to store the orders that come in for each specific table and also be able to print out the order for the kitchen staff.
# Take some time to review the adjusted structure of the program we created earlier. Note that tables is now dictionary with the table numbers as the keys. It also accounts for a new property called order. The assign_table function has also been adjusted to account for the changes.
# Run the code to move onto the next checkpoint.

# 2.To help Jiho implement the ability to store the order in a specific table, let’s implement a function called assign_and_print_order().
# The function should have two parameters called table_number and order_items. The parameter of order_items should be grouped with an unpacking operator (*) so we can capture a variable number of order items per table.
# For now, our program will error out if we run it. Don’t worry we will fill in the function in the next step!

# 3.Our function assign_and_print_order() should then assign an order to a table. Inside of our function access the nested order key for the specific table (using the table_number argument) from tables and set it to the order_items parameter.

# 4.In addition to assigning the order to our tables dictionary, we also want to print every ordered item so the kitchen knows what to cook!
# Inside of assign_and_print_order() use a for loop to iterate through order_items and print each individual order item.

# 5.Lastly, let’s see our function in action. Luckily we just had a new customer come in for their reservation. Use the assign_table() function to add a new customer named 'Arwa' to table 2 with a VIP status set to True.

# 6.Now that Arwa is seated and ready to order, call our assign_and_print_order() function for table 2 with the order items of 'Steak', 'Seabass', and 'Wine Bottle'.
# Print tables to see the result!

tables = {
    1: {
        'name': 'Jiho',
        'vip_status': False,
        'order': 'Orange Juice, Apple Juice'
    },
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
}

print(tables)


def assign_table(table_number, name, vip_status=False):
    tables[table_number]['name'] = name
    tables[table_number]['vip_status'] = vip_status
    tables[table_number]['order'] = ''

# Write your code below:


def assign_and_print_order(table_number, *order_items):
    tables[table_number]['order'] = order_items
    for order in order_items:
        print(order)


assign_table(2, 'Arwa', True)

assign_and_print_order(2, 'Steak', 'Seabass', 'Wine Bottle')

print(tables)
