# 1.You’ve been provided with a list of words from the first line of Jean Toomer’s poem Reapers.
# Use .join() to combine these words into a sentence and save that sentence as the string reapers_line_one.

reapers_line_one_words = ["Black", "reapers", "with",
                          "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = " ".join(reapers_line_one_words)

print(reapers_line_one)

# 1.You’ve been given a list, winter_trees_lines, that contains all the lines to William Carlos Williams poem, Winter Trees. You’ve been asked to join together the strings in the list together into a single string that can be used to display the full poem. Name this string winter_trees_full.
# Print your result to the terminal. Make sure that each line of the poem appears on a new line in your string.

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among',
                      'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']
winter_trees_full = "\n".join(winter_trees_lines)
print(winter_trees_full)
