# For Loop

# Basic form

#for variable in <list_of_items>:
#    code to run

for loopvar1 in range(4):  # 0,1,2,3
    print(loopvar1)
print("---")
for loopvar1 in range(2,7): #  2,3,4,5,6
    print(loopvar1)
print("---")
for loopvar1 in range(10,0,-1): #  10,9,8,7,6,5,4,3,2,1
    print(loopvar1)
print("---")
for loopvar1 in range(0,100,5): # 0,5,10..95
    print(loopvar1)




    # If you know how many iterations you going to do 
    # you probably want a for loop
# break
print("---break---")
for loopvar1 in range(0,100,5): # 0,5,10..95
    if loopvar1 == 50:
        break
    print(loopvar1)
