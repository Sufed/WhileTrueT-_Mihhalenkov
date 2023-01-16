from random import *
from math import *
#5 Вариант
#Harjutus 5.
print("Harjutus 5.")
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
число = int(input("Введи число: "))
max_число = число + 10
while число <= max_число:
    print("Текущее число: ", число)
    число += 1
print()
#Harjutus 0.1.
print("Harjutus 0.1")
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
#for i in range(1,5):
#    x=str("*"*i).center(18," ")
#    print(x, end="")
#    print()
#for i in range(1,7):
#    x=str("*"*i(i+2)).center(18," ")
#    print(x, end="")
#    print()
#for i in range(1,10):
#    x=str("*"*i(i+4)).center(18," ")
#    print(x, end="")
#    print()
#Harjutus 11
print("Arvuti nõistatab numbrit 1-10 ja sina üritad seda ära arvata")
a=randint(1,10)
vastus=int(input("Mis arv on mõstatanud arvutit?: "))
k=p=1
while vastus!=a:
    print("Ära sa ei arvanud ära, proovi uuesti!: ")
    vastus=int(input("Sisesta vastus"))
    k+=1
    p+=1
    if k>2:
        print("Püüdlused on lõppenud")
        b=input("Kas tahad veel kord? ")
        if b.upper()=="JAH":
            k=0
            continue
        else:
            break
if vastus==a:
    print("Palju õnne, sa arvasid ära!", p)
print()
#Harjutus 0
p=0
while True:
    number=int(input("Sisestage number suurem kui 10: "))
    if number>=10:
        print("Õigesti")
        break
    else:
        print("Arv on liiga väike", p)
print("katsed", p)
#Harjutus 22.
print("Ma tahan kommi")
katsed=0
while True:
    answer=input("Tahan kommi! ")
    katsed+=1
    if answer.lower()=="komm":
        print(f"Teil kommid kirjutakse kulus {katsed} katse.")
        break

print("Ma tahan kommi")
katsed=0
answer=""
while answer.lower()!="komm":
    answer=input("Tahan kommi! ")
    katsed+=1
print(f"Katsed: {katsed}.")
print()

#Harjutus 1.
while True:
    try:
        nimi=input("Palun sisesta oma nimi: ")
        if nimi=="SIIM":
            n=int(input("Palun sisesta mitu korda soovid tervitust saada: "))
            for i in range(1,n+1):
                print(f"Ole tervitatud, {nimi}, {i}. korda.")
        else:
            break
    except:
        print("!!!")

while True:
    print("Tere Tulemast!")
    try:
        print("Latte, 2.50 euro.")
        print("Espresso, 2 euro.")
        print("Cappuccino, 3 euro.")
        print("Kakao, 2.20 euro.")
        s=float(input("Sisestage summa: "))
        if s<2 and s>3: break
        m=input("Valige makseviis")
        if m.lower()=="sulraga":
