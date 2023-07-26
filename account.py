

class Account():
    def __init__(self, username, password, email, site) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.site = site

    def setUsername(self, new_name):
        self.username = new_name

    def setPassword(self, new_pass):
        self.password = new_pass
    
    def setEmail(self, new_email):
        self.email = new_email

    def setSite(self, new_site):
        self.site = new_site