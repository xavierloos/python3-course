# 1.You’re a programmer working for an organization that is trying to digitize and store poetry called Preserve the Verse.
# You’ve been given two strings, the title of a poem and it’s author, and have been asked to reformat them slightly to fit the conventions of the organization’s database.
# Make poem_title have title case and save it to poem_title_fixed.

# 2.Print poem_title and poem_title_fixed.
# How did the string change?

# 3.The organization’s database also needs the author’s name to be uppercase only.
# Make poem_author uppercase and save it to poem_author_fixed.

# 4.Print poem_author and poem_author_fixed.
# Again, how did the string change?

poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title()

print(poem_title)
print(poem_title_fixed)

poem_author_fixed = poem_author.upper()

print(poem_author)
print(poem_author_fixed)
