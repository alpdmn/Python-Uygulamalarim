# Aşağıdaki futbolcu bilgilerini dictionary listesinde sakla.
  #futbolcu1: 99 Mario Lemina 1993 19 1 3
  #futbolcu2: 9 Mauro İcardi 1993 14 6 1
  #futbolcu3: 45 Victor Osimhen 1998 24 19 5

# Aşaüıdaki Cümleyi Yazdır.
 # 99 forma numaralı Mario Lemina ismindeki futbolcunun doğum yılı 1993 ve çıktığı maç sayısı 19


futbolcu1={
         'Ad-Soyad':'Mario Lemina',
         'Doğum Yili':1993,
         'Oynadiği maç sayisi':19,
         'Gol sayisi':1,
         'Asist Sayisi':3,
         'Forma Numarasi':99

     }
futbolcu2={
         'Ad-Soyad':'Mauro İcardi',
         'Doğum Yili':1993,
         'Oynadiği maç sayisi':14,
         'Gol sayisi':6,
         'Asist Sayisi':1,
         'Forma Numarasi':9

     }
     



futbolcu3={
         "Ad-Soyad":'Victor Osimhen',
         'Doğum Yili':1998,
         'Oynadiği maç sayisi':24,
         'Gol sayisi':19,
         'Asist Sayisi':5,
         'Forma Numarasi':45

     }
print(futbolcu1)
print(futbolcu2)
print(futbolcu3)

cümle=f"{futbolcu1['Forma Numarasi']} forma numarali {futbolcu1['Ad-Soyad']} isimli futbolcunun doğum yili {futbolcu1['Doğum Yili']} ve çiktiği maç sayisi {futbolcu1['Oynadiği maç sayisi']}"
cümle2=f"{futbolcu2['Forma Numarasi']} forma numarali {futbolcu2['Ad-Soyad']} isimli futbolcunun doğum yili {futbolcu2['Doğum Yili']} ve çiktiği maç sayisi {futbolcu2['Oynadiği maç sayisi']}"
cumle3=f"{futbolcu3['Forma Numarasi']} forma numarali {futbolcu3['Ad-Soyad']} isimli futbolcunun doğum yili {futbolcu3['Doğum Yili']} ve çiktiği maç sayisi {futbolcu3['Oynadiği maç sayisi']}"
print(cümle)
print(cümle2)
print(cumle3)