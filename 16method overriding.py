

class User:
    def __init__(self):
        self.type="generalUser"
        print(f"{self.type} is user type")

    def acessDashboard(self):
        print("Welcome to our site...")

class Admin(User):
    def __init__(self):
        self.type="AdminUser"
        print(f"{self.type} is user type")

    def acessDashboard(self):
        print("Welcome to our site...")

a=Admin()
a.acessDashboard()
b=User()
b.acessDashboard()