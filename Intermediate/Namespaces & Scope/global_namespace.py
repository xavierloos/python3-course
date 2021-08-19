# 1.Note: Since we will be printing a lot of namespaces, the current editor has markers for where to write each checkpoint.
# Let’s start by examining the global namespace when the script is empty.
# Call globals() inside of a print() function to observe the current global namespace.

# 2.Let’s now add some Python code to see how the namespace changes. Add a variable called global_variable with the value of 'global'.

# 3.Let’s add some more code to populate the namespace! Add a function called print_global() that does the following:
# Defines a variable inside called global_variable with the value of 'nested global'.
# Defines a variable inside called nested_variable with the value of 'nested value'.

# 4.Let’s examine how the global namespace has changed. Print the globals() function once more.

# 5.Here are some important takeaways to note from the comparison:
# As we saw previously, the global namespace only contains items that are non-nested. In this case, our global namespace does not contain the identical nested name of global_variable.
# Depending on where we call globals() we will have a different namespace generated. This means globals() will show the namespace at the time it was executed. Since we called globals() a second time after defining a few items (such as variables and functions), those items now show up in the global namespace.
# Play around with the code and run it one more time to move onto the next exercise.

print(' -- Globals Namespace with empty script -- \n')
# Write Checkpoint 1 here:
print(globals())


# Write Checkpoint 2 here:
global_variable = "global"


# Write Checkpoint 3 here:
def print_global():
    global_variable = "nested global"
    nested_variable = "nested value"


print(' \n -- Globals Namespace non-empty script -- \n')
# Write Checkpoint 4 here:
print(globals())
