#1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız.

#2- Dikdörtgenin alan ve çevresini hesaplayan fonksiyonu yazdır.

#3- Yazı tura uygulamasını fonksiyon kullanarak yap.(Random modülü)

#4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazdır.

#5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazdır.


#1
def yazdir(text, adet):
    return text * adet
print(yazdir("Alp ", 10))

#2
def dikdortgencev( kenar1,kenar2,kenar3,kenar4):
    return kenar1 + kenar2 + kenar3 + kenar4

print(dikdortgencev(11,23,34,45))

def dikdortgenalan(uzunkenar ,kisakenar):
    return uzunkenar *kisakenar
print(dikdortgenalan(35,22))

#3
import random
def yazitura():
    sonuc=random.choice(["Yazi", "Tura"])
    return sonuc
print("Sonuç: ", yazitura())

#4
def asalmi(n):
    if n<2:
        return False
    for b in range(2, int(n ** 0.5) + 1):
        if n % b ==0:
            return False
    return True





def asal(sayi1 , sayi2):
    asalsayilar= []
    for b in range(sayi1 , sayi2 + 1):
        
            if asalmi(b):

                asalsayilar.append(b)
    return asalsayilar
sayi1 = int(input())
sayi2 = int (input())
print(f"{sayi1} ve {sayi2} arasındaki asal sayilar: ", asal(sayi1,sayi2))








#5
def bolensayi(sayi):
    bolunenler = []
    for a in range(1, sayi + 1):
        if sayi % a == 0:
            bolunenler.append(a)
    return bolunenler
sayi =int(input())     
print(f" {sayi} sayisinin tam bölenleri: ", bolensayi(sayi))    