# 1.For an upcoming holiday, Jiho plans on making a prix fixe menu for the restaurant. Customers at the restaurant will be able to choose the following:
# 1 Appetizer
# 2 Entrees
# 1 Side dish
# 2 Scoops of different ice cream flavors for dessert.
# To accomplish all these choices, we are going to utilize the different types of arguments that we have learned so far. Review the current function in the editor and run the code to move on!

# 2.Let’s start by defining a function called single_prix_fixe_order() which will define four parameters to accept the full order:
# A parameter named appetizer
# A parameter named entrees paired with a * operator
# A parameter named sides
# A parameter named dessert_scoops paired with a ** operator
# Our function should simply have four print() statements that print each individual parameter.

# 3.We got our first prix fixe order in! The customer wants the following:
# 'Baby Beets' as an appetizer
# 'Salmon' and 'Scallops' as entrees
# 'Mashed Potatoes' as a side
# A scoop of 'Vanilla' ice cream and a scoop of 'Cookies and Cream' for dessert
# Utilize our function single_prix_fixe_order() to print out all of the customers order.

# Write your code below:
def single_prix_fixe_order(appetizer, *entrees, sides, **dessert_scoops):
    print(appetizer)
    print(entrees)
    print(sides)
    print(dessert_scoops)


single_prix_fixe_order('Baby Beets', 'Salmon', 'Scallops', sides='Mashed Potatoes',
                       ice_cream_scoop1='Vanilla', ice_cream_scoop2='Cookies and Cream')
