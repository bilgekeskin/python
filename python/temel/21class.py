#veri tipi oluşturma
class Account:
    def __init__ (self,isim,numara,bakiye): #objemizde hangi özelliklerin olacağını oluşturuyoruz, self olmak zorunda
        self.isim = isim
        self.numara = numara
        self.bakiye = bakiye
    def hesap_bilgileri(self):
        print("İsim : ",self.isim)
        print("Numara : ",self.numara)
        print("Bakiye : ",self.bakiye)
    def para_cek(self,miktar):
        if (self.bakiye - miktar < 0):
            print("Bakiyeniz yeterli değil!")
        else:
            self.bakiye -= miktar
            print("Yeni Bakiye: ",self.bakiye)
    def para_yatir(self,miktar):
        self.bakiye += miktar
        print("Yeni Bakiye: ",self.bakiye)


account = Account("Bilge Keskin",123456,1000) #objemize 3 tane değer verdik
account.hesap_bilgileri()

account.para_cek(1200)

account.para_yatir(1000)