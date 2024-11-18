# DemoListSet.py

colors = ["red", "blue", "green"]
print(colors)
colors.append("white")
print(colors)
colors.append("yellow")
print(colors)
colors.remove("blue")
print(colors)

#set형식
a = {1,2,3,3}
b = {3,4,4,5}
print(a)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

#Tuple형식
tp = (10, 20, 30)
print(tp)
print(len(tp))

#함수 정의(튜플 사용)
def calc(a,b):
    return a+b, a*b

#호출
Result = calc(3,4)
print(Result)

print("id: %s, name: %s" % ("kim","김유신"))

#형식변환(Type Casting)
a = set((1,2,3))
print(a)
b = list(a)
b.append(4)
print(b)
