bilangan =int(input("Masukkan angka yang ingin dicek (11): "))
pembagi = 2
while bilangan % pembagi != 0:
    pembagi = pembagi + 1

if pembagi == bilangan:
    print("Angka primer")

else:
    print("Bukan angka primer")