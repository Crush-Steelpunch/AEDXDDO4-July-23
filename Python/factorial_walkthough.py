# Task 2 - Factorial
# 1. Add a new file: Factorial.py and make it the startup file. - DONE
# 2. Ask the user to input an integer.  - DONE 
# 3. Display the number's factorial using a while loop.
# Note: the factorial of a number is that number multiplied by all the
# preceding numbers.
# The factorial of 5 is = 5 x 4 x 3 x 2 x 1 = 120
# or if you like = 1 x 2 x 3 x 4 x 5
# 4. Save and run


factvar = int(input("INTEGER: "))

# While Loop

initialcountvar = factvar

while factvar > 1:
    preceedvar = factvar - 1
    if factvar == initialcountvar:
        resultvar = preceedvar * factvar  # the first time preceedvar needs to multiply by fact var
    else:
        resultvar = resultvar * preceedvar  # the subsiquent times we need to muliply by resultvar
    factvar = preceedvar  
print(resultvar)

# For Loop
factvar = int(input("INTEGER: "))

fact = 1
for loopvar in range(1,factvar + 1):
     fact = loopvar * fact
print(fact)
