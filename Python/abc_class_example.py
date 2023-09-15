# The Abstract Base Class
from abc import ABC, abstractmethod 

class Bird(ABC):

    def __init__(self,reproductioncount):
        self.reproductioncount = reproductioncount
    
    @abstractmethod
    def eat(self):
        pass

    def communicate(self):
        return "tweet"




class Finch(Bird):
    
    def eat(self,worms):
        return "yum {} worms".format(worms)

freddyfinchoff = Finch(1)

print(freddyfinchoff.communicate())

print(freddyfinchoff.eat(14))


class Penguin(Bird):

    def eat(self, fish):
        return "yum {} fish".format(fish)

pingu = Penguin(1)

print(pingu.eat(12))