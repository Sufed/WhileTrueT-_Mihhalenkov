from random import *
#5 Вариант
number = int(input("Enter a number: "))
max_number = number + 10

while number <= max_number:
    print("Current number: ", number)
    number += 1
#Harjutus 5.
while True:
    try:
        n=int(input("Размер квадрата: "))
        break
    except:
        print("Неправильно.")
for a in range(n): #Переменная a это строчка
    for b in range(n): #Переменная b это столб
        if a==b or a+b==n-1:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()
#Harjutus 0.
число = int(input("Число1: "))
#Число максимальное сделать и +10 под while
максчисло = число+10
while число <= максчисло:
    число += 1
for число in range(число,максчисло+1):
    print("Цикл: ", число)
print()
#Harjutus 0.1.
while True:
    try:
        число = int(input("Число: "))
        break
    except:
        print("On vaja arvude tüüp kasutada")
if число <= 10:
    число += 1
else:
    print("Неа, нужно от 1-го:", end=" ")
for число in range(1,11):
    print("Цикл: ", число)

#Harjutus 1(6)
for x in range(5):
    print("******")
#Harjutus 2(6)
n=0
print("kolmnurga")
for e in range(11,0,-1):
    n = n + 1
    for f in range(0,n+1):
        print("*", end="")
    print()
print("")
#Harjutus 3(6)
n=0
print("kolmnurga")
for e in range(11,0,-1):
    n = n - 1
    for f in range(0,n-1):
        print("*", end="")
    print()
#Harjutus 4(6)
for i in range(1,11):
    print("*"*i, end="")
    print()
#Ёлка
for i in range(1,5):
    x=str("*"*i).center(18," ")
    print(x, end="")
    print()
for i in range(1,7):
#    x=str("*"*i(i+2)).center(18," ")
    print(x, end="")
    print()
for i in range(1,10):
    x=str("*"*i(i+4)).center(18," ")
    print(x, end="")
    print()
