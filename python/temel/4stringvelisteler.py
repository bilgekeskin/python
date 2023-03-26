a = "python"
b = [1, 2, 3, 4, 5, 6, 7]

print(a[0])
print(a[1])
print(a[2])

print(len(a))  # karakter sayısı
print(len(b))

print(a[len(a)-1])  # son karakteri alma
print(b[len(b)-1])

print(a[0:2]) # 0. indeksten 2.indekse kadar yaz 2.indeks dahil değil
print(a[2:]) # 2.indeksten sonuna kadar yaz 2.dahil
print(a[:4]) #4.indekse kadar yaz 4.dahil değil
print(b[0:6:2]) #0dan başla 6ya kadar ikişer atlayarak git
print(b[::2]) #baştan sona kadar ikişer atlayarak yaz


"""
DERSTEKİ NOTLAR

liste oluşturma yöntemleri:
 -liste1 = list() bir boş liste
 -liste2 = list([22, 34, 61]) 22, 34, 61 sayılarını içeren bir liste
 -liste3 = list(["ali", "ahmet", "osman"]) stringler listesi
 -liste4 = list("python") p, y, t, h, o, n karakterlerinden oluşan bir liste

in kullanımı:
 -in işleci bir değerin ilgili liste içerisinde olup olmadığını kontrol eder. Var ise True yok ise False döner.
 -not in şeklinde de kullanımı vardır
    
 -print (2 in liste2)
 -print (34 in liste2)
 -print (34 not in liste2)

max, min ve sum fonksiyonları:
 -print(max(liste2)) listedeki maks. değerdeki elamanı döner
 -print(min(liste2)) listedeki min. değerdeki elemanı döner
 -print(sum(liste2)) listedeki tüm elemanları toplar ve sonucu döner

"""