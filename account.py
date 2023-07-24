

class Account():
    def __init__(self, username, password, email, appname) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.appname = appname

    def setUsername(self, new_name):
        self.username = new_name

    def setPassword(self, new_pass):
        self.password = new_pass
    
    def setEmail(self, new_email):
        self.email = new_email
