# 12_OOP.py

'''
    [Object Oriented Programming] - 객체지향 프로그래밍
        - 객체지향이론
            실제 세계는 사물(객체)로 이루어져 있으면,
            발생하는 모든 사건들은 사물간의 상호작용이다.

            이 개념을 토대로 프로그래밍 언어 접목 -> 객체지향 프로그래밍

        - 특징
            1. 코드의 재사용성이 높다. (함수 배울 때, 높은 재사용성)
            2. 코드를 관리하기 좋다. (편하다.)
            3. 프로그램의 신뢰성이 높아진다.

        - '클래스'와 '객체'
            1. 클래스는 일종의 설계도(또는 틀)이며, 객체는 그 설계도를 통해 만들어진 실제 사물
                갤럭시s10 설계도 --> 갤럭시s10 1, 2, 3, 4, 5, ....

            2. 클래스(class)
                정의 : 객체(사물)를 정의해 놓은 것 (어떠한 객체를 만들 것인지)
                용도 : 객체를 생성

            3. 객체 (object)
                정의 : 실제로 존재하는 것 (사물 같은)
                용도 : 클래스에 정의된 대로 사용한다.

        - 객체 / 인스턴스
            1. 인스턴스(instance) : 사례, 경우, 실체
                - 기본적으로는 객체와 같은 의미
                - 문장에서 쓰임에 따라 구분한다.
                    클래스를 통해 실제로 만들어진 객체를 '인스턴스'라고 한다.

                    갤럭시s10 -> 객체
                    갤럭시s10 설계도 -> 클래스 -> 객체를 만들 수 있다.
                    내가 가지고 있는 갤럭시s10은 인스턴스이다.

            - 객체의 구성 요소 : 속성, 기능
                (속성 : 갤럭시s10의 색상 등.. / 기능 : 갤럭시s10의 카메라 등..)

                1. 객체는 클래스에서 정의한 다수의 속성과 기능을 가질 수 있다.
                2. 속성 = 변수
                3. 기능 = 함수

            - 클래스를 비유할 때
                붕어빵 틀(클래스) / 만들어진 붕어빵(객체)
                자동차 공장(클래스) / 출고된 자동차 (객체)

'''
'''
    1. 클래스(설계도/틀)는 속성(변수)을 정의하거나, 기능(함수)을 정의할 수 있다.
        > 함수와 마찬가지로 클래스도 작성해놓기만하면 프로그램 수행에 영향이 없다.
        > 객체(인스턴스)를 생성한 뒤부터 클래스에 작성된 코드가 효력이 발생할 수 있다.

    2. 클래스 안에 정의(def)된 함수는 '메서드(method)'라고도 부른다.
        > 메서드를 만들 때는 반드시 최소 하나의 매개변수가 필요하다.
        > 나 자기 자신을 의미하는 self라는 이름으로 한다.
          (꼭 self가 아니어도 된다.)

'''

class Car: # 자동차 설계도 작성
    def power_on(self): # def power_on(bmw):
        print("부릉부릉!")
        self.power = True # bmw.power = True
        # bmw 인스턴스에 power라는 변수(속성)가 추가 됐다. (변수 생성 코드)
        self.drive() # bmw.drive() 

    def drive(self):
        print("주행시작!")
                
# 인스턴스 생성
bmw = Car()  # 변수명 = 클래스명() --> Car 클래스의 객체(인스턴스) 생성
# ~~~ 관련 함수 --> 문자열.함수(), 리스트.함수()
bmw.power_on() # 클래스에 정의된 함수 호출
print("bmw의 시동 여부 :", bmw.power)

# 클래스에 여러 속성/기능을 정의 해두고, 인스턴스(객체)라는 하나의 단위로 묶어서 다루겠다.

tico = Car() # 위에 있는 bmw와는 별개의 새로운 인스턴스가 생성
tico.drive()
tico.power = "시동켜짐"
print("tico의 시동 여부 :", tico.power) # 오류! tico는 power 변수를 만드는 코드가 없다.

tico.model = "TICO의 최신모델" # tico는 model 변수를 추가했다.
print(tico.model)
#print(bmw.model) #  오류, bmw인스턴스에 model변수가 있다치고 출력하려고 함.

# python 객체의 특징 : 만들어지는 인스턴스별로 속성(변수)이 다를 수 있다. 


# 1. 클래스를 사용하는 이유 ?

# 클래스 없이 자동차 2대를 다뤄보기
car1_model = "BMW"  # 모델명 변수
car1_power = False  # 시동 on/off 변수
car1_max_speed = 200 # 자동차 최고 속도

car2_model = "SONATA" # 모델명 변수
car2_power = True  # 시동 on/off 변수
car2_max_speed = 180 # 자동차 최고 속도

# 자동차가 주행하는 함수
def drive_car(model, power, max_speed, speed): # speed = 주행하고 싶은 속도
    print("{} 주행준비..".format(model))

    if power == False :
        print("주행불가 : 시동을 켜주세요.")
        return

    if speed > max_speed :
        print("{}의 최고속도는 {}km입니다. 속도를 줄입니다.".format(model, max_speed))
        speed = max_speed # 원래의 speed 변수에 최고속도 값을 대입

    print("{}km로 주행합니다. 출발 ~~".format(speed))

print()
drive_car(car1_model, car1_power, car1_max_speed, 150) # 자동차1을 150으로 주행
#           "BMW"       False          200        150
print()
drive_car(car2_model, car2_power, car2_max_speed, 200) # 자동차2를 200으로 주행
#           "SONATA"    True        180           200 
    
# 1) 각 변수들은 서로 전~혀 연관성이 없다. (변수명만 그냥 비슷하게 지었을 뿐)
# 2) 함수를 호출할 때, 일일이 매개변수로 모든 값을 전달해줘야 한다. (귀찮다.)

# 2. 클래스의 사용(1)
# 하나의 틀을 만들고, 그 틀로 자동차를 생성한다.
class Car:
    def drive_car(self, speed): # speed = 주행하고 싶은 속도
        print("{} 주행준비..".format(self.model))

        if self.power == False :
            print("주행불가 : 시동을 켜주세요.")
            return

        if speed > self.max_speed:
            print("{}의 최고속도는 {}km입니다. 속도를 줄입니다.".format(self.model, self.max_speed))
            speed = self.max_speed

        print("{}km로 주행합니다. 출발~~".format(speed))

car1 = Car()
car2 = Car()

car1.model = "BMW"
car1.power = False
car1.max_speed = 200

car2.model = "SONATA"
car2.power = True
car2.max_speed = 180
print()
car1.drive_car(150)
print()
car2.drive_car(200)

# drive_car 호출 시, 정의된 매개변수는 2개(self, speed)이다.
# self에는 자동으로 호출하는 인스턴스가 대입 
# 그 뒤 매개변수부터는 호출할 때 값을 전달해야한다.

# 1) 인스턴스라는 하나의 변수에 모든 속성들을 담아놨다. 연관성이 생김 
# 2) 함수(메서드)를 호출할 때 그냥 호출해도 self에는 인스턴스가 대입되기 때문에
#    함수의 수행문 안에서 self.~~ 호출한 인스턴스의 속성들을 사용할 수 있다. 

# 3. 클래스의 사용 (2) - 생성자
# 생성자
#   1. 인스턴스 생성 시 자동으로 호출되는 메서드(함수) -- 무조건 호출
#   2. 목적 : 인스턴스 생성과 동시에 속성을 추가/초기값 지정을 하고 싶을 때 사용(초기화)
#   3. 생성자 함수의 이름 : __init__
print()
class Car:
    def __init__(self, model) :
        print("생성자 호출!")
        self.model = model

car1 = Car("BMW")
# 인스턴스를 생성하는 코드 --> 알고보니 생성자함수를 호출하는 코드
# 생성자 함수가 호출되고나서 인스턴스가 만들어진다.
car2 = Car("SONATA")
print("car1 모델 :", car1.model)
print("car2 모델 :", car2.model)
# 생성자 함수를 이용하면, 모든 인스턴스가 공통적으로 지녀야할 속성(변수)을 만들 수 있다.
# 왜? 인스턴스 생성 시 무조건 호출되는 생성자 함수니까
print()
# 4. 클래스의 사용 (3) - 생성자를 활용
class Car:
    def __init__(self, model, power, max_speed):
        print("[{}] 인스턴스가 생성됩니다.".format(model))
        self.model = model # 내 인스턴스에 model 속성을 생성하며 매개변수로 받은 model 값을 대입 
        self.power = power
        self.max_speed = max_speed

    def drive_car(self, speed):
        print("{} 주행 준비..".format(self.model))

        if self.power == False:
            print("주행불가 : 시동을 켜주세요.")
            return

        if speed > self.max_speed :
            print("{}의 최고속도는 {}km입니다. 속도를 줄입니다.".format(self.model, self.max_speed))
            speed = self.max_speed

        print("{}km로 주행합니다. 출발~~".format(speed))
        
car1 = Car("BMW", False, 200)
car2 = Car("SONATA", True, 180)

car1.drive_car(150)
print()
car2.drive_car(200)












































































            
