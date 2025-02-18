siteadi = " Github sitesinde python ile öğrendiklerimi kendim uygulayip aktariyorum"
website = "https://github.com/"

# 1- ' Github sitesinde ' karakter dizisinin baş ve sondaki boşluk karakterini sil.

# 2- siteadi değişkenindeki tüm karakterleri küçük harfe çevir.

# 3- website değişkeninde kaç tane '.' karakteri vardır?

# 4- website değişkeni 'https' ile mi başlıyor?

# 5- website '/' ile mi bitiyor?

# 6- siteadi içerisindeki tüm karakterler  harflerdenmi oluşuyor?

# 7- siteadi değişkenindeki tüm boşlukları '-' ile değiştir 

# 8- siteadi değişkenindeki python kelimesini javascript ile değiştir.

# 9- website  değişkeni 'www' içeriyormu?

# 10- siteadi değişkenini lsiteye çeviriniz.

#1
siteadi = " Github sitesinde python ile öğrendiklerimi kendim uygulayip aktariyorum"
sonuc = ' Github sitesinde '.strip()
print(sonuc)

#2
siteadi = "Github sitesinde python ile öğrendiklerimi kendim uygulayip aktariyorum"
print(siteadi.lower())

#3
website = "https://github.com/"
print(website.count("."))


#4
website = "https://github.com/"
print(website.startswith("https"))

#5
website = "https://github.com/"
print(website.endswith("/"))

#6
siteadi = " Github sitesinde python ile öğrendiklerimi kendim uygulayip aktariyorum"
print(siteadi.isalpha())


#7
siteadi = "Github sitesinde python ile öğrendiklerimi kendim uygulayip aktariyorum"
print(siteadi.replace(" ", "-"))

#8
siteadi = "Github sitesinde python ile öğrendiklerimi kendim uygulayip aktariyorum"
print(siteadi.replace("python", "javascript"))

#9
website = "https://github.com/"
print(website.find("www"))

#10
siteadi = "Github sitesinde python ile öğrendiklerimi kendim uygulayip aktariyorum"
print(siteadi.split())
