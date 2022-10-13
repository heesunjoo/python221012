# -*- 생성자와 소멸자 그리고 참조 카운트 관리  -*-
class MyClass:
    def __init__(self, value):
        self.value = value
        print("Instance is created! Value = ", value)
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성 
d = MyClass(10)
del d
##del d 는 애초에 자동으로 메모리를 없애주기 때문에 필요없다.   


print ("---전체 코드 실행 종료")
