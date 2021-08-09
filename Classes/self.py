# 1.In script.py you’ll find our familiar friend, the Circle class.
# Even though we usually know the diameter beforehand, what we need for most calculations is the radius.
# In Circle‘s constructor set the instance variable self.radius to equal half the diameter that gets passed in.

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = diameter / 2

    def circumference(self):
        circumference = 2 * self.pi * self.radius
        return circumference


# 2.Define three Circles with three different diameters.
# A medium pizza, medium_pizza, that is 12 inches across.
# Your teaching table, teaching_table, which is 36 inches across.
# The Round Room auditorium, round_room, which is 11,460 inches across.

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

# 3.Define a new method circumference for your circle object that takes only one argument, self, and returns the circumference of a circle with the given radius by this formula:
# circumference = 2 * pi * radius
