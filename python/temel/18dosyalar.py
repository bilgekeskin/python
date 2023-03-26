file = open("ornek_dosya.txt", "w") #w kipi dosyayı açmak ve yazmak için kullandığımız kipimiz

file.write("Hello world!") #dosya içine yazı yazmak

file.close() #her dosya işlemimiz bittiğinde close ile işlemi kapatmak zorundayız

#dosyaya yazdığımız şeyi değiştirdiğimizde diğerleri silinmesin istiyorsak üstüne eklemek için w yerine a kipini(append) kullanmalıyız
#alt alta yazdırma işlemi için her stringten sonra \n yoksa a kipi hemen sonuna ekler