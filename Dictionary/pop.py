# 1.You are designing the video game Big Rock Adventure. We have provided a dictionary of items that are in the player’s inventory which add points to their health meter. In one line, add the corresponding value of the key "stamina grains" to the health_points variable and remove the item "stamina grains" from the dictionary. If the key does not exist, add 0 to health_points.

# 2.In one line, add the value of "power stew" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.

# 3.In one line, add the value of "mystic bread" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.

# 4.Print available_items and health_points.

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20,
                   "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20,
                   "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)

health_points += available_items.pop("power stew", 0)

health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)
