# Exception Handling

# Basic Form

# try:
#     <code that might fail>
# except:
#     <code that runs if the try fails>


try:
    textfilevar = open('filethatdoesnotexist.txt')
    print('The File exists and I opened it')
    textfilevar.close()
except Exception as e:
    print('It failed! because: ', e)
    textfilevar = open('filethatdoesnotexist.txt','w')
    textfilevar.close()
    print('I created the file, try again')