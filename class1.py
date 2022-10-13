# class1.py
#1) 클래스 형식 정의
class Person:
    #클래스 멤버 변수
    num_person=0
    #초기화 메서드(가장먼저실행)
    def __init__(self):
        self.name="default name"
        self.num=0
        self.num+=1
        Person.num_person +=1
    def print(self):
        print("My name is {0}" .format(self.name))
        print("My name is {0}" .format(self.num))

#2) 인스턴스 생성
p1 = Person()
p2 = Person()
p3 = Person()
print("숫자:{0}" .format(p1.num))
print("숫자:{0}" .format(Person.num_person))
p1.name = "전우치"
#3)메서드 호출
p1.print()
p2.print()

#동적인 형식(코드가 실행중-런타임)이라 변수 추가 가능
#p1 인스턴스 title 없으면 class title로 간다
Person.title="NN"
print (p1.title)
print (p2.title)
print ( Person.title)


