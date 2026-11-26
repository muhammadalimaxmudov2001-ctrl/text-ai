############  AMALYOT 1

# ism = input("Ismingizni kiriting:")
# yosh =int (input("yoshingizni kiriting:"))
# boy = int( input("Nechanchi maktabda o'qiysiz:"))
# print(f"Boldi siz bilan bog'lanamiz!,", f" ismingiz  {ism}", f"Maktabingiz {boy}",f" yoshingiz {yosh} " ," Siz bilan bog'lanamiz")

####### AMALYOT 2

# yosh = int(input("Yoshingizni kiriting:"))
# yangi_yosh = yosh +1
# print(f"Sizning yoshingiz {yosh} da , keyingi yili siz yani 2027-yil {yangi_yosh} ga to'lasiz")

##### Amalyot 3

# son1 = int (input("1-pul miqdorini kiriting:"))
# son2 = int (input("2-son miqodorini kiriting:"))
# print(son1 * son2 , son1 + son2 , son1 - son2)

#############     AMALYOT 4

# print("LUX PARFUMEGA HUSH KELIBSIZ!")
# maxsulot = input("Maxsulot nomini kiriting:")
# narxi = float( input("Maxsulot narxini kiriting:"))
# soni = int( input ("Sonini kiriting:"))

# umumiy = narxi * soni
# print(f"maxsulot nomi: {maxsulot}, narxi:{narxi} $ , soni: {soni} ta")
# print(f"Umumiy to'lov {umumiy} $ , tashrifingizdan mamnunmiz😊")


############ 3-leeson amalyot #############

# son =int(input("Son kiritinchi korayluchi: "))

# if son >0:
#     print("Soningiz musbat")
# elif son <0:
#     print("soningiz manfiy")




# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <1 and yosh >=7:
#     print("Halidetskiy ekansan ukaam")
    
# elif yosh <8 and yosh <=17:    
#         print("Ha yaxwi maktabbi bitirarkansizda")
# elif yosh <18 and yosh >=35:
#     print("Oka tuzumisiz")
# elif yosh > 36 and yosh <=60:
#     print("Assalomu aleykuuum bratim") 
# else:
#     print("Yaxwi dam olin")   
    

############################### 

# for i in range (1, 7):
#     print(f"{i} Marta alom python")

##

# for n in range(1, 11):
#     print(f"7 * {n} = {7*n}")
    
    
# for raqam in range(1, 21 ,2):   
#     print(f"{raqam} to'gson")
    
# for raqam in range(2, 21 ,2):   
#     print(f"{raqam} jup son")


# for i in range(1,21):
#     if i % 2:
#         print(f"{i}juft sonku")
#     else:
#         print(f"{i} toq")




# son = 1
# while son <= 100:
#     if son % 2 == 0:
#         print(son)
#     son += 1    #increament


# son = 1
# while son <= 10:
#     print(f" 5 * {son} = {5 * son}")
#     son =+ 1 


















# import random 

# random_son = random.randint(1,10)

# urinishlar = 0

# while True:


#     if urinishlar == 3:
#         print("II  buldi qanchagacha yozmoqchisiz ")
#         break
#     taxmin = int(input("1 dan 10 gacha son kiriting: "))
    
#     urinishlar += 1

#     if taxmin == random_son:
#         print("Malades malades topdi")
#         print("nma ko'paytirvordin ukajonim: ", urinishlar)

#         break


    


#         break
#     elif taxmin < random_son:
#         print("kattaroq son kiritng!")

#     else:
#         print("Kichikroq son kiriting!")
        
        







hisobdagi_pul = 100

while True:

    print("Hisobingizdagi pul" ,hisobdagi_pul)
    pul = int(input("Nech pul yechasan: "))

    if hisobdagi_pul < pul:
        print("Gaday puli kam")

    elif hisobdagi_pul > pul:
        print(hisobdagi_pul - pul)

        break