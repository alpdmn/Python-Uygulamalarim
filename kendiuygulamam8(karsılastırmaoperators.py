#1- Girilen 2 sayıdan hangisi büyüktür?

#2- Girilen bir sayının tek çift kontrolünü yapınız.

#3- Bir öğrencinin girilen 3 notuna göre başarı durumunu kontrol ediniz.50 ve üstünde başarılı.

#1
sayi=int(input())
sayi2=int(input())
sonuc=(sayi>sayi2)
print(f"{sayi} {sayi2} den büyük {sonuc}")

#2
sayi=(int(input()))
sonuc=(sayi % 2 == 1)
print(sonuc)

#3
not1=float(input())
not2= float(input())
not3=float(input())
sonuc=not1>50
sonuc2=not2>50
sonuc3=not3>50
print(f"{sonuc} dersi geçtiniz")
print(f"{sonuc2} dersi geçemediniz")
print(f"{sonuc3} dersi geçtiniz")