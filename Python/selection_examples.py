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



