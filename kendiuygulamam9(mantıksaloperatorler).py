#1- Yaşı 18' den büyük yada veli izni varsa bir işte çalışabilir durumunu kontorl ediniz.

#2- Ders notu 50-100 arasındaysa geçti değilse kalsın bilgisini yazdırınız.

#3- Not ortalaması en az 70 puan ve zayıfı yoksa teşekkür belgesi alabilme durmunu kontrol ediniz.

#4- İşe girmek için en az önlisans ya da lisans mezunu olma durumunu kontrol ediniz.Sigara kullanmama koşulu.

#5- Uygulamaya giriş kontrolünü  "username yada email" yada "parola" için yapalım.



#1
x=int(input())
izin=input()

sonuc = x>18 or izin=="var"
print( sonuc )

#2
not1=float(input())
koşul = not1>=50 and not1<=100
print(koşul, "Dersi Geçti")
koşul2= not1<=50 
print(koşul2, "Dersten kaldı")

#3
not1= int(input())
zayıf="yok"

koşul= not1>=70 and zayıf=="yok"
print("teşekkür belgesi aldınız")

#4
lisans=input()
önlisans=input()
koşul = önlisans== "var" or lisans== "var"
print(koşul , "işe girebilirsiniz")

#5
username = "alperen"
email ="dumannalperenn@gmail.com"
parola="12345"
girilenbilgi = input("email yada username: ")
girilenbilgi2=input("parola: ")

koşul= (username==girilenbilgi) or (email==girilenbilgi) and (parola==girilenbilgi2)
print(koşul)