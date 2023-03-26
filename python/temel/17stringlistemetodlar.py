liste = [1,2,3,4,5,6]
a = "araba"

print(a.startswith("ar")) #a stringimiz a ile başlıyor mu?true false döndürür
print(a.endswith("s")) #a ile bitiyo mu

print(a.replace("a","o")) #a karakterlerini o ile değiştirir

liste.append("python") #en sonuna istediğimizi ekler
print(liste)

liste.pop() #listenin son elemanını listeden çıkartır, içine indeks değeri verirsek o indeksi çıkartır
print(liste)

"""
DERSTEKİ NOTLAR

-print(liste10.count(4)) # 4 sayısının liste içerisinde kaç defa tekrar edildiğini döner

-liste10.extend(liste11) # liste 10'a liste 11'i ekler. None döner.

-print (liste10.index(4)) # 4 sayısının listedeki indeksinin ilk görüldüğü yeri döner

-liste10.insert(1, 25) # indeks 1 konumuna 25 sayısını yerleştir. Eleman silmez. Araya yerleştirir. None döner.

-liste10.remove(32) # ilk görülen konumdaki 32 değerini listeden kaldırır. None döner.

-liste10.reverse() # listeyi tersine çevirir. None döner.

-liste10.sort() # listeyi artan biçimde yeniden yazar. None döner.


"""