class User:
    def __init__(self):
        self.username = ""
    def setUsername(self, username):
        self.username = username
    def getUsername(self):
        return self.username
    
# untuk digunakan di success register dan diforgot password
users = User()