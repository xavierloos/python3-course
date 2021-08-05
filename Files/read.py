# 1.Use with to open the file welcome.txt. Save the file object as text_file.

# 2.Read the contents of text_file and save the results in text_data.

# 3.Print out text_data.

with open('welcome.txt') as text_file:
    text_data = text_file.read()
print(text_data)
