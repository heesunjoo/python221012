# function2.py
#교집합 문자를 리스트로 리턴
def intersect(prelist, postlist):
    #지역변수 리스트로 초기화
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print (intersect("HAM", "SPAM"))
