#Bankamatik Uygulaması

#Hesap Bilgileri Tutulacak(dict olarak) 3-5 kullanıcının hesap bilgisi

# menu, paracekme, bakiyesorgula, parayatirma fonksiyonları tanımlanacak.

#çekilmek istenen tutar hesapta yok ise ek hesap kullanılmak istendiği sorulacak.

hesaplar = [
    {
        "ad":"Alp Eren Duman",
        "hesapno":"12345",
        "bakiye":35000,
        "ekhesap":10000,
        "username":"alpdmn",
        "password":"alp123",
        "ekhesaplimit":15000
    },
    {
        "ad":"Ali Sönmez",
        "hesapno":"123456",
        "bakiye":55000,
        "ekhesap":20000,
        "username":"alisön",
        "password":"ali123"

    },
    {
        "ad":"Furkan Kıran",
        "hesapno":"1234567",
        "bakiye":10000,
        "ekhesap":2000,
        "username":"furkir",
        "password":"fur123",
        "ekhesaplimit":15000
    },
    {
        "ad":"Mehmet Boz",
        "hesapno":"12345678",
        "bakiye":60000,
        "ekhesap":30000,
        "username":"mehboz",
        "password":"meh123",
        "ekhesaplimit":35000
    }



]
def menu(hesap):
    print("\n")

    print(f"merhaba, {hesap["ad"]}")

    print("1- Bakiye Sorgulama")
    print("2- Para Çekme")
    print("3- Para Yatırma")

    islem = input("Yapmak istediğiniz işlem: ")

    if islem == "1":
       bakiyesorgula(hesap)
    elif islem == "2":
        paracekme(hesap)
    elif islem == "3":
        parayatirma(hesap)
    else: 
        print("yanlış seçim")
    menu(hesap)

def bakiyesorgula(hesap):
    print(f"bakiye: {hesap["bakiye"]}")
    print(f"ek bakiye: {hesap["ekhesap"]}")
    print(f"ek bakiye limit: {hesap["ekhesaplimit"]}")
def paracekme(hesap):
    miktar = float(input(" çekmek istediğiniz miktarı girin: "))
    if hesap["bakiye"] >= miktar:
        hesap["bakiye"] -= miktar
        print("paranizi alabilirsiniz.")
    else:
        toplam = hesap["bakiye"] + hesap["ekhesap"]

        if toplam >= miktar:
            ekhesapkullanimizni = input("ek hesap kullanilsinmi? (e/h)")
            if ekhesapkullanimizni == "e":
                kullanilacakmiktar= miktar - hesap["bakiye"]
                hesap["bakiye"] = 0
                hesap["ekhesap"] -= kullanilacakmiktar
            else:
                print("üzgünüz bakiyeniz yetersiz")
        else:
            print("Bakiyeniz Yetersiz.")
def parayatirma(hesap):
    islem = input("Paranizi bakiyeyemi yoksa ek hesabami yatirmak istersiniz? (b/e)")
    if islem == "b":

        yatirilicaktutar= float(input("Yatirmak istediğiniz tutarı girin: "))
        hesap["bakiye"] += yatirilicaktutar     
        print(f"Yatirdiğiniz tutar: {yatirilicaktutar}, Yeni bakiyeniz: {hesap["bakiye"]}")
    if islem == "e":
       yatirilicaktutar= float(input("Yatirmak istediğiniz tutarı girin: "))
       if yatirilicaktutar > hesap["ekhesaplimit"]:
           print("Yatiracağiniz tutar ek hesap limitinden yüksektir")
       elif yatirilicaktutar == hesap["ekhesaplimit"] - hesap["ekhesap"]:
           hesap["ekhesap"] += yatirilicaktutar
           print(f"Ek hesaba yatirdiğiniz tutar: {yatirilicaktutar}, Ek hesap bakiyeniz {hesap["ekhesap"]}")
           

    
def login():
    username = input("username: ")
    password = input("password: ")
    isLoggedIn = False
    for hesap in hesaplar:
        if hesap["username"] == username and hesap["password"] == password:
            isLoggedIn=True   
            menu(hesap)
            break

    if not (isLoggedIn):
        print("username veya password yanliş")
login()