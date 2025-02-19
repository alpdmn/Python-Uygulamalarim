#1- "Toyota, Bmw, Renault, Mercedes" elemanlarına sahip markalar isimli liste oluştur

#2- Liste kaç elemanlı?

#3- Listenin ilk ve son elemanı nedir?

#4- "Renault" markasını "Wolksvagen" ile güncelle.

#5- "Wolksvagen" listenin bir elemanı mı?

#6- Listenin ilk 2 elemanını al.

#7- Listenin sonuna "Ford" ve "Citroen" markalarını ekle.

#8- Listenin son elemanını siliniz.

#9- Aşağıdaki verileri liste içerisinde saklayınız.

     #araba1: Tiguan 2018 [50000]
     #araba2: Audia3 2022 [35000]
     #araba3: Megane 2023 [15000]

#10- arabaların kaç yıllık olduğunu  hesapla.

#11- arabaların kilometrelerinin ortalamalarını hesapla.


#1
markalar = ["Toyota", "Bmw", "Renault", "Mercedes"]
print(markalar)

#2
markalar = ["Toyota", "Bmw", "Renault", "Mercedes"]
kaceleman = len(markalar)
print(kaceleman)

#3
markalar = ["Toyota", "Bmw", "Renault", "Mercedes"]
ilkeleman = markalar[0]
soneleman = markalar[3]
print(ilkeleman, soneleman)

#4
markalar = ["Toyota", "Bmw", "Renault", "Mercedes"]
markalar[2] = "Volkswagen"
guncelle = markalar
print(guncelle)

#5
markalar = ["Toyota", "Bmw", "Volkswagen", "Mercedes"]
elemanimi = "Volkswagen" in markalar
print(elemanimi)

#6
markalar = ["Toyota", "Bmw", "Volkswagen", "Mercedes"]
ilk2eleman = markalar[0:2]
print(ilk2eleman)

#7
markalar = ["Toyota", "Bmw", "Volkswagen", "Mercedes"]
ekle = markalar + ["Ford", "Citroen"]
print(ekle)

#8
markalar = ["Toyota", "Bmw", "Volkswagen", "Mercedes"]
del markalar[0]
print(markalar)

#9
arabalar = [["Tiguan", "2018","50000"], ["Audia3", "2022", "35000"], ["Megane", "2023", "15000"]]
print(arabalar) 

#10
araba1 = ["Tiguan", 2018,50000]
araba2 = ["Audia3", 2022, 35000]
araba3 = ["Megane", 2023, 15000]
arabalar = [araba1,araba2,araba3]
tiguanmodel = 2025 - araba1[1]
audia3model = 2025 - araba2[1]
meganemodel = 2025 - araba3[1]
print(tiguanmodel, audia3model, meganemodel)

#11
araba1 = ["Tiguan", 2018, 50000]
araba2 = ["Audia3", 2022, 35000]
araba3 = ["Megane", 2023, 15000]

kilometreort = araba1[2] + araba2[2] + araba3[2] / 3
print(kilometreort)