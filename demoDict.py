# demoDict.py
device = {"아이폰":5, "아이패드":10, "윈도우":20}
print (type(device))
print( len(device))
print(device["아이폰"])
device["맥북"]=15
print(device)
device["아이폰"]=6
print(device)
del device["아이패드"]
print(device)

print("---list-----")
for item in device.items():
    print(item)

print("---?---")
for k,v in device.items():
    print(k,v)

print("-----key------")
for key in device.keys():
    print(key)

print("----value-----")
for value in device.values():
    print(value)

phone = {"kim":"1111", "lee":"2222"}
print (phone.keys())
print (phone.values())
print("kim" in phone)
print("park" in phone)
print("park" not in phone)

# 참조를 복사(pass by reference, call by reference)
p=phone
print(p)
p["kang"]="1234"
print(phone)
print(p)
# id 는 주소 비슷한 개념으로, 객체의 값을 찍어 같은값이면 같은 객체, 다른값이면 다른 객체
print(id(phone), id(p))


# <, >, <=, >= (bool 참/거짓), !=, == (=의 경우 대입하는 것)
print("----논리식 출력---")
print(1<2)
print(1 !=2)
print(1==2)

#and(~이면서, ~이고), or(~이거나)
print(True and True and True)
print(True and True and False)
print(True or False or False)

# bool type 이란 어떤 조건 식이 있는데 맞아 틀려 물어보는 형식

# 숫자는 0이면 거짓, 0이 아니면 참
# 문자의 경우 없으면 거짓, 문자가 있으면 참 
# list경우 비워 있으면 거짓, 문자열이 있으면 참
# None 는 값이 없는 상태를 나타내고 이또한 거짓

print("---bool()---")
print(bool(0))
print(bool(3))
print(bool(""))
print(bool("demo"))
print(bool([]))
print(bool([1,2,3]))
a=[1,2,3]
a=None 
b=3
print(a)
print(bool(a))
print(bool(b))

a=[1,2,3]
b=a
a[0]=38
print(a)
print(b)
print(id(a), id(b))
# copy본 만들기 [:]
c=a[:]
a[0]=1
print(a)
print(b)
print(c)
print(id(a), id(b), id(c))

#list가 아닌경우에도 상요할수 있는 copy만들기
a=[1,2,3]
import copy
b=copy.deepcopy(a)
a[0]=38
print(a)
print(b)



