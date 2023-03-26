#r kipi dosyayı okumamıza yarar

file = open("ornek_dosya.txt", "r")

veri = file.read() #içine değer verirsek yazdığımız değer kadar karakteri okur
print(veri)

file.close()

#file.seek(10 = dosyamızın 10. karakterinin olduğu konuma git)