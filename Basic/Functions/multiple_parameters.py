# 1.Our travel application users want to calculate the total expenses they may have to incur on a trip.
# Write a function called calculate_expenses that will have four parameters (in exact order):
# plane_ticket_price
# car_rental_rate
# hotel_rate
# trip_time
# Each of these parameters will account for a different expense that our users will incur.
# Note: Like before, if we run this function now, we will get an error since there are no statements in the body.

# 2.Within the body of the function, let’s start to make some calculations for our expenses. First, let’s calculate the total price for a car rental.
# Create new variable called car_rental_total that is the product of car_rental_rate and trip_time.

# 3.Next, we want to apply the same logic but for our hotel_rate.
# Create new variable called hotel_total that is the product of hotel_rate and trip_time.
# We also have a coupon to give our users some cashback for their hotel visit so subtract 10 from that total in the same statement. Woohoo, coupons! 💵
# Hint
# Use * to perform multiplication between the two variables.Don’t forget to subtract 10 after!

# 4.Lastly, let’s print a nice message for our users to see the total. Use print to output the sum of car_rental_total, hotel_total and plane_ticket_price.

# 5.Call your function with the following argument values for the parameters listed:
# plane_ticket_price : 200
# car_rental_rate : 100
# hotel_rate : 100
# trip_time: 5

# Write your code below:
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
    car_rental_total = car_rental_rate * trip_time
    hotel_total = (hotel_rate * trip_time) - 10
    print("The car rental total is: ", car_rental_total)
    print("The hotel total is: ", hotel_total)


calculate_expenses(200, 100, 100, 5)
