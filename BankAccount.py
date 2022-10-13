# BankAccount.py

#은행의 계정을 표현한 클래스
# 아무거도 없어도 Object상속받는거임 BankAccount(Object) 
class BankAccount:
    def __init__(self, id, name, balance):
        #변수이름숨김(__*)
        self.__id = id
        self.__name = name 
        self.__balance = balance
    #입금 
    def deposit(self, amount):
        self.__balance += amount 
    #출금
    def withdraw(self, amount):
        self.__balance -= amount
    #결과 출력
    def __str__(self):
        return "{0}, {1}, {2}".format(self.__id, 
        self.__name, self.__balance)

#인스턴스 객체를 생성
account1 = BankAccount(100, "전우치", 15000)
account1.withdraw(3000)


print(account1)
##백도어(테스드
print(account1._BankAccount__name)



