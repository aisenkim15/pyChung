class person:
    def __init__(self, name, age):
        print("person 생성자")
        self.name = name
        self.age = age

    def printInfo(self):
        print("Person, print info")
        print("Name: ", self.name)
        print("Age: ", self.age)

    def sleep(self):
        print("Person, sleep")
        print(self.name + "님은 8시간 잡니다.")