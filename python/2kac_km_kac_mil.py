km = input("Kilometre Değerini Giriniz = ")
bir_mil = 1.609344 #km

mil_cevirme = (float(km)/bir_mil) #ya da inputta type casting yapabilirsin
#km = float(input("Kilometre Değerini Giriniz = "))

print(mil_cevirme)
print(str(km) + " Km = " + str(mil_cevirme) + " mil eder.")
