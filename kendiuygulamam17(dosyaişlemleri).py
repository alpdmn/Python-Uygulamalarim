# Not Uygulaması

# 1- Menu
    #1- Not Gir
    #2- Ortalamaları Göster (90-100 -> AA, 85-89 -> BA),
    #3- Notları Kayıt Et
    #4- Çıkış
def nothesapla(satir):
    satir= satir[:-1]
    liste=satir.split(":")

    ogrenciadi= liste[0]
    notlar= liste[1].split(",")

    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ortalama=(not1 + not2 + not3) / 3
    if ortalama >= 90 and ortalama <=100:
        harf= "AA"
    elif ortalama >= 80 and ortalama <=89:
        harf = "BA"
    elif ortalama >= 75 and ortalama <=79:
        harf = "BB"
    elif ortalama >= 70 and ortalama <=74:
        harf = "CB"
    elif ortalama >= 65 and ortalama <=69:
        harf = "CC"
    elif ortalama >= 60 and ortalama <=64:
        harf = "DC"
    return f"{ogrenciadi} ':' {harf}  (  {ortalama}  )"
def notgir():
    ad = input("öğrenci adi: ")
    soyad = input("öğrenci soyadi: ")
    not1=input("not 1: ")
    not2=input("not 2: ")
    not3=input("not 3: ")

    with open("sinavnotlari.txt","a", encoding="utf-8") as file:
        file.write(ad + ' ' + soyad + ':' + not1 + "," + not2 + "," +not3+"\n")

def notlarioku():
    with open("sinavnotlari.txt","r", encoding="utf-8") as file:
        for satir in file:
            print(nothesapla(satir))

def notlarikaydet():
    with open("sinavnotlari.txt", "r",encoding="utf-8") as file:
        liste=[]
        for satir in file:
            liste.append(nothesapla(satir))
        with open("sonuclar.txt","w",encoding="utf-8") as file2:
            file2.writelines(liste)
while True:
    islem = input("1- Not Gir\n2-Notları Oku\n3-Notları Kayıt Et\n4- Çıkış\nseçim: ")

    if islem =="1":
       notgir() 
    elif islem =="2":
        notlarioku()
    elif islem == "3":
        notlarikaydet()
    else:
        break
