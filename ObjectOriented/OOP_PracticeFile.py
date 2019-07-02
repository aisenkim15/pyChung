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
class Car2():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
"""





