# demoIndex2.py

# 리스트 형식 연습
colors = ["red", "blue", "green"]
colors += ["red"]
colors.append("red")
print(colors)
print(colors.count("red"))
print(colors.index("red"))
print(colors.index("red", 1))
print(colors.index("red", 2))
## 버그라고한다. 이런경우 수동으로 다 풀어줘야한다.
print(colors)

