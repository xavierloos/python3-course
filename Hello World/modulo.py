# 1. You’re trying to divide a group into four teams. All of you count off, and you get number 27. Find out your team by computing 27 modulo 4. Save the value to my_team.

# 2. Print out my_team. What number team are you on?

# 3. Food for thought: what number team are the two people next to you (26 and 28) on? What are the numbers for all 4 teams? (Optional Challenge Question)
my_team = 27 % 4

print(my_team)

person_1 = 26 % 4

print(person_1)

person_2 = 28 % 4

print(person_2)

teams = 4 % 27
print(teams)
