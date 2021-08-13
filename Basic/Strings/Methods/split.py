# 1.In the code editor is a string of the first line of the poem Spring Storm by William Carlos Williams.
# Use .split() to create a list called line_one_words that contains each word in this line of poetry.

line_one = "The sky has given over"

line_one_words = line_one.split()


# 1.Your boss at the Poetry organization sent over a bunch of author names that he wants you to prepare for importing into the database. Annoyingly, he sent them over as a long string with the names separated by commas.
# Using .split() and the provided string, create a list called author_names containing each individual author name as it’s own string.

# 2.Great work, but now it turns out they didn’t want poet’s first names (why didn’t they just say that the first time!?)
# Create another list called author_last_names that only contains the last names of the poets in the provided string.

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print(author_last_names)

# 1.The organization has sent you over the full text for William Carlos Williams poem Spring Storm. They want you to break the poem up into its individual lines.
# Create a list called spring_storm_lines that contains a string for each line of Spring Storm.

spring_storm_text = \
    """The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split("\n")
