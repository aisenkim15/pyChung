class Users:
    def __init__(self, first_name, last_name, birthDay):
        self.first_name = first_name
        self.last_name = last_name
        self.birthDay = birthDay
        self.login_attempt = 0

    def describe_user(self):
        print("First Name: {}\n Last Name: {}\n Birthday: {}".format(self.first_name, self.last_name, self.birthDay))
        self.greet_user()

    def greet_user(self):
        print("Welcome User {}".format(self.last_name))

    def increment_login_attempt(self):
        self.login_attempt += 1

    def reset_login_attempt(self):
        self.login_attempt = 0


user1 = Users("ChungHyun", "Kim", "May 25th")
for i in range(5):
    user1.increment_login_attempt()
print(user1.login_attempt)
user1.reset_login_attempt()
print(user1.login_attempt)



