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


#불변 가변형식
print("---불변형식---")
a=1.2
print(id(a))
a=2.3
print(id(a))

print("---가변형식---")
lst=[1,2,3]
print(id(lst))
lst.append(4)
print(id(lst))

print("---global---")

g=1
def testScope(a):
    #전역변수를 맵핑해주면 불변도 바꿔줄수있다
    #global g
    g = 2
    return g+a

#호출
testScope(1)
print(testScope(1))
print("함수호출 후 g:{0}" .format(g))

print("---기본값---")
def times(a=10, b=20):
    return a*b

#호출
print(times())
print(times(5))
print(times(5,6))

