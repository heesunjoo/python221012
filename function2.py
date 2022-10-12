# function2.py
#교집합 문자를 리스트로 리턴
from re import X


def intersect(prelist, postlist):
    #지역변수 리스트로 초기화
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print (intersect("HAM", "SPAM"))

print("---지역변수, 전역변수---")
#전역변수
x=5
def func1(a):
    return a+x

#호출
print(func1(1))

def func2(a):
    #지역변수
    x=2
    return a+x


#호출
print (func2(1))


#참조를 전달하는 방식
wordlist = [ "J", "A", "M"]
def change(x):
    x[0] = "H"

def change2(x):
    x[1] = "M"

#호출
change(wordlist)
print(wordlist)
print("함수호출후:{0}" .format(wordlist))
change2(wordlist)
print(wordlist)
print("함수2호출: {0}". format(wordlist))

#복사본 사용
wordlist = ["J", "A", "M"]

def change(x):
    x1 = x[:]
    x1[0] = "H"
    print("함수 내부:{0}" .format(x1))

#호출
change(wordlist)
print("---------")
print("함수 호출후:{0}".format(wordlist))