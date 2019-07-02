# 10_file_io.py 

# 파이썬 언어로 컴퓨터에 존재하는 실제 파일을 다루는 방법

'''
    [파일 입출력] - file input/output
        - 실제 파일 생성/삭제/쓰기/읽기 등의 행위 ..

        - 파일의 이해
            디렉토리(Directory)
                > 폴더 또는 디렉토리라고 부른다.
                > 폴더 안에는 파일과 또 다른 폴더를 포함할 수 있다.
                > 용량이 없다.
                > 폴더 안으로 들어가는 일 밖에 못함(실행 개념 없음)

            파일 (File)
                > 컴퓨터에서 정보(data)를 저장하는 논리적인 단위
                > 파일은 실제 물리 disk(HDD, SSD)에 저장이 되고, 용량이 존재
                    >> 파일명.확장자 (파일전체이름에서 맨 오른쪽 . 기준으로 확장자)
                    >> test.txt.xlsx --> 엑셀파일
                > 실행, 쓰기, 읽기 등을 할 수 있다.

                > 기본적으로 모든 파일은 메모장으로 열 수 있다.
                  우리가 파이썬으로 소스파일 다루는 것도, 메모장으로 열어서 수정해도 된다.

                      단, 파이썬 편집기는 '코드 실행' 기능이 있고, 메모장은 없다.

                - Binary 파일
                    > 메모장으로 열었을 때, 알아볼 수 없다. (내용이 깨져보임)
                    > 확장자에 맞는 전용 프로그램으로 열어야 알아볼 수 있다.
                        >> 엑셀(xlsx), 워드(docx), 한글(hwp)...
                        
                - Text 파일
                    > 메모장으로 열었을 때, 우리가 알아볼 수 있는 파일
                        >> txt, py, html, xml, c 등등..


    [파일 다루는 기본 구조]
    파일객체 = open("파일이름", "파일 열기 모드")

        파일객체 : 변수와 비슷하다. (그냥 변수라고 생각)
        파일이름 : 컴퓨터에 존재하는 파일명
        파일 열기 모드 : 열었을 때, 어떤 행위를 할 것인지 미리 모드를 결정
            r   : 읽기모드 (read)
            w   : 쓰기모드 (write)
            a   : 추가모드 (add)
'''

print("[파일 입출력]")

# 파일의 절대 경로 : 드라이브문자를 포함하여, 전체 경로를 작성
# Windows 운영체제에서는 드라이브문자를 사용 -> 드라이브문자명: --> ex) C:, D:
# D드라이브의 테스트 폴더의 test.txt --> D:\\테스트\\test.txt
# 상대 경로 : 실행된 프로그램 실행파일 위치가 기준

# 파일 읽기

file = open("C:\\test.txt", "r") # 절대경로 사용

# read() : 파일의 전체 내용을 '문자열'로 반환
text = file.read()
print(text)
# 사용을 다 한 파일은 열었기 때문에 반드시 닫아줘야 한다.
# 닫지 않으면, 프로그램이 계속 사용 중이기 때문에, 다른 곳에서 파일을 다룰 수 없다. 
file.close()
print()

# with 를 이용하여 close() 생략하기
with open("C:\\test.txt", "r") as file : # open한 파일을 file 변수로 다루겠다.
    text = file.read()
    print(text)

# close를 생략해도 with 문법 안에서 자동으로 close해준다.
print()

# 파일 내용을 한 줄 씩 읽기(1)
# readlines() : 한 줄 씩 문자열로 나눠서 리스트 반환 (개행\n포함)

with open("C:\\test.txt", "r") as file :
    text = file.readlines()
    print(text)
    
# 파일 내용을 한 줄 씩 읽기 (2)
# readline() : 한 줄을 문자열로 읽기 (\n 포함)
with open("C:\\test.txt", "r") as file:
    text = file.readline()
    print(text) # print의 end='\n'에 의해 개행이 2번 된다.



# readline() 으로 파일 전체 읽기
with open("C:\\test.txt", "r") as file:
    while True: # 무한 반복 
        text = file.readline()
        if not text :
            break
        print(text, end='')
    
# 다음 줄을 읽어라! 라는 명령을 따로 하지 않았는데 자동으로 다음 줄이 읽어졌다.
# 프로그래밍언어에서 file을 다룰 때 공통
# > 한 번 읽거나, 쓰고 나면 자동으로 그 다음위치로 이동 (offset)

# 통계 산출(파일의 단어 개수, 라인 수)

with open("C:\\test.txt", "r") as file :
    text = file.read()   # 파일의 전체 내용 읽기 
    word_list = text.split() # 공백 기준으로 문자를 나눠서 단어라는 개념으로 쓰겠다. 
    line_list = text.split("\n") # 개행 기준으로 라인 개념으로 쓰겠다.

print(line_list)
print("라인 수 :", len(line_list))
print("단어 수 :", len(word_list))



# 읽은 파일을 for문에 대입하기
with open("C:\\test.txt", "r") as file:
    for line in file : # 한 줄씩 대입 된다. 
        print(line, end='')

# 파일 쓰기
# 파일이 없으면 새로 생성, 있으면 지우고 새로 만든다.
with open("C:\\test.txt", "w") as file:
    for i in range(1, 11): # i에 1 ~ 10까지 대입되며 반복
        text = "{}번째 줄입니다.\n".format(i)
        file.write(text)
        





















































































                
