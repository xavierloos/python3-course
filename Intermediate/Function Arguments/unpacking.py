# 1.Jiho thinks our restaurant application is missing one really important feature. Jiho would like for the application to be able to calculate the total bill of a table (including tip) and split it based on the number of people at the table.
# Thankfully, we had an existing function called calculate_price_per_person() from our last restaurant project that we can reuse. Take some time to examine the function and its inner workings.
# Run the code to move onto the next checkpoint. Don’t worry we shouldn’t see any output just yet.

# 2.Looks like we are ready to give our function a test run! Luckily, table seven at Jiho’s restaurant is ready to pay.
# Define a list called table_7_total that has the following values in order:
# 534.50 (Representing the total bill cost)
# 20.0 (Representing the tip percentage)
# 5 (Representing the number of people to split the bill for)

# 3.Using the unpacking operator, call calculate_price_per_person() with the list table_7_total.

def calculate_price_per_person(total, tip, split):
    total_tip = total * (tip/100)
    split_price = (total + total_tip) / split
    print(split_price)


# Write your code below:
table_7_total = [534.50, 20.0, 5]

calculate_price_per_person(*table_7_total)
