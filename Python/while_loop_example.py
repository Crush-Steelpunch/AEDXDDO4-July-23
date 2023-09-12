# While loop
# Basic form

# var1 = 1  # Variable to test
# while <test on preset var>:
#    loop code goes here
#    change the variable


x = 1
while x <= 5:
    print(x,"Hello World")
    x = x + 1

# slide example

n = 1
while n <= 5:
    print('*' * n)
    n = n + 1
print('*' * n)
while n > 0:
    n = n - 1
    print('*' * n)