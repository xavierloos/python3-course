# 1. Use .sort() to sort addresses.

# 2. Use print() to see how addresses changed.

# 3. Remove the # and whitespace in front of the line sort(names). Edit this line so that it runs without producing a NameError.

# 4. Use print to examine sorted_cities. Why is it not the sorted version of cities?

# 5.Edit the .sort() call on cities such that it sorts the cities in reverse order (descending).
# Print cities to see the result.

# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]


# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)
print(cities)

addresses.sort()
print(addresses)