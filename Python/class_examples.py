# Classes
# A programmatic object containing data and methods
# i.e. variables and functions


# Basic Form

"""
class Classname:

    attribute = "some data"

    def methodname(input):
        <code for method goes here>
        return value
"""


class Dog:

    breed = "labrador"
    weight = 35
    energy = "Medium"

    def communicate(self):
        return "woof"



bonnie = Dog()

bonnie.energy = "High"

print(bonnie.energy)
print(bonnie.communicate())

goldie = Dog()

print(goldie.energy)
print(goldie.communicate())

bonnie = Dog()

bonnie.energy = "High"

print(bonnie.energy)
print(bonnie.communicate())

