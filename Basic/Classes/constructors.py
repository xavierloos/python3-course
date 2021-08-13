# 1.Add a constructor to our Circle class.
# Since we seem more frequently to know the diameter of a circle, it should take the argument diameter.
# It doesn’t need to do anything yet, just write pass in the body of the constructor.

# 2.Now have the constructor print out the message "New circle with diameter: {diameter}" when a new circle is created.
# Create a circle teaching_table with diameter 36.

class Circle:
    pi = 3.14

    # Add constructor here:
    def __init__(self, diameter):
        print("New circle with diameter: {diameter}".format(diameter=diameter))


teaching_table = Circle(36)
