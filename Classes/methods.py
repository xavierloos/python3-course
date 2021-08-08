# 1.At Jan van High, the students are constantly calling the school rules into question. Create a Rules class so that we can explain the rules.

# 2.Give Rules a method washing_brushes that returns the string .
# "Point bristles towards the basin while washing your brushes."

class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."

# ANOTHER EXAMPLE

class Dog:
    dog_time_dilation = 7

    def time_explanation(self):
        print("Dogs experience {} years for every 1 human year.".format(
            self.dog_time_dilation))


pipi_pitbull = Dog()

pipi_pitbull.time_explanation()
