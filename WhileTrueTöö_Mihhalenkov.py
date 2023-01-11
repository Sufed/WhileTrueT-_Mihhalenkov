from random import *
#5 Вариант
#Harjutus 1.
число=int(input("Число: "))
while число <= 10:
    число += 1
for число in range(1,11):
    print("Цикл: ", число)
print()

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
#Harjutus 5.
while True:
    try:
        n=int(input("Размер квадрата: "))
        break
    except:
        print("Неправильно.")
for a in range(n): 
    for b in range(n):
        if a==b or a+b==n-1:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()
