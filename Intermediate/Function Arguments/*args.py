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
