banyak_bilangan = int(input('masukan banyaknya bilangan: '))
count = 0
n1 = 0
n2 = 1
list_fibonacci = []
while count < banyak_bilangan:
   list_fibonacci.append(n1)
   bilangan_terakhir = n1 + n2
   n1 = n2
   n2 = bilangan_terakhir
   count += 1
 
daftar_string = [str(angka) for angka in list_fibonacci]
deret_string = ', '.join(daftar_string)
print('Deret fibonacci dengan banyak bilangan {} adalah:\n{}'. format(banyak_bilangan, ', '.join(daftar_string)))