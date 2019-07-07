from Person_Module import person
# 자식클래스


class Student(person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def study(self):
        print("Student, study")
        print(self.name + "학생은 6시간 공부합니다")

    def sleep(self):
        print("Student, sleep")
        print(self.name + "학생은 6시간 잡니다")

#자식클래스2


class Teacher(person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def grade(self):
        print("Teacher Grade")
        print(self.name + "선생님 is grading ")
