from Isprime import *
end = int(input("Enter a valid number ranging from 1 to 100"))
numList = range(1, end, 1)

for num in numList:
    if isprimeFunction(num):
        print(num)