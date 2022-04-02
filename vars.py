class User:
    active_users = []

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def activate (self):
        if not self.is_active():
            self.__class__.active_users.append(self)
           
    
    def deactivate (self):
        if self.is_active():
            self.__class__.active_users.remove(self)

    def is_active(self):
        return self in self.__class__.active_users


me = User ("Simon", "simoncordovax@gmail.com")
me.name ="Simon Cordova"
print(me.name)

print(f"Active Users: {User.active_users}")
me.activate()
me.activate()

print(f"Active Users: {User.active_users}")

me.deactivate()

print(f"Active Users: {User.active_users}")

print(f"Active users off of me: {me.active_users}, Class Level: {User.active_users}")
me.active_users = "Just me"
print(f"Active users off of me: {me.active_users}, Class Level: {User.active_users}")