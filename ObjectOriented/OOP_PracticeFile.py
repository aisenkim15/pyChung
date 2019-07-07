"""
class Car:
    def powerOn(self):
        print("Engine starting~~!")
        self.power = True
        self.drive()

    def drive(self):
        print("Driving~~!")


bmw = Car()
bmw.powerOn()

car1_model = "BMW"
car1_power = False  # 시동 on Off 변수
car1_max_speed = 200

car2_model = "Sonata"
car2_power = True  # 시동 on Off 변수
car2_max_speed = 180


def drive_car(model, power, max_speed, speed):
    print("{} 주행준비..".format(model))

    if power == False:
        print("주행불가: 시동을 켜")
        return

    if speed > max_speed:
        print("{]의 최고속도는 {}. 속도를 줄입니다".format(model, max_speed))
        speed = max_speed

    print("{}km로 주행합니다. 출발".format(speed))


drive_car(car1_model, car1_power, car1_max_speed, 170)
"""

"""
class Car2():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
"""

# Problem ~~~~~~!!!!!!
"""
class Student:
    def __init__(self, name, age, phone, sub):
        self.sub = sub

    def print_info(self):
        print("Name: {}\nAge: {}\nPhoneNum: {}\n".format(self.name, self.age, self.phone))

    def study(self):
        print("{} 님이 {} 공부를 시작합니다".format(self.name, self.sub))


        self.name = name
        self.age = age
        self.phone = phone
student1 = Student("John", "23", "010-2342-2323", "C++") 
student2 = Student("Marry", "21", "010-3433-0000", "Java")
student3 = Student("Bob", "43", "010-0000-9999", "Python")

student1.print_info()
student2.print_info()
student3.print_info()
"""

# using "DetailedPersonModule" and "Person_Module
"""
from Person_Module import person
from DetailedPersonModule import Student, Teacher

student1 = Student("James", "23")
teacher1 = Teacher("Teacher1", "34")

print(student1.study())
print(teacher1.name)
"""
"""
from abc import *

class Animal(metaclass= ABCMeta):
    @abstractmethod
    def Cry(self):
        pass

class Dog(Animal):
    def Cry(self):
        print("냐옹")
"""

class Calc:

    def __init__(self):
        add_count = 0
        min_count = 0
        mul_count = 0
        div_count = 0

    def add(self, num1, num2):
        print("{} + {} = {}". format(num1, num2, num1+num2))
        self.add_count += 1

    def subtract(self, num1, num2):
        print("{} - {} = {}". format(num1, num2, num1-num2))
        self.min_count += 1

    def multiply(self, num1, num2):
        print("{} * {} = {}". format(num1, num2, num1*num2))
        self.mul_count += 1

    def divide(self, num1, num2):
        print("{} / {} = {}". format(num1, num2, num1/num2))
        self.div_count += 1

    def print_infro(self):
        print("add: ", self.add_count)
        print("subtract: ", self.sub_count)
        print("multiply: ", self.mul_count)
        print("divide: ", self.div_count)

newCalc = Calc()
newCalc.add(2,3)
newCalc.subtract(9,2)