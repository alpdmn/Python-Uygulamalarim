

#1- Kullanıcıdan alınan 2 sayının çarpımı ile a,b,c toplamının farkı nedir

#2- c'nin b'ye kalansız bölümünü hesapla

#3- (a,b,c) toplamının mod 7' si nedir?

#4- b'nin a. kuvvetini hesaplayınız.

#5- a, *b, c = (2,4,6,8,13) işlemine göre c' nin küpü nedir?

#6- a, b, *c = (2,4,6,8,13) işlemine göre c' nin değerleri toplamı nedir

#1
sayi=int(input())
sayi2 =int(input())
a, b, c = 4, 8, 12
carpma= sayi*sayi2 
toplama=a+b+c
sonuc=carpma-toplama
print(str(sonuc))

#2
a, b, c = 4, 8, 12
sonuc=c // b
print(sonuc)

#3
a, b, c = 4, 8, 12
toplama=a+b+c
sonuc =toplama%7
print(sonuc)

#4
a, b, c = 4, 8, 12
usalma=b **a
print(usalma)

#5
a, *b, c = (2,4,6,8,13)
sonuc=c**3
print(sonuc)

#6
a, b, *c = (2,4,6,8,13)
toplama=6+8+13
print(toplama)