# baho = int(input("Bahoni kiriting: "))

# if baho > 90:
#     print("A")
# elif baho > 80:
#     print("B")
# elif baho > 70:
#     print("C")
# elif baho > 60:
#     print("D")
# else:
#     print("F")




# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i, "juft son")
#     else:
#         print(i, "toq son")



# for i in range(1, 31):
#     if i % 3 == 0:
#         print(i)        











###################################################################################







## 1

i = 1
while i <= 20:
    print(i)
    i += 1
    
    
    
    
    
    
## 2
    
    
i = 20
while i >= 1:
    print(i)
    i -= 1
    
    
    
    
    
# 3
    
i = 2
while i <= 50:
    print(i)
    i += 2
    
    
    
    
    
    
    
## 4
    
    
i = 1
while i <= 10:
    print(7 * i)
    i += 1
    
    
    
### 5
    
    
    
i = 1
yigindi = 0

while i <= 100:
    yigindi += i
    i += 1

print(yigindi)


## 5


i = 1
while i <= 100:
    if i % 5 == 0:
        print(i)
    i += 1
    
    
    
    
### 6
    
    
parol = input("Parolni kiriting: ")

while parol != "python123":
    parol = input("Parol noto'g'ri. Qayta kiriting: ")

print("Parol to'g'ri!")



### 7


parol = ""
i = 0

while i < 3:
    parol = input("Parolni kiriting: ")

    if parol == "python123":
        print("Parol to'g'ri!")
        break
    else:
        print("Parol noto'g'ri!")

    i += 1

if i == 3 and parol != "python123":
    print("Akkaunt bloklandi!")
    
    
    
    
    
    
### 8
    
    
parol = ""
i = 0

while i < 3:
    parol = input("Parolni kiriting: ")

    if parol == "python123":
        print("Parol to'g'ri!")
        break
    else:
        print("Parol noto'g'ri!")

    i += 1

if i == 3 and parol != "python123":
    print("Akkaunt bloklandi!")                    
    
    
    
    
#### 9 bankomat
    
    
    
balans = 100

while True:
    print("Balans:", balans)
    pul = int(input("Pulingizni yechishingiz mumkin (0 - chiqish): "))

    if pul == 0:
        break
    elif pul > balans:
        print("Balansda yetarli pul yo'q!")
    else:
        balans -= pul
        print("Pul yechildi!")

print("Kartada pulingiz qolmadi.")



### 10


import random

son = random.randint(1, 100)
i = 0

while True:
    taxmin = int(input("Sonni toping: "))
    i += 1

    if taxmin == son:
        print("Topdingiz!")
        print("Urinishlar soni:", i)
        break
    elif taxmin < son:
        print("Kattaroq")
    else:
        print("Kichikroq")    




