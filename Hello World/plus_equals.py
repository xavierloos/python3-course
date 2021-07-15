# 1. We’re doing a little bit of online shopping and find a pair of new sneakers. Right before we check out, we spot a nice sweater and some fun books we also want to purchase!

# Use the += operator to update the total_price to include the prices of nice_sweater and fun_books.

# The prices (also included in the workspace) are:

# new_sneakers = 50.00
# nice_sweater = 39.00
# fun_books = 20.00

total_price = 0

new_sneakers = 50.00
total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price += nice_sweater

total_price += fun_books
print("The total price is", total_price)