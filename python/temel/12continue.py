#continue = döngüyü başa döndürmek

i = 0

while (i < 10):
    if i == 3 or i == 5:
        i += 1
        continue
    print("i: ",i)
    i += 1