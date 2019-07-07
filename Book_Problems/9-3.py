class Users:
    def __init__(self, first_name, last_name, birthDay):
        self.first_name = first_name
        self.last_name = last_name
        self.birthDay = birthDay

    def describe_user(self):
        print("First Name: {}\n Last Name: {}\n Birthday: {}".format(self.first_name, self.last_name, self.birthDay))
        self.greet_user()

    def greet_user(self):
        print("Welcome User {}".format(self.last_name))

user1 = Users("ChungHyun", "Kim", "May 25th")
user1.describe_user()

