# 09_function.py

'''
    [함수 function]   (method 메서드 : 같은말)
        - 특정 작업을 수행하는 일련의 문장들을 하나로 묶은 것

        - 함수의 장점 (사용하는 이유)
            1. 한 번 만들어 놓으면 언제든지 재사용 가능
            2. 중복된 코드 제거
            3. 프로그램의 구조화
                > 작업 단위로 코드를 묶어서 구조화 시킨다.

    [함수의 기본 구조]
    def 함수이름(매개변수) :    def = define 정의하다.
        수행문
        return 변환 값(또는 결과 값)

    1. 매개변수 (parameter)
        - 함수가 호출될 때 값을 받을 '변수'
        - 개수 제한이 없고, 필요 없으면 생략도 가능
        - 우리가 함수를 호출할 때 전달하는 '값'을 인수라고 부른다.
            > argument


   2. 반환 값(결과 값)
       - return 뒤에 오는 값은, 함수의 수행이 완료되고 되돌려주는 값
       - return 을 사용하면 함수의 수행이 끝난다.
           > 마치 반복문에서 break를 사용한 것과 느낌이 비슷

    >>> 매개변수와 반환 값의 유/무에 따른 함수 형태 (4가지)
        1. 매개변수와 반환 값 둘 다 있다.
        2. 매개변수와 반환 값 둘 다 없다.
        3. 매개변수만 있다.
        4. 반환 값만 있다. 
            
'''
print("[함수]")

# 함수는 define (정의) 하기만 하면 프로그램 수행에 영향이 없다.
# 함수를 정의한다 = 이 후 이 함수를 언제든 사용할 수 있도록 준비

def f(x) :
    return x + 5

result = f(10)
print("결과 :", result)
print()
print("[함수의 4가지 형태]")
# 1. 매개변수, 반환 값 둘 다 있을 경우
def add(a, b):
    return a + b

# add함수는 매개변수가 2개 -> 사용하려면 값을 2개 전달해줘야 한다. 
result = add(1, 2) # 함수 호출 (1) 
print("{} + {} = {}".format(1, 2, result))
print("{} + {} = {}".format(3, 4, add(3, 4))) # 함수 호출 (2)
# 반환 값이 있는 함수를 호출 했을 때는
# 함수의 기능 수행이 끝난 뒤 반환 값을 들고 온다.
# (1) add(1, 2)는 함수의 반환 값인 3으로 대체되고 변수에 대입한다.
# (2) add(3, 4)는 7로 대체되고 format()함수에서 사용된다.

# 2. 매개변수, 반환 값 둘 다 없을 경우
def sayHo():
    print("Ho~~")
    print("Ho!!")

# 함수를 호출하면, 코드의 흐름이 내가 호출한 함수의 수행문으로 점프
# 함수의 수행문이 끝나면, 함수를 호출했던 원래 위치로 되돌아온다.
# 단, return 반환 값이 있다면 그 값을 들고 온다.
print("sayHo() 호출 전")
sayHo()
print("sayHo() 호출 후")
print()

# 매개변수에 따라 함수를 '호출'할 때는 그 규칙을 맞춰줘야 한다.
# '반환 값'에 따라서는 규칙을 맞추지 않아도 사용은 가능하다.
# 반환 값이 있다 = 그 값을 변수에 대입, 그 값을 어딘가에 바로 사용
result = sayHo()
print("sayHo()의 결과 값1 :", result)
print()
print("sayHo()의 결과 값2 :", sayHo())
# 반환 값이 없는 함수는 그냥 호출만 하기
# 변수에 대입하거나 어딘가에 사용을 하면 None이라는 값이다.
print()

# 3. 매개변수만 있다.
def say(talk):
    print(talk)

say("hohoho")
print()

# 4. 반환 값만 있다.
def getHo():
    return "ho! ho! ho!"

ho = getHo()
print(ho)
print(getHo())

# return 뒤에 오는 값의 자료형에 따라 반환된 결과도 그 자료형이 된다.

# ====================================================================================================

# 여러 값 반환하기
print("[여러 개의 값 반환]")
def calc(a, b):
    return a+b, a-b, a*b, a/b # 여러 개처럼 보이지만, '튜플'

# d = 1, 2, 3 --> 튜플 () 생략 가능
print(calc(10, 3))
a, b, c, d = calc(10, 3) # 튜플 4개 요소를 각각 변수에 하나씩 대입 
print(a, b, c, d)
print()

# 매개변수에 초기 값 사용

# 이름, 나이, 전화번호를 매개변수로 전달받고 출력 
def print_info(name, age, phone="010-xxxx-xxxx"):
    print("이름 :", name)
    print("나이 :", age)
    print("전화번호 :", phone)
    
print_info("홍길동", 20, "010-1111-2222")
print_info("임꺽정", 30, "010-2222-2222")
print_info("성춘향", 17)
# 3번째 매개변수(초기 값 사용)에 값을 주면, 내가 준 값
# 값을 안 주면, 초기 값
#print() 함수의 sep=' ', end='\n' 은 초기값이 적용된 매개변수

# 매개변수에 초기 값을 적용하려면, 초기 값이 들어가는 매개변수는 맨 뒤에 위치해야 한다.
#def func(a, b="hi", c):
#    print("test")
    
print()

# 키워드 인수 : 함수의 매개변수명을 키워드로 사용
def print_info(name, age, phone):
    print("이름 :", name)
    print("나이 :", age)
    print("전화번호 :", phone)

print_info("홍길동", 20, "010~~~")
print_info(age=19, name="임꺽정", phone=112)
print(1, 2, 3, sep='zz')
# print() 함수 호출 시 sep나 end에 값을 넣는 행위 (키워드 인수)
print()

# 가변인수 : 전달하는 값의 개수가 변할 수 있다.
# 함수를 만드는 입장에서 변할 수 있는 값들을 처리
def add(*args) : # arguments : 인수들
    print(args) # * 떼면 튜플이다.
    add_result = 0
    for i in args :
        add_result += i

    return add_result

print(add(1, 2, 3, 4, 5, 6, 7, 8))
print(add(1, 2))
print(add(1, 2, 3))
# print() 함수도 값을 몇 개 전달하더라도 다 출력된다.
# 일반 매개변수, 가변인수를 혼용할 때, 가변인수는 마지막에 위치
'''
def func(*args, a):
    print(args)
    print(a)
    
func(1, 2, 3, 4, 5, 6)
'''
# 초기값이 지정된 매개변수나, 가변인수는 뒤에 !!
# > 두 개 같이 쓰지 않는다.
def func(*args, sep=' ', end='\n'):
    for i in args:
        print(i)
func(1,2,3,4, sep='', end='')

print()



def func3(num3): # 9
    print("func3() 시작") # 10
    print("num3 =",num3)
    print("func3() 끝") # 11

def func2(num2): # 6
    print("func2() 시작") # 7
    print("num2 =",num2)
    func3(num2 - 1) # 8, 12
    print("num2 =",num2)
    print("func2() 끝") # 13

def func1(num1):# 3
    print("func1() 시작") # 4
    print("num1 =",num1)
    func2(num1 - 1)# 5, 14
    print("num1 =",num1)
    print("func1() 끝")# 15

print("func1() 호출 전") # 1
func1(3) # 2, 16
print("func1() 호출 후") # 17

'''
재귀함수 
    - 함수의 수행문 안에서 나 자기 자신 함수를 다시 호출하는 함수
    - 수행문이 반복되기 때문에 반복문과 유사한 성격
    - 너무 많이 반복 수행하다보면 프로그램 오류 발생
    - 함수 호출 시 'stack' 이라는 구조의 메모리를 사용
        Queue : First In, First Out (FIFO) - 입구/출구 따로
        Stack : First In, Last Out (FILO) - 출입구 하나 
            > Stack 용량이 초과될 정도로 많이 호출하면 오류!
            > StackOverflow 오류라고 한다.
                >> 함수 수행이 끝난 후 돌아갈 위치를 저장
    - 재귀함수도 반복문처럼 반복 호출이 끝날 수 있는 조건이 필요 

'''
print()
def func(num) :
    print("func() 시작, num =", num)
    if num == 1:
        print("num이 1일때부터 끝!")
        return # 함수에서 반환 값없이 return 만 쓰면 함수 끝 

    func(num - 1) # 내 함수를 다시 호출 = 재귀호출! (재귀호출이 있으면 재귀함수)
    print("func() 끝, num =", num)

func(3)

print()

# 지역변수와 전역변수
# 지역변수 : 특정 지역에서만 사용가능한 변수
# 전역변수 : 전체 영역에서 사용가능한 변수
#       > 우리는 여태 '전역변수'만 사용했다.

value = "전역변수" # 어느 수행문에도 속하지 않는 위치
                  # 만들어진 뒤부터 어디서든 사용 가능

def func1() :
    print("func1() 호출!")
    print(value) # 전역변수는 어디서든 접근 가능

def func2() :
    print("func2() 호출!")
    value_func2 = "func2()의 지역변수!"
    print(value_func2)

    # value 라는 전역변수가 이미 있는데 지역에서 value에 값을 대입하게 되면
    # 전역변수 value의 값이 변경되는게 아니라 같은 이름으로 이 지역의 value 지역변수가 생성
    value = "지역변수로 변경!"
    print(value)

def func3() :
    print("func3() 호출!")
    global value_func3 # 지역변수를 전역변수로 만드는 명령 
    value_func3 = "func3()의 지역변수"
    
func1()
func2()
#print(value_func2) # 오류! func2에만 존재하는 지역변수 
print(value)
func3() 
print(value_func3) # func3()에서 만들어준 전역변수
# 단, func3()이 호출되어야 value_func3 변수가 만들어진다.


























    
