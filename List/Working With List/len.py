# 1. Calculate the length of long_list and save it to the variable long_list_len.
  
# 2. Use print() to examine long_list_len.
 
# 3. We have provided a completed range() function for the variable range_list.
# Calculate its length using the function len() and save it to a variable called range_list_length.
# Note: Range objects do not need to be converted to lists in order to determine their length

# 4. Use print() to examine range_list_length.
# Hint
# Your output should be 300

# 5. Change the range() function that generates range_list so that it skips 100 instead of 10 steps between items.
# How does this change range_list_len?

long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

range_list = range(2, 3000, 100)

# Your code below: 
long_list_len = len(long_list)
print(long_list_len)

range_list_length = len(range_list)
print(range_list_length)