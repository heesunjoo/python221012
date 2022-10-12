# demoIndex.py
strA="python is very powerful"
strB="파이썬은 강력해"
print(strA[0])
print(strA[0:6])
print(strA[:6])
print(strB[:])
print(strB[-3:])

# 리스트 형식 연습
colors = ["red", "blue", "green"]
print ( len(colors))
print ( colors [0])
colors.append("white")
colors.insert(1, "pink")
print(colors)
colors += ["red"]
colors.append("red")
print(colors)
print(colors.count("red"))
print(colors.index("red"))
print(colors.index("red", 1))
print(colors.index("red", 0))
print(colors)
print(colors.pop())
print(colors.pop())
print(colors.pop(1))
print(colors)
colors.remove("red")
colors.extend(["blue","white","black"])
colors.sort()
print(colors)
colors.reverse()
print(colors)

