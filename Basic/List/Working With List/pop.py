# 1. We have decided to pursue the study of data science in addition to our computer science coursework. We signed up for an online school that would help us become proficient.
# Check out the current list of topics we will be studying in our code editor. 
# Click Run to print out the list.
 
# 2. It looks like we have an overlap with our computer science curriculum for the topic of "Python 3". 
# Let’s remove the topic from the list of data_science_topics using our newly learned .pop() method. 
# Print data_science_topics to see your result.

# 3. Looks like there is overlap on the "Algorithms" topic as well. Let’s use .pop() to remove it as well. 
# Print data_science_topics to see the changes.

data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 
data_science_topics.pop()
print(data_science_topics)

data_science_topics.pop(3)
print(data_science_topics)