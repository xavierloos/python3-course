# 1.In script.py you’ll find our familiar friend, the Circle class.
# Even though we usually know the diameter beforehand, what we need for most calculations is the radius.
# In Circle‘s constructor set the instance variable self.radius to equal half the diameter that gets passed in.

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = diameter / 2
