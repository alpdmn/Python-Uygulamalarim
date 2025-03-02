class Bankahesabi:
    def __init__(self, hesapsahibi):
        self.hesapsahibi =hesapsahibi
        self.bakiye=0.0

    def getbakiye(self):
        return self.bakiye


    def parayatir(self , miktar):
        self .bakiye += miktar
        return self.bakiye
    

    def paracek(self , miktar):
        self.bakiye -= miktar
        return self.bakiye
    
hesap = Bankahesabi("Alp Duman")
print(hesap.parayatir(1000))
print(hesap.getbakiye())
hesap.paracek(500)
print(hesap.getbakiye())
hesap.paracek(200)
print(hesap.getbakiye())
