# Login Class

# the idea of 'self'

# better attribute assignation

class Login:


    def __init__(self,passeduser,passedpw,passedserver):
        self.username = passeduser
        self.password = passedpw
        self.server = passedserver

    def login(self):
        print("You have logged in to: ", self.server, "as: ", self.username )

    def emailcheck(self):
        self.login()
        return "You got mail in: " + self.server 

    def privacyviolation(self,otheraccount):
        otheraccountdata = [otheraccount.username,otheraccount.password,otheraccount.server]
        otheraccount.login()
        return otheraccountdata


gmail = Login("leon","password123","gmail.com")
hotmail = Login("lr","np8954n6vp954456vpy79n","hotmail.com")
yahoo = Login("bowtieguy2001","1234","yahoo.com")

print(yahoo.emailcheck())  # running the function in the copies from the class
print(gmail.emailcheck())

print(yahoo)    # print the 'id' of the class, they will be unique
print(gmail)
print(hotmail)

print(gmail.privacyviolation(yahoo))
gmail.privacyviolation(yahoo)