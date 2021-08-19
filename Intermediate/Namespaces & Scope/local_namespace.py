# 1.Note: Since we will be printing a lot of namespaces, the current editor has markers for where to write each checkpoint.
# First, let’s look at the differences between the global and local namespaces for a file with one variable defined. In the code editor, write two print statements that:
# print locals()
# print globals()
# Examine the output of both. Notice any similarities?

# 2.Now that we have seen what a local namespace looks like without any other code, let’s add some functions so we can check out local namespaces inside of a function.
# Create a function called divide() that has two parameters num1 and num2.
# The function should create a variable called result that is the result of dividing num1 by num2. The function should then also print locals().

# 3.Let’s add some more names! Create a function called multiply() that has two parameters num1 and num2.
# The function should create a variable called product that is the result of multiplying num1 by num2. This function should also print locals().

# 4.To see our local namespace inside divide(), we need to execute it. Call divide() with the values of 3 & 4. Examine the local namespace it generates.

# 5.To see our local namespace inside multiply(), we need to execute it. Call multiply() with the values of 4 & 50. Examine the local namespace it generates. Notice any similarities?

# 6.Let’s examine how the local namespace called outside of functions has changed. Print locals() once more. Notice any changes?

global_variable = 'global'

print(' -- Local and global Namespaces with empty script -- \n')
# Write Checkpoint 1 here:
print(locals())
print(globals())

# Write Checkpoint 2 here:


def divide(num1, num2):
    result = num1 / num2
    print(locals())

# Write Checkpoint 3 here:


def multiply(num1, num2):
    product = num1 * num2
    print(locals())


print(' \n -- Local Namespace for divide -- \n')
# Write Checkpoint 4 here:
divide(3, 4)

print(' \n -- Local Namespace for multiply -- \n')
# Write Checkpoint 5 here:
multiply(4, 50)

print(' \n -- Local Namespace final -- \n')
# Write Checkpoint 6 here:
print(locals())
