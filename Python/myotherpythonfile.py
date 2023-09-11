# this is a file for showing people how to do a python file

print("Hello Class")    # This is a line that will be run

#         0101110111
# Binary representation of 4312858897
# Could be a telebphone number
# Could be a decimal value of money
# Could be an ip address
# 

# Data typing 
# - Integer, any whole number , e.g 1, -15 101,110,111
# - Floating, any fractional number, e.g 1.0, -15.5. 101.110111
# - String, alphanumeric text e.g. 'cat' 'Dinosaur2055', '01 110 1111'
# - Boolean, true or false value e.g 'True', 'False'



varname = 'value'  

integervar = 123        # Integer
floatvar = 123.45       # Float
stringvar = "text here" # String
boolvar = True          # Boolean, no quotes, capitalized words

print(integervar)
print(floatvar)
print(stringvar)
print(boolvar)

myVar1 = "I like pies"  # start vars with a lower case letter
x = "somthing here"     # make variable names explain what they are for
print(myVar1)
print(x)


# Input

input()  # This will pause the program so you can type in

inputString = input("Please Type in a word: ")  # store input in a var

print(inputString) # print the contents of the var

# Variable Manupulation

textVar1 = input('Type in your name: ')
textVar2 = input('Type in an animal: ')

print(textVar1 + textVar2)

print(textVar1 + " typed in the animal " + textVar2)

# numbers

numvar1 = 15
numvar2 = 12
print(numvar1 + numvar2)

# example 2


awsomenessvar1 = input('Type your awesomeness level: ')
print(30 + int(awsomenessvar1))

# casting

integervar = 123        # Integer
floatvar = 123.45       # Float
stringvar = "20" # String
boolvar = True          # Boolean, no quotes, capitalized word

print(30 + int(stringvar))

# Commas in the print statement

print("string" + str(30) + "another string") # This needs to be converted to work

print("string" , 30 , "another string")  # commas convert everything to a string
# but also add spaces

# casting to float

floatvar2 = 1.23
floatvar3 = 1.99  # this does not round up
print(int(floatvar2))
print(int(floatvar3))
