﻿from random import *
#5 Вариант
#Harjutus 1.
число=int(input("Число: "))
while число <= 10:
    print("Цикл: ", число)
    число += 1
for число in range(1,11):
    print("Цикл: ", число)
print()
#Harjutus 5.
n=int(input("Размер квадрата: "))
for a in range(n):
    for b in range(n):
        if a+b==n-1:
            print("X", end=" ")
        else:
            print("O", end=" ")
print()
#https://moodle.edu.ee/mod/assign/view.php?id=1937108
