# demoif.py
from re import A


score = int(input('Input Score: '))
print(score)
if (90<=score<=100):
    grade="A"
elif (80<=score<90):
    grade="B"
elif (70<=score<80):
    grade="C"
elif (score<70):
    grade="D"

print("grade is " + grade)