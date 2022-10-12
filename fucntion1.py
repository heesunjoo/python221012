# fucntion1.py

#1)함수를 정의
def setvalue(newValue):
    x=newValue
    print("함수내부:{0}".format(x))
#2) 함수 호출
retValue=setvalue(5)
print(retValue)

#함수정의
def swap(x,y):
    return y,x

# 호출
result =list(swap(3,4))
print(result)
