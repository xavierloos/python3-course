# 1.It’s March 14th (known in some places as Pi day) at Jan van High, and you’re feeling awfully festive. You decide to create a program that calculates the area of a circle.
# Create a Circle class with class variable pi. Set pi to the approximation 3.14.

# 2.Give Circle an area method that takes two parameters: self and radius.
# Return the area as given by this formula:
# area = pi * radius ** 2

# 3.Create an instance of Circle. Save it into the variable circle.

# 4.You go to measure several circles you happen to find around.
# A medium pizza that is 12 inches across.
# Your teaching table which is 36 inches across.
# The Round Room auditorium, which is 11,460 inches across.
# You save the areas of these three things into pizza_area, teaching_table_area, and round_room_area.
# Remember that the radius of a circle is half the diameter. We gave three diameters here, so halve them before you calculate the given circle’s area.

class Circle:
    pi = 3.14

    def area(self, radius):
        area = self.pi * radius ** 2
        return area


circle = Circle()

pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)
