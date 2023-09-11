# Selection Examples

# Basic Form

# if <test>:
#    perform an action   # this will run if the test is true

inputvar = int(input('Input a number that is not 7: '))

if inputvar == 7:
    print("You typed a seven even though I told you not to")
    result = inputvar^2
    print("If your number was a square, it would have the area:", result)

    # ==  is equal to
if inputvar > 7:
    print("You typed a big number")

if inputvar != 7:
    print("You typed a number that isn't 7")

if inputvar <= 7:
    print("You typed a number that is 7 or less")

if inputvar > 7 and inputvar < 1000:
    print("Your number is between 8 and 999")

if inputvar == 7 or (inputvar > 12 and inputvar < 20):
    print("Either 7 or in the teens")



    # using else for returning information if the test is false

if inputvar > 10:
    print("You passed!")
else:
    print("You Failed!")
    

# Using elif to perform multiple sequential tests

if inputvar < 10:
    print("you have a single digit number")
elif inputvar < 100:
    print("you have a double digit number")
elif inputvar < 1000:
    print("You have a triple digit number")
else:
    print("Your number is huuuuge")

print("end program")