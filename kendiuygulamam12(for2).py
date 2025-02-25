urunler=[
    {"urunadi":"Hp Victus", "fiyat": 32999},
    {"urunadi":"Lenovo Thinkpad", "fiyat": 25499},
    {"urunadi":"Apple Macbook", "fiyat": 49999},
    {"urunadi":"Huawei Matebook", "fiyat": 26999},
    {"urunadi":"Casper Nirvana", "fiyat": 20000},
]

#1- Aşağıdaki örnek cümleyi tüm ürünlere uygula.
   #  "Hp Victus marka ürünün fiyatı 32999 Türk Lirası"

#2- Ürünlerin Toplam Fiyatı nedir?

#3- 25000 ile 40000 arasındaki ürünleri listele

#4- Kullanıcıdan alınan anahtar kelimeye göre ürünleri listeleyiniz.


#1
urunler=[
    {"urunadi":"Hp Victus", "fiyat": 32999},
    {"urunadi":"Lenovo Thinkpad", "fiyat": 25499},
    {"urunadi":"Apple Macbook", "fiyat": 49999},
    {"urunadi":"Huawei Matebook", "fiyat": 26999},
    {"urunadi":"Casper Nirvana", "fiyat": 20000},
]
for a in urunler:
    
    print(f"{a["urunadi"]} marka ürünün fiyatı {a["fiyat"]} Türk lirası")

#2
urunler=[
    {"urunadi":"Hp Victus", "fiyat": 32999},
    {"urunadi":"Lenovo Thinkpad", "fiyat": 25499},
    {"urunadi":"Apple Macbook", "fiyat": 49999},
    {"urunadi":"Huawei Matebook", "fiyat": 26999},
    {"urunadi":"Casper Nirvana", "fiyat": 20000},
]
toplam=0
for b in urunler:
    toplam += b["fiyat"]
print(toplam)

#3
urunler=[
    {"urunadi":"Hp Victus", "fiyat": 32999},
    {"urunadi":"Lenovo Thinkpad", "fiyat": 25499},
    {"urunadi":"Apple Macbook", "fiyat": 49999},
    {"urunadi":"Huawei Matebook", "fiyat": 26999},
    {"urunadi":"Casper Nirvana", "fiyat": 20000},
]
for c in urunler:
    if(c["fiyat"]>25000 and c["fiyat"]<40000):
        print(c)

#4
urunler=[
    {"urunadi":"Hp Victus", "fiyat": 32999},
    {"urunadi":"Lenovo Thinkpad", "fiyat": 25499},
    {"urunadi":"Apple Macbook", "fiyat": 49999},
    {"urunadi":"Huawei Matebook", "fiyat": 26999},
    {"urunadi":"Casper Nirvana", "fiyat": 20000},
]
kelime = input("aramak istediğiniz ürün: ")

for d in urunler:
    if((d["urunadi"]).lower().find(kelime.lower()) > -1):
        print(d)