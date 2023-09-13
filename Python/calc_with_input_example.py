while True:

    inputvar1 = input("no1: ")
    inputvar2 = input("no2: ")

    if inputvar1.isnumeric():
        if inputvar2.isnumeric():
            print(float(inputvar1)+float(inputvar2))
        else:
            print("Needs number")
    else:
        print("Needs number")
