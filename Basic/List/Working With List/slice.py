# 1. Use print() to examine the variable beginning.
# Before hitting Run think about what elements beginning will contain?

# 2.Modify beginning, so that it selects the first 2 elements of suitcase.

# 3.Create a new list called middle that contains the middle two items ( ["pants", "pants"] ) from suitcase.
# Print middle to see the slice!

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:2]

# Your code below: 
print(beginning)

middle = suitcase[2:4]
print(middle)

# Slicing Lists II
# 1. Create a new list called last_two_elements containing the final two elements of suitcase.
# Print last_two_elements to see your result.

# 2.Create a new list called slice_off_last_three containing all but the last three elements.
# Print slice_off_last_three to see your result.

suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 
last_two_elements = suitcase[-2:]
print( last_two_elements) 

slice_off_last_three = suitcase[:-3]
print(slice_off_last_three) 