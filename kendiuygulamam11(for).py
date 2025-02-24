sayilar =[3,5,7,2,12,32,45]

# 1- "sayilar" listesindeki her bir elemanı yazdır.

# 2- "sayilar" listesindeki hangi sayılar 3 ün katı.

# 3- "sayilar" listesinde tüm sayıların toplamı nedir?

urunler=["apple watch10","ıphone 16pro","ıhpone12","ıphone x","apple watch9"]

# 4- "urunler" listesindeki tüm ıphone markaları listele.

# 5- "urunler" listesindeki kaç adet apple watch ürünü var.


#1
sayilar =[3,5,7,2,12,32,45]
for a in sayilar:
    print(a)

#2
sayilar =[3,5,7,2,12,32,45]
for c in sayilar:
    if c % 3 == 0:
        print(c)



#3
sayilar =[3,5,7,2,12,32,45]
toplam = 0
for b in sayilar:
    toplam += b
    print(toplam)

#4
urunler=["apple watch10","ıphone 16pro","ıhpone12","ıphone x","apple watch9"]
for d in urunler:
    
    print(d.find("ıphone"))
#5
urunler=["apple watch10","ıphone 16pro","ıhpone12","ıphone x","apple watch9"]
for e in urunler:
    print(e.count("apple watch"))
    
    