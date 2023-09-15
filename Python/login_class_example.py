# Login Class

# the idea of 'self'

# better attribute assignation

class Login:

    username = "user1"
    password = "pawssord"
    server = "server.com"

    def login(self):
        print("You have logged in to: ", self.server, "as: ", self.username )

    def emailcheck(self):
        print("You got mail in: ", self.server)

gmail = Login()
gmail.username = "leon"
gmail.server = "gmail.com"


hotmail = Login()
hotmail.username = "bowtieguy2023"
yahoo = Login()
yahoo.server = "yahoo.co.uk"



print(yahoo.emailcheck())
print(gmail.emailcheck())
