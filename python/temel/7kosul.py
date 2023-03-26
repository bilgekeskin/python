yas = int(input("Yaşınızı Girin:"))

if yas < 18:
    print("Reşit değilsiniz.")
else:
    print("Reşitsiniz.")


"""

< küçükse
> büyükse
<= küçük eşitse
>= büyük eşitse
== eşitse
!= eşit değilse

"""    

"""

DERSTEKİ NOTLAR

karşılaştırma işleçleri string için kullanıldığında: 
 -karşılaştırma her iki stringin ilk harflerinden başlanarak yapılır
 -ve alfabetik öncelik dikkate alınır.

 -önemli not: birden fazla koşul doğru olabilir.bu durumda sıralamada ilk olarak doğru olan şarta girilerek alnızca bu ilgili şart içindeki kod koşturulur.

"""