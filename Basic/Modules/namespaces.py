# 1.Below import codecademylib3_seaborn, import pyplot from the module matplotlib with the alias plt.

# 2.Import random below the other import statements. It’s best to keep all imports at the top of your file.

# 3.Create a variable numbers_a and set it equal to the range of numbers 1 through 12 (inclusive).

# 4.Create a variable numbers_b and set it equal to a random sample of twelve numbers within range(1000).

# 5.Now let’s plot these number sets against each other using plt. Call plt.plot() with your two variables as its arguments.

# 6.Now call plt.show() and run your code!
# You should see a graph of random numbers displayed. You’ve used two Python modules to accomplish this (random and matplotlib).

import codecademylib3_seaborn

# Add your code below:
from matplotlib import pyplot as plt

import random

numbers_a = range(1, 13)

numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a, numbers_b)

plt.show()