# List
#    Index Number: 0          1            2                3             4          5           
shoppinglist = [ "Cake","Biscuits","cake", "biscuits", "cannedfish", "sparklingwater", "carrots", "potatoes" ]

# python list of string objects

oddnumlist = [ 1, 5 , 7, 9, 11 ]  # list of integers

boollist = [True,False,False,True,True,False,True]

print(["list", "of", "things"])

print(shoppinglist)
print(oddnumlist)

for loopvar in shoppinglist:  # lists can be used as iterators
    print(loopvar)

print(shoppinglist[1])
print(shoppinglist[-1])  # last item of the list
print(shoppinglist[2:4])  # items 2 & 3


# list of lists

megalist = [shoppinglist, oddnumlist, boollist]

print(megalist)
print(megalist[1][2])  # return from list index 1, item index 2

# function for list lenght

print(len(boollist))

# strings are lists

stringvar = "Leon is Ace"

for letter in stringvar:
    print(letter)

print(len(stringvar))

print(stringvar[3])  # single letter from a string
print(stringvar[0:4]) # range of letters



# help(shoppinglist) 

shoppinglist.append("plasters")
shoppinglist.append("batteries")

print(shoppinglist)

print(boollist.count(True))  # count howm many of a specific item is in the list

shoppinglist.remove("sparklingwater")

print(shoppinglist)

shoppinglist.insert(0,"freddos")
print(shoppinglist)

shoppinglist.sort()

print(shoppinglist)

# Converting lists to strings

joinchar = ","
shoppingliststr =  joinchar.join(shoppinglist)

print(shoppingliststr)
print(type(shoppingliststr))

# converting strings to lists

splitstr = "monitor,laptop,glass,ipad,mouse,webcam"
newlist1 = splitstr.split(",")  # split the string on the commas to a list

print(newlist1)
print(type(newlist1))


# the 'in' test

list1 = ["sheep", "cow", "llama","pig","horse","dog","goat","chicken"]

testanimal = input("ANIMAL: ")
if testanimal in list1:
    print("In list")
else:
    print("not in list")


while testanimal not in list1:
    print("No! guess again")
    testanimal = input("ANIMAL: ")