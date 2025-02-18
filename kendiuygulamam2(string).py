# araba = "Wolksvagenin en sevdiğim arabasi R-Line Tiguan"

# 1- 'araba' değişkeni içerisindeki karakter sayisi nedir?

# 2- 'araba' içerisindeki 'Wolksvagenin' kelimesini al.

# 3- 'araba' değişkeninin ilk 5 ve son 5 karakterini al.

# 4- 'araba' değişkenini tersten yazdır.

# 5- Klavyeden girilen araba bilgisine göre arabanin modelini, kilometresini ve kaza durumunu yaz.

#1
araba = "Wolksvagenin en sevdiğim arabasi R-Line Tiguan"
karaktersayisi = len(araba)
print(karaktersayisi)

#2
araba = "Wolksvagenin en sevdiğim arabasi R-Line Tiguan"
print(araba[0:12])

#3
araba = "Wolksvagenin en sevdiğim arabasi R-Line Tiguan"
print(araba[0:5])
print(araba[41:46])

#4
araba = "Wolksvagenin en sevdiğim arabasi R-Line Tiguan"
print(araba[ :-1])

#5
araba = "R-Line Tiguan"
model = 2018
kilometre = 42000
kazadurum = "kaput değişen"
arabadurum = f"Arabam {araba}dir. {model} modeldir. Aracim {kilometre} kilometrededir. Aracimda sadece {kazadurum}dir."
print(arabadurum)