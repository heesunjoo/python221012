# demoLoop.py
value = 5
while value > 0:
    print(value)
    value -=1


print("--- for in ---")
d= {100:"apple", 200:"kiwi"}

print(len(d))

for k,v  in d.items():
    print(k,v)

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

lst = [100, "apple", 3.14]
print(len(lst))
for item in lst:
    print(item, type(item))

##구구단 출력
for i in [2,3,4,5,6]:
    print("----{0}단---".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2} " .format(i,j,i*j))


print("----break구문----")
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i>5:
        break
    print ("item:{0}" .format(i))

print("----continue구문----")
for i in lst:
    if i%2==1:
        continue
    print("item:{0}" .format(i))

print("삼각형그리기")
for i in lst:
    a="*"
    print(a*i)


print("--range()---")
print(list(range(10)))
print(list(range(2000,2000)))
print(list(range(1,200,50)))

for i in range(1,15):
    a="*"
    print(a*i)
print("----while---")
value=10
while value>0:
    value-=1
    a="*"
    print(a*value)

print("----리스트컴프리핸션---")
lst=list(range(1,11))
print([i**2 for i in lst if i>5])

for i in lst:
    print(i*j  for j in lst if (j>5))


tp = ("apple", "orange", "kiwi")
print ([len(i) for i in tp])














