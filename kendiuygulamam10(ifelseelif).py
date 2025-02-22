#1- Bir aracın yakıt tipine göre (benzin,dizel,lpg) belirtilen bir mesafede ne kadar yakıt masrafı olduğunu hesaplayan uygulamayı yapınız.
# benzin : 39.35
# dizel : 41.71
# lpg :20.28


#2-  Bir öğrencinin 2 yazılı bir sözlü notunu alarak ortalama hesaplayınız ve hesaplanan
# ortalamaya göre not aralığına karşılık gelen değerlendirmeyi yapınız.

#   0-24    => 0
#   25-44   => 1
#   45-54   => 2
#   55-69   => 3
#   70-84   => 4
#   85-100  => 5

#1
mesafe=float(input("Katettiğiniz mesafeyi km cinsinden yazınız: "))
yakıttipi=input()
if(yakıttipi == "Benzin" ):
    hesap=39.35 * mesafe
    print("Benzinli aracın katettiği mesafede harcadığı yakıt: ", str(hesap))
elif(yakıttipi == "Dizel"):
    hesap2=41.71 * mesafe
    print("Dizel aracın katettiği mesafede harcadığı yakıt: ", str(hesap2))
elif(yakıttipi == "Lpg"):
  hesap3=20.28 * mesafe
  print("Lpg li aracın katettiği mesafedeki harcadığı yakıt: ", str(hesap3))
else:
 print("Yanlış Yakıt Tipi Girdiniz.")

 #2
 not1=int(input("1. Yazılı notunu giriniz: "))
 not2=int(input("2. Yazılı notunu giriniz: "))
 sözlü=int(input("Sözlü notunu giriniz: "))
toplam=not1+not2+sözlü 
notortalama= toplam / 3
if(notortalama >=0 and notortalama <= 24):
   print("Ders not Ortalamanız: ", str(notortalama))
   print("Ders puanınız:0")
elif(notortalama >=25 and notortalama <= 44):
   print("Ders not Ortalamanız: ", str(notortalama))
   print("Ders puanınız:1")   
elif(notortalama >=45 and notortalama <= 54):
   print("Ders not Ortalamanız: ", str(notortalama))
   print("Ders puanınız:2")
elif(notortalama >=55 and notortalama <= 69):
     print("Ders not Ortalamanız: ", str(notortalama))
     print("Ders puanınız:3")   
elif(notortalama >=70 and notortalama <= 84):
   print("Ders not Ortalamanız: ", str(notortalama))
   print("Ders puanınız:4")
elif(notortalama >=85 and notortalama <= 100):
      print("Ders not Ortalamanız: ", str(notortalama))
      print("Ders puanınız:5")     