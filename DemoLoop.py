#while구문
value = 5
while value > 0:
    print(value)
    value -= 1

#for in구문
lst = [100, "python", 3.14]
for item in lst:
    print(item, type(item))

print("---dict형태---")
fruits = {"apple":"red", "kiwi":"green"}
for k, v in fruits.items():
    print(k, v)

#함수 정의
def getBiggerThan20(i):
    return i > 20

print("---필터링 함수 있음---")
itemL = filter(getBiggerThan20, lst)
for item in itemL:
    print(item)

print("---람다 함수 있음---")
itemL = filter(lambda)



