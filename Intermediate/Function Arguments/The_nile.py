# Not Just A River In Egypt
# 1.At The Nile our biggest concern is our consumers, and our biggest cost is delivering their goods to them. We want to develop a program that will help us minimize these costs so we can continue making everyone happy.
# First we’ll need to calculate these costs using a function that you’re going to write called calculate_shipping_cost().
# Give calculate_shipping_cost three parameters: from_coords, to_coords, and shipping_type.

# 2.Both from_coords and to_coords are tuples, containing first the latitude and then the longitude. Since our get_distance() function looks for all four as separate arguments, we’ll need to separate these variables out.
# Inside calculate_shipping_cost unpack those tuples into from_lat, from_long, to_lat, and to_long.

# 3.Now call get_distance(from_lat, from_long, to_lat, to_long) and save the result as distance.
# There’s other ways to separate those two coordinates when calling this function, how would you have done it?

# 4.Next, get the shipping_rate by using the provided SHIPPING_PRICES dictionary and fetching the key passed in as shipping_type.

# 5.Calculate the price by multiplying the distance by the shipping_rate.

# 6.Finally, return the formatted price, created by calling the provided format_price() on the price itself.

# 7.What about our shoppers who hastily purchase goods without indicating their shipping type? Let’s give our function a default argument for shipping_type. Since they’re in such a hurry let’s make the default argument 'Overnight'. They’ll be happier to get what they ordered earlier, and we’ll be happier because they paid more money for it. It’s a win-win!

# 8.Want to make sure you wrote the function correctly? Try calling test_function(calculate_shipping_cost) after your function definition.
from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:


def calculate_shipping_cost(from_coords, to_coords, shipping_type="Overnight"):
    from_lat, from_long = from_cords
    to_lat, to_long = to_coords
    distance = get_distance(*from_coords, *to_coods)
    shipping_rate = SHIPPING_PRICES[shipping_type]
    price = distance * shipping_rate
    return format_price(price)


# Test the function by calling
test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here


# Test the function by calling
# test_function(calculate_driver_cost)

# Define calculate_money_made() here


# Test the function by calling
# test_function(calculate_money_made)
