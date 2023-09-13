fileobjectvar = open("Python/story.txt")

print(type(fileobjectvar))  # <class '_io.TextIOWrapper'>  type

#help(fileobjectvar)

stringvar1 = fileobjectvar.read()

print(type(stringvar1))

print("how many sheep")
print(stringvar1.count("sheep"))

dogstory = stringvar1.replace("sheep","dog")
print(dogstory)