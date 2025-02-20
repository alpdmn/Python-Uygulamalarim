customers = ["alitopaç","icardi","muslera","osimhen","lemina"]
ordertotals = [12000,30000,40000,75000,34500]

#1- "frankowski" kullanıcı adıyla yapılan 20000 liralık sipariş ekle.

#2- Son eklenen siparişi sil.

#3- Tüm müşteriler için aşağıdaki özet cümleyi yazdır.
     # '<username>' isimli müşterinin sipariş toplamı '<10000>' liradır

#4- Müşterileri alfabetik olarak sırala.

#5- Sipariş toplamlarını azalan şekilde sırala.

#6- En düşük sipariş hangisi?

#7- 'lemina' isimli kullanıcının kaç tane siparşi var?

#8-  Customers listesinden 'muslera' isimli kullanıcıyı sil.

#9- Listelerdeki tüm içerikleri sil.

#10- Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamarını listeye ekle.

#1
customers.append("frankowski")
ordertotals.append(20000)
print((customers) + (ordertotals))

#2
ordertotals.pop(5)
print(ordertotals)

#3
sonuc=f"{customers[0]} isimli müşterinin sipariş tutari {ordertotals[0]}"
sonuc=f"{customers[1]} isimli müşterinin sipariş tutari {ordertotals[1]}"
sonuc=f"{customers[2]} isimli müşterinin sipariş tutari {ordertotals[2]}"
sonuc=f"{customers[3]} isimli müşterinin sipariş tutari {ordertotals[3]}"
sonuc=f"{customers[4]} isimli müşterinin sipariş tutari {ordertotals[4]}"
print(sonuc)




#4
customers.sort()
print(customers)

#5
ordertotals.reverse()
print(ordertotals)

#6
minsayi=min(ordertotals)
print(minsayi)

#7
customers.count("lemina")
print(customers)


#8
customers.remove("muslera")
print(customers)

#9
#customers.clear()
#ordertotals.clear()
print(customers)
print(ordertotals)

#10

customers.append(input())
ordertotals.append(input())
print(customers)
print(ordertotals)
