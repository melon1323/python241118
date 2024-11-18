# function.py
#1)함수를 정의
def times(a,b):
    return a*b

#2)함수를 호출
result = times(5,6)
print(result)

def setValue(newValue):
    #지역변수
    x = newValue
    print("함수내부:", x)

#호출
result = setValue(5)
print(result)

#교집합을 리턴 함수
def intersect(prelist, postlist):
    result = []
    for x in prelist:
        if x in postlist and x not in result:
            result.append(x)
    return result

#호출
print(intersert("HAM","SPAM"))