a = 3 
b = 3.14
c = "python"
d = [1,2,3,4,5,"python"]
e = (1,2,3,4,5,"python") #tuple immutable(değiştirilemez) veri tipi
f = {"elma":3,"armut":4,"kiraz":5}
g = False
h = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))
print(type(g))
print(type(h))

print(a,b,c,d,e,f,g,h)



# Tip dönüşümleri

x ='3'
print (type(x))
y = 4
print (type(y))

print (x*y)  # Tip3: Sonucu 12 bekliyorsak Anlamsal hataya (Tip3) düşeriz. 

# Bu durumda hata almamak için:

print (int(x)*y)

# int () içerisine gönderdiğimiz string mutlaka rakamlardan oluşmalıdır. Negatif olabilir.
# Aksi halde runtime hatası alınır.




"""


DERSTEKİ NOTLAR

-print ile farklı tipteki değerler tek seferde ekrana yazdırılabilir.

-Bir değişkenin değerini ve tipini program akışında değiştirebilirsiniz.

-Önce işlem sonra atama yapılır.
    
Değişken ismi belirlemede kural:
 -A-Z, a-z ve alt çizgi ile başlayabilir. Ancak rakam ile başlayamaz
 -A-Z, a-z ve rakam kombinasyonları kullanılabilir. Rakam ile başlaması yasaktır.
 -Matematiksel işleçler gibi özel karakterler kullanılamaz.

Yanlış kullanıma örnekler: 
 -değer$ = 12
 -abc?
 -9x = 5

-Değişken isimleri büyük küçük harf duyarlılığına sahiptir.

-Anahtar kelimeler değişken isimleri olarak rastgele atanamazlar.

Yanlış kullanıma örnek: 
 -lambda = 23
 -lambda anahtar kelimedir. Herhangi bir değişken ataması için kullanılamazlar. 

-Anahtar kelimeler listesini bulmak için önce keyword modülünün projeye eklenmesi ve ardından aşağıdaki kod satırının yazılması gereklidir
 print (keyword.kwlist)

-Python yorumlayıcının çalıştırabildiği en küçük program koduna ifade denir. Bir program birçok ifadeden oluşur.

-hesaplama yapabilen özel karakterlere işleç denir

-işleç tarafından işlenen değerlere işlenen denir.

-Matematiksel işlemlerin öncelik sırası python'da uygulanmaktadır.    


"""