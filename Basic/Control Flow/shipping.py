# Ground Shipping:
# 1. First things first, define a weight variable and set it equal to any number.

# 2. Next, we need to know how much it costs to ship a package of given weight by normal ground shipping based on the “Ground shipping” table above.

# Write a comment that says “Ground Shipping”.

# Create an if/elif/else statement for the cost of ground shipping. It should check for weight, and print the cost of shipping a package of that weight.

# 3. A package that weighs 8.4 pounds should cost $53.60 to ship with normal ground shipping:

# 8.4 * $4.00 + $20.00 = $53.60
# Test that your ground shipping function gets the same value.

# Ground Shipping Premium:
# 4. We’ll also need to make sure we include the price of premium ground shipping in our code.

# Create a variable for the cost of premium ground shipping.

# Note: This does not need to be an if statement because the price of premium ground shipping does not change with the weight of the package.

# 5. Print it out for the user just in case they forgot!
 
# Drone Shipping:
# 6. Write a comment for this section of the code, “Drone Shipping”.

# Create an if/elif/else statement for the cost of drone shipping. This statement should check against weight and print the cost of shipping a package of that weight.
 
# 7. A package that weighs 1.5 pounds should cost $6.75 to ship by drone:

# 1.5 * $4.50 + $0.00 = $6.75
# Test that your drone shipping function gets the same value.

# Solution:
# 8. Great job! Now, test everything one more time!

# What is the cheapest method of shipping a 4.8 pound package and how much would it cost?
# What is the cheapest method of shipping a 41.5 pound package and how much would it cost?

weight = 41.5
flat_charge = 20
cost_ground_premium = 125.00
print("Ground Shipping Premium: " + str(cost_ground_premium) )
# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + flat_charge
elif weight <= 6:
  cost_ground = weight * 3 + flat_charge
elif weight <= 10:
  cost_ground = weight * 4 + flat_charge
else: 
  cost_ground = weight * 4.75 + flat_charge
print("Ground Shipping: " + str(cost_ground))
# Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5 
elif weight <= 6:
  cost_drone = weight * 9 
elif weight <= 10:
  cost_drone = weight * 12 
else:
  cost_drone = weight * 14.25 
print("Drone Shipping: " + str(cost_drone))