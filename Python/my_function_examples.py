# Writing your own functions

def functionName():
    #code bit here
    pass   # This `pass` keyword lets you define a function with no actual code


def showTwo():   # This defines the function
    print(2)




showTwo()    # This calls the function, to run it
# Function with Input 


def addTwo(inputvar):
    if inputvar.isnumeric():
        print(int(inputvar) + 2)
    else:
        print("You didn't give me a number!")

mynumber = input("Gimme number!: ")

addTwo(mynumber)


# Function with a return

def doubler(inputvar):
    return [inputvar,inputvar]

doubleme = input("What shall I double?")
listofdoubledthings  = doubler(doubleme)
print(listofsoubledthings)