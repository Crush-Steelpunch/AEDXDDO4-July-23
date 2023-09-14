fileobjectvar = open("Python/story.txt")  # create a "File Object" 

print(type(fileobjectvar))  # <class '_io.TextIOWrapper'>  type

help(fileobjectvar)
# using read()
stringvar1 = fileobjectvar.read()

print(type(stringvar1))

print("how many sheep")
print(stringvar1.count("sheep"))

dogstory = stringvar1.replace("sheep","dog")
print(dogstory)

# using readlines()

fileobjectvar.seek(0)  # return to the start of the file to read it all again

listvar1 = fileobjectvar.readlines()
listvar1.append("THE END\n")
print(listvar1)

# Close the read only object

fileobjectvar.close()

# Open the file for writing

writefileobjectvar = open("Python/story.txt","w")  # open and delete the file contents
# push the data to be written to disk
writefileobjectvar.write(dogstory)
# close the file
writefileobjectvar.close()

# Basic workflow
# open()
# read() or readlines()
# close()
# manipulate the data
# open("w")
# write()
# close()

