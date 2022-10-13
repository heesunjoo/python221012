class Person:
    pass
class Bird:
    pass
class Student(Person):
    pass

class Bird2(Student):
    pass



p, s, b, b2= Person(), Student(), Bird(), Bird2()

print("p is instance of Person: ", isinstance(p, Person))
print("s is instance of Person: ", isinstance(s, Person))
print("p is instance of Object: ", isinstance(p, object))
print("p is instance of Bird: ", isinstance(p, Bird))
print("b is instance of Student: ", isinstance(b, Student))
print("b2 is instance of Student: ", isinstance(b2, Student))
print("b2 is instance of Person: ", isinstance(b2, Person))
print("int is instance of Object: ", isinstance(int, object))