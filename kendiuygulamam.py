"""
iki evin  evinin elektrik,su,doğalgaz faturalarini topla ve  kdv oranini baz alarak hesapla
kdv:0.18
daire1: 
daire2:

"""
elektrik = float(input("Elektrik fiyati daire1: ")  )
dogalgaz = float(input("Dogalgaz fiyati daire1: ")  )
su = float(input("Su fiyati daire1: ")  )
elektrik2 = float(input("Elektrik fiyati daire2: "))
dogalgaz2 = float(input("Doğalgaz fiyati daire2: "))
su2 = float(input("Su fiyati daire2: "))
toplam = elektrik + elektrik2 + dogalgaz + dogalgaz2 + su + su2
print(("Elektrik,Su ve Doğalgaz toplami: ") + str(toplam))
kdvoran = toplam * 0.18
print("Dairelerin faturalarinin(elektrik,su,doğalgaz) kdv orani: " + str(kdvoran))
