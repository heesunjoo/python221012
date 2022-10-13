# 클래스메서드.py
# 상속의 대상
class CoeffVar(object):
    coefficient = 1 
    #데코레이터(살아있는 주석)
    @classmethod 
    #self 는 인스턴스를 나타내는 말이지만cls 는 class
    def mul(cls, fact):
        return cls.coefficient * fact 

#파생형식을 정의
class MulFive(CoeffVar):
    coefficient = 5 

x = MulFive.mul(4)
print(x)


