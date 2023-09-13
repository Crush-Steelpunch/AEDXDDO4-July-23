import math   # import the module

sqrtof9 = math.sqrt(9)   # access the function with modname.funcname()
print(sqrtof9)

from string import capwords  # import just the function from the module

somewords = input("Type some words: ")
print(capwords(somewords))    # call the function



from calendar import monthcalendar as mnth  # renaming functions

for row in mnth(2023,9):
    print(row)