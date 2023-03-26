file = open("ornek_dosya.txt", "r")

for satir in file:
    #döngü kullanarak dosyamızı okuyabiliriz
    print(satir)

file.close()