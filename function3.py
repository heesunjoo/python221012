# function3.py
# 함수정의
def connectURI(server, port):
    strURL = "http://" + server + ":" + port
    return strURL

#호출
print (connectURI("credu.com", "80"))
print (connectURI(port="80", server="credu.com"))

#가변인자
def union(*ar):
    result=[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

#호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))

#정의되지 않은 인자
def userURIBuilder (server, port, **user):
    strURL = "http://" + server + ":" + port + "/?"
    for key in user.keys():
        strURL +=key+"="+user[key]+"&"
    return strURL

#호출
print (userURIBuilder("naver.com","80",id="kim",passwd="1234"))
print (userURIBuilder("naver.com", "80", id="kim", passwd="1234",name="mike", age="30"))

#람다 함수
g = lambda x,y:x*y
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())

