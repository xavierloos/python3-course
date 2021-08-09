# 1.In script.py you’ll find our familiar friend, the Circle class.
# Even though we usually know the diameter beforehand, what we need for most calculations is the radius.
# In Circle‘s constructor set the instance variable self.radius to equal half the diameter that gets passed in.

class Circle:
    pi = 3.14

    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        # Add assignment for self.radius here:
        self.radius = diameter / 2


# 2.Define three Circles with three different diameters.
# A medium pizza, medium_pizza, that is 12 inches across.
# Your teaching table, teaching_table, which is 36 inches across.
# The Round Room auditorium, round_room, which is 11,460 inches across.

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)
